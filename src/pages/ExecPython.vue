<template>

  <Alert closable type="warning" title="tinydb不抗揍, 不要连续地点击删除任务。后期会用注解形式自动绑定参数到命令行。" />

  <Tabs :active-key="activeKey" destroy-on-hide style="margin-top: 10px;" @change="handleTabChange" editable
    :show-add-button="fileArgvList && fileArgvList.length < 50" @delete="handleTabDelete" @add="handleTabAdd"
    auto-switch>

    <TabPane destroy-on-hide :key="fileArgv._uid"
      v-for="(fileArgv, idx) of fileArgvList.filter(item => !item.isDeleted)" :title="fileArgv.taskName">

      <Space>
        <Input v-model="fileArgv.taskName" style="width: 150px;" placeholder="任务名称" allow-clear />

        <Button @click="openPyFile(fileArgv._uid)">选择脚本</Button>

        <Button @click="showArg = !showArg">{{ showArg ? '隐藏' : '显示' }}参数栏</Button>

        <Button @click="handleAdd(fileArgv._uid)">新增参数</Button>

        <Button type="outline" :disabled="!fileArgv.taskName" @click="saveConfig(fileArgv._uid)">保存配置</Button>
        <Button type="primary" :disabled="!fileArgv.taskName || !fileArgv.pyFilePath || !code"
          @click="execPyFile(fileArgv._uid)">保存并执行代码</Button>

      </Space>



      <p v-if="fileArgv.pyFilePath">
        Python脚本路径:
        <Link target="_blank" :href="fileArgv.pyFilePath">{{ fileArgv.pyFilePath }}</Link>
      </p>

      <!-- <Divider /> -->

      <p v-show="showArg">
        <FormItem v-for="(arg, index) of fileArgv.argv" :field="`参数${index + 1}`" :label="`参数${index + 1}`"
          :key="index">
          <Input v-model="arg.value" allow-clear />

          <Button @click="handleDelete(fileArgv._uid, index)"
            :style="{ marginLeft: '10px' }">删除参数</Button>
          <Button @click="openFolder(fileArgv._uid, index)" :style="{ marginLeft: '10px' }">打开文件夹</Button>
          <Button @click="openFiles(fileArgv._uid, index)" :style="{ marginLeft: '10px' }">打开文件</Button>

        </FormItem>

        <!-- <Input v-model="argv" placeholder="参数1" allow-clear /> -->
      </p>

    </TabPane>

  </Tabs>

  <div v-if="fileArgvList.filter(item => !item.isDeleted).length > 0"
    style="height: calc(100% - 170px); margin-top: 10px;">
    <PythonEditor v-if="renderEditor" v-model="code"></PythonEditor>
  </div>

</template>


<script setup>
import { nextTick, onMounted, ref } from "vue";
import PythonEditor from '../components/PythonEditor.vue';
import { Notification } from "@arco-design/web-vue";
import { nanoid } from 'nanoid'

const tableName = "ExecPython"
const code = ref()
const showArg = ref(true)
const renderEditor = ref(false)
const activeKey = ref()

const fileArgvList = ref([])

const handleAdd = (uid) => {
  showArg.value = true

  const filtered = getFiltered(uid)
  filtered[0].argv.push({ value: '' })
};

const handleDelete = (uid, index) => {
  showArg.value = true

  const filtered = getFiltered(uid)
  filtered[0].argv.splice(index, 1)
}

onMounted(async () => {
  const res = await window.pywebview.api.listTable(tableName)
  if (!res || res.length == 0) {
    handleTabAdd()
  } else {
    fileArgvList.value = res

    handleTabChange(fileArgvList.value[0]._uid)
  }

})


const execPyFile = async (uid) => {
  const filtered = getFiltered(uid)
  console.log(code.value)

  await window.pywebview.api.writeFile(filtered[0].pyFilePath, code.value)

  await window.pywebview.api.upsertTableByCondition(tableName, filtered[0], '_uid', uid)

  const argvv = filtered[0].argv.map(item => item.value)
  console.log(argvv)
  const res = await window.pywebview.api.execPyFile(filtered[0].pyFilePath, ...argvv)
  if (!res) {
    Notification.error(`${filtered[0].taskName} 代码执行出错`)
    return
  }

  Notification.success(`${filtered[0].taskName} 代码执行成功`)
};


const saveConfig = async (uid) => {
  const filtered = getFiltered(uid)

  await window.pywebview.api.upsertTableByCondition(tableName, filtered[0], '_uid', uid)
  Notification.success(`${filtered[0].taskName} 配置保存成功`)
}

const openPyFile = async (uid) => {
  const pyPath = await window.pywebview.api.openPyFile()
  if (!pyPath) {
    return
  }

  const filtered = getFiltered(uid)
  filtered[0].pyFilePath = pyPath[0]

  handleTabChange(uid)
}

const openFolder = async (uid, index) => {
  const res = await window.pywebview.api.openFolder()
  if (!res) {
    return
  }

  const filtered = getFiltered(uid)
  filtered[0].argv[index].value = res[0]
}


const openFiles = async (uid, index) => {
  const files = await window.pywebview.api.openFiles()
  if (!files) {
    return
  }

  const filtered = getFiltered(uid)
  filtered[0].argv[index].value = files.join(",")
}


const handleTabAdd = async () => {
  const number = fileArgvList.value.length;

  const item = {
    _uid: nanoid(),
    taskName: "任务" + (number + 1),
    argv: [{ value: '' }],
    pyFilePath: null,
  }
  fileArgvList.value = fileArgvList.value.concat(item)

  await window.pywebview.api.insertTable(tableName, item)
};

const handleTabDelete = async (uid) => {
  await window.pywebview.api.removeTableByCondition(tableName, "_uid", uid)

  const res = await window.pywebview.api.listTable(tableName)
  fileArgvList.value = res

  if (fileArgvList.value && fileArgvList.value.length > 0) {
    handleTabChange(fileArgvList.value[0]._uid)
  }
}

const getFiltered = (uid) => {
  return fileArgvList.value.filter(item => item._uid == uid)
}

const handleTabChange = async (uid) => {
  activeKey.value = uid

  reRenderEditor(uid)
}

const reRenderEditor = async (uid) => {
  renderEditor.value = false

  const filtered = getFiltered(uid)
  if (!filtered || filtered.length === 0) {
    return
  }
  if (!filtered[0].pyFilePath) {
    return
  }
  const content = await window.pywebview.api.readContent(filtered[0].pyFilePath)
  console.log(content)
  if (!content) {
    return
  }
  code.value = content
  nextTick(() => {
    renderEditor.value = true
  })
}




</script>


<style scoped>
</style>
