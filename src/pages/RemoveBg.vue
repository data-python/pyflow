<template>

  <Alert closable style="margin-top: 10px;">
    <template #title>
      API_KEY需要到
      <Link target="_blank" href="https://www.remove.bg/">www.remove.bg</Link>
      注册生成
    </template>

    <!-- <Image style="margin-top: 10px;" :preview-props="{
      actionsLayout: ['rotateRight', 'zoomIn', 'zoomOut'],
    }" width="100%" src="https://luo0412.oss-cn-hangzhou.aliyuncs.com/1655396504404-JBAJRxJp3rC8.png" />

    <TypographyTitle :heading="6">效果展示如下:</TypographyTitle>

    <Image style="margin-top: 10px;" :preview-props="{
      actionsLayout: ['rotateRight', 'zoomIn', 'zoomOut'],
    }" width="300px" src="https://luo0412.oss-cn-hangzhou.aliyuncs.com/1655396765593-F7yYQKeHWici.png" /> -->

  </Alert>


  <Space direction="vertical" fill style="margin-top: 10px;">

    <Input v-model="apiKey" placeholder="API_KEY" />

    <Button type="outline" :disabled="!apiKey" @click="removeBg">选择图片, 抠除背景</Button>

  </Space>

  <p>
    图片路径:
    <Link target="_blank" :href="picPath">{{ picPath }}</Link>
  </p>
  <p>
    处理后的图片路径:
    <Link target="_blank" :href="outPath">{{ outPath }}</Link>
  </p>













  <!--  <Alert closable type="warning">-->
  <!--    <template #title>-->
  <!--      常见问题-->
  <!--    </template>-->

  <!--    <Link target="_blank" href="https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170">ImportError: Microsoft Visual C++ Redistributable for Visual Studio 2019 not installed on the machine.</Link>-->
  <!--  </Alert>-->

</template>

<script setup>
import { ref, onMounted } from "vue"

const apiKey = ref()
const picPath = ref()
const outPath = ref()

const tableName = "RemoveBg"

onMounted(async () => {
  const res = await window.pywebview.api.getTable(tableName)
  console.log(res)
  if (!res) {
    return
  }
  apiKey.value = res.apiKey
})

const removeBg = async () => {
  const picFilePath = await window.pywebview.api.openPicFile()
  if (!picFilePath) {
    return
  }

  picPath.value = picFilePath[0]

  const res = await window.pywebview.api.removeBg(picFilePath[0], apiKey.value)
  if (!res) {
    return
  }
  outPath.value = picFilePath + '_no_bg.png'

  await window.pywebview.api.upsertTable(tableName, {apiKey: apiKey.value}, 0)
}
</script>