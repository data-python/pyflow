<template>


  <Button type="outline" @click="openPdfFile">选择PDF</Button>

  <p v-show="pdfPath">
    pdf路径:
    <Link target="_blank" :href="pdfPath">{{ pdfPath }}</Link>
  </p>

  <p v-show="outlinePath">
    大纲生成路径:
    <Link target="_blank" :href="outlinePath">{{ outlinePath }}</Link>
  </p>



</template>

<script setup>
import {ref} from "vue";

const pyFilePath = ref(null)
const pdfPath = ref(null)
const outlinePath = ref(null)

import { Notification } from "@arco-design/web-vue";

const openPdfFile = async () => {
  const pdfFilePath = await window.pywebview.api.openPdfFile()
  if (!pdfFilePath) {
    return
  }

  pdfPath.value = pdfFilePath[0]

  const outlinesFilePath = await window.pywebview.api.genPdfOutlines(pdfFilePath[0])
  outlinePath.value = outlinesFilePath
  // Notification.success({content: "已生成pdf大纲 " + outlinesPath})
  // window.open(outlinesPath)
};







</script>