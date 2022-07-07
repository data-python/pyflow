<template>


  <Row :gutter="10">
    <Col :span="12">
    <Card title="阿里云图床配置">
   
        <Input placeholder="region" v-model.trim="region" />

      <p>
        <InputPassword placeholder="accessKeyId" v-model.trim="accessKeyId" />
      </p>
      <p>
        <InputPassword placeholder="accessKeySecret" v-model.trim="accessKeySecret" />
      </p>
      <p>
        <Input placeholder="bucket" v-model.trim="bucket" />
      </p>

      <Upload :disabled="!region || !accessKeyId || !accessKeySecret || !bucket" @change="onChange" draggable
        :show-file-list="false" :auto-upload="false" />

    </Card>

    </Col>

    <Col :span="12">
    <List>
      <template #header>今日上传记录
      </template>
      <ListItem v-for="item in list">
        <Link target="_blank" :href="item.url">{{ item.name }}</Link>
      </ListItem>
    </List>
    </Col>
  </Row>


</template>

<script setup>
import OSS from "ali-oss"
import { ref, onMounted } from "vue"
import moment from "moment"

const tableName = "AliyunOss"

const uploadRef = ref();
const files = ref([]);

const list = ref([])

const region = ref()
const accessKeyId = ref()
const accessKeySecret = ref()
const bucket = ref()

onMounted(async() => {
  const res = await window.pywebview.api.getTable(tableName)
  console.log(res)
  if (res) {
    region.value = res.region
    accessKeyId.value = res.accessKeyId
    accessKeySecret.value = res.accessKeySecret
    bucket.value = res.bucket
  }

  listLatest()
})

const onChange = (fileList) => {
  // console.log(fileList)
  files.value = fileList;
  handleUpload(fileList[fileList.length - 1])
};

const initClient = () => {
  const config = {
    region: region.value,
    accessKeyId: accessKeyId.value,
    accessKeySecret: accessKeySecret.value,
    bucket: bucket.value
  }

  return new OSS({
    ...config,
    secure: true,
  });
}

const randomStr = (len) => {
  len = len || 32;

  // 默认去掉了容易混淆的字符oOLl,9gq,Vv,Uu,I1
  const $chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678';
  const maxPos = $chars.length;
  let pwd = '';
  for (let i = 0; i < len; i++) {
    pwd += $chars.charAt(Math.floor(Math.random() * maxPos));
  }
  return pwd;
}

const isOk = () => {
  return region.value && accessKeyId.value  && accessKeySecret.value && bucket.value
}

const handleUpload = async (file) => {
  // console.log(file)

  if (!isOk()) {
    return false
  }

  const client = initClient()
  if (!client) {
    return
  }
  await client.multipartUpload(moment(new Date()).format("YYYYMMDD-HHmmss") + "-" + randomStr(12) + "-" + file.name, file.file)
  
  const config = {
    region: region.value,
    accessKeyId: accessKeyId.value,
    accessKeySecret: accessKeySecret.value,
    bucket: bucket.value
  }
  await window.pywebview.api.upsertTable(tableName, config, 0)

  listLatest()
}

const listLatest = async () => {
  if (!isOk()) {
    return false
  }

  const client = initClient()
  if (!client) {
    return
  }
  const res = await client.list({
    // 'max-keys': limit,
    'prefix': moment(new Date()).format("YYYYMMDD-")
  })

  list.value = res.objects.reverse()
}



</script>