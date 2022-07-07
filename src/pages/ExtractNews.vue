<template>

  <Card>
    <Link target="_blank" href="https://github.com/GeneralNewsExtractor/GeneralNewsExtractor">GeneralNewsExtractor
    </Link>

    <Link target="_blank" href="https://github.com/chrislinan/cx-extractor-python">cx-extractor-python</Link>

    <Link target="_blank" href="https://github.com/codelucas/newspaper">newspaper</Link>

  </Card>



    <Tabs style="margin-top: 10px;" :active-key="type" postion="top" animation @change="handleChange">
      <TabPane key="html" title="HTML文本">
        <Textarea placeholder="HTML文本" auto-size v-model="html" allow-clear />
      </TabPane>
      <TabPane key="url" title="链接">
        <Input placeholder="链接" auto-size v-model="url" allow-clear />
      </TabPane>
    </Tabs>

    <Button type="outline" style="margin-top: 10px;" :loading="loading" :disabled="!url"
      @click="extract">提取标题和正文</Button>

    <Row :gutter="10" v-show="title" style="margin-top: 10px;">
      <Textarea placeholder="标题" auto-size v-model="title" readonly />
      <Textarea placeholder="正文" auto-size v-model="content" readonly />
    </Row>


</template>

<script setup>
import { ref } from "vue"

const loading = ref(false)

const url = ref("https://hise.hznu.edu.cn/c/2022-04-20/2696928.shtml")
const html = ref(`<html>
<body></body>
</html>`)
const type = ref('html')

const title = ref()
const content = ref()

const extract = async () => {
  let res = ''
  if (type.value === "url") {
    res = await window.pywebview.api.extractNews(url.value)
  } else {
    res = await window.pywebview.api.extractHTML(html.value)
  }

  if (!res) {
    return
  }
  // console.log(res)
  title.value = res.title
  content.value = res.content
}

const handleChange = (key) => {
  type.value = key
}
</script>