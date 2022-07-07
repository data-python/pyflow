<template>

  <Alert>
   编码设为gbk, 支持中文
  </Alert>

  <p style="margin-top: 10px;">
  <Button type="outline" @click="removeBg">选择JSON, 转换成CSV</Button>
  </p>

  <p>
    JSON路径: <Link target="_blank" :href="jsonPath">{{ jsonPath }}</Link>
  </p>
  <p>
    CSV路径: <Link target="_blank" :href="outPath">{{ outPath }}</Link>
  </p>


</template>

<script setup>
import {ref} from "vue"

const jsonPath = ref(null)
const outPath = ref(null)

const removeBg = async () => {
  const jsonFilePath = await window.pywebview.api.openJsonFile()
  if (!jsonFilePath) {
    return
  }
  jsonPath.value = jsonFilePath[0]

  const res = await window.pywebview.api.json2csv(jsonPath.value)
  if (!res) {
    return
  }
  outPath.value = res
}
</script>