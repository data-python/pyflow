<template>

  <div class="deployfe">

    <Alert closable type="warning" title="多个任务一起打包有时会执行失败, 待优化, 暂时建议不要同时部署"/>

  <Tabs destroy-on-hide style="margin-top: 10px;" :editable="true" @delete="handleTabDelete" @add="handleTabAdd" show-add-button auto-switch>

    <TabPane destroy-on-hide :key="config._uid"  v-for="(config, index) of configList.filter(item => !item.isDeleted)" :title="config.taskName">
      
      <p>
        <Input placeholder="任务名称" v-model.trim="config.taskName" />
      </p>

      <Row :gutter="10">
        <Col flex="auto">
        <Input placeholder="工程目录(package.json所在目录)" v-model.trim="config.projectPath" allow-clear />
        </Col>
        <Col flex="100px">
        <Button type="outline" @click="openFolder(config._uid)">选择文件夹</Button>
        </Col>
      </Row>

      <p>
        <Input placeholder="打包命令(vite等工具需全局安装)" v-model="config.buildCmd" allow-clear />
      </p>

      <p>
        <Input placeholder="打包目录" v-model.trim="config.distPath" />
      </p>

      <p>
        <Input placeholder="远程服务器目录" v-model.trim="config.remotePath" />
      </p>
      <p>
        <Input placeholder="远程服务器IP" v-model.trim="config.hostname" />
      </p>
      <p>
        <Input placeholder="远程服务器用户名" v-model.trim="config.username" />
      </p>

      <p>
        <InputPassword placeholder="远程服务器密码" v-model.trim="config.password" allow-clear />
      </p>

      <Space>
        <Button type="outline" :loading="loading[config._uid]"
          :disabled="!config.taskName"
          @click="save(config._uid)">保存</Button>

        <Button type="primary" :loading="loading[config._uid]"
          :disabled="!config.taskName || !config.projectPath || !config.remotePath || !config.hostname || !config.username || !config.password || !config.buildCmd || !config.distPath"
          @click="deploy(config._uid)">部署并保存</Button>

      </Space>

    </TabPane>

  </Tabs>
  </div>

</template>

<script setup>
import { ref, onMounted } from "vue"
import { Notification } from "@arco-design/web-vue";

const tableName = "DeployFe"
const loading = ref({})
const configList = ref([])

onMounted(async () => {

  const res = await window.pywebview.api.listTable(tableName)
  if (res && res.length > 0) {
    configList.value = res
  } else {
    handleTabAdd()
  }

})


const deploy = async (uid) => {
  loading.value[uid] = true

  const { projectPath, remotePath, hostname, username, password, buildCmd, distPath } = configList.value[uid]

  try {
    const res = await window.pywebview.api.deployFe(projectPath, remotePath, hostname, username, password, buildCmd, distPath)
    if (!res) {
      loading.value[uid] = false
      Notification.error(`${configList.value[uid].taskName} 执行出错, 请检查配置`)
      return
    }
  } catch (err) {
    console.log(err)
    loading.value[uid] = false
    Notification.error(`${configList.value[uid].taskName} 执行出错, 请检查配置`)
    return
  }

  loading.value[uid] = false

  await window.pywebview.api.upsertTable(tableName, configList.value[uid], uid)

  // @todo 暂不能保证是部署成功的提示
  Notification.success(`${configList.value[uid].taskName} 执行完毕`)
}

const save = async (uid) => {
  loading.value[uid] = true
  await window.pywebview.api.upsertTable(tableName, configList.value[uid], uid)
  loading.value[uid] = false

  Notification.success(`${configList.value[uid].taskName} 保存成功`)
}


const openFolder = async (uid) => {
  const res = await window.pywebview.api.openFolder()
  if (!res) {
    return
  }
  // console.log(res)
  configList.value[uid].projectPath = res[0]
}


const handleTabAdd = async () => {
  const number = configList.value.length;

  configList.value = configList.value.concat({
    _uid: number,
    taskName: "任务" + (number + 1),
    projectPath: "e:/workspace-electron/pyflow",
    buildCmd: 'vite build',
    distPath: 'dist',
    remotePath: "/opt/temp",
    hostname: "x.x.x.x",
    username: "root"
  })

  await window.pywebview.api.upsertTable(tableName, configList.value[number], number)
};

const handleTabDelete = async(uid) => {
  await window.pywebview.api.upsertTable(tableName, {
      ...configList.value[uid],
      isDeleted: true,
    }, uid)

  configList.value[uid].isDeleted = true  
}


</script>

<style scoped>
/* .deployfe :deep(.arco-tabs-tab-close-btn) {
  display: none;
} */
</style>