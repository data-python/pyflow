<template>

  <Card>
    <Space>
      <Link target="_blank" href="https://github.com/Gsllchb/Handright">Handright</Link>
    </Space>
  </Card>

  <Row :gutter="10" style="margin-top: 10px;">
    <Col flex="auto">
    <Input placeholder="文本" v-model="text" allow-clear />
    </Col>
  </Row>

  <Row :gutter="10" style="margin-top: 10px;">
    <Col flex="auto">
    <Input placeholder="字体文件路径" v-model.trim="fontPath" allow-clear />
    </Col>
    <Col flex="170px">
    <Space>
      <Link target="_blank" href="https://github.com/Gsllchb/Handright/tree/master/tests/fonts">下载地址</Link>
      <Button type="outline" @click="openFontFile">选择字体</Button>
    </Space>
    </Col>
  </Row>

  <Row :gutter="10" style="margin-top: 10px;">
    <Col flex="auto">
    <Input placeholder="图片输出目录(默认为桌面路径)" v-model.trim="outPath" allow-clear />
    </Col>
    <Col flex="120px">
    <Button type="outline" @click="openFolder">选择输出文件夹</Button>
    </Col>
  </Row>

  <Row :gutter="10" v-show="imgPath" style="margin-top: 10px;">
    <Col flex="auto">
    图片输出路径:
    <Link target="_blank" :href="imgPath">{{ imgPath }}</Link>
    </Col>
  </Row>

  <Button type="outline" style="margin-top: 10px;" :loading="loading" :disabled="!text || !fontPath"
    @click="genenrate">生成</Button>




</template>

<script setup>
import { ref, onMounted } from "vue"

const tableName = "HandWrite"
const loading = ref(false)

const text = ref()
const fontPath = ref()
const outPath = ref('')
const imgPath = ref()

onMounted(async () => {
  const res = await window.pywebview.api.getTable(tableName)
  if (res) {
    text.value = res.text
    fontPath.value = res.fontPath
    outPath.value = res.outPath
  }
})


const openFontFile = async () => {
  const res = await window.pywebview.api.openFontFile()
  if (!res) {
    return
  }
  fontPath.value = res[0]
}

const openFolder = async () => {
  const res = await window.pywebview.api.openFolder()
  if (!res) {
    return
  }
  outPath.value = res[0]
}

const genenrate = async () => {
  const res = await window.pywebview.api.handwrite(text.value, fontPath.value, outPath.value)
  if (!res) {
    return
  }
  imgPath.value = res

  await window.pywebview.api.upsertTable(tableName, {
    text: text.value,
    fontPath: fontPath.value,
    outPath: outPath.value
  }, 0)
}

</script>