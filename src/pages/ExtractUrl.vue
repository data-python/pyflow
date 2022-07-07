<template>

  <p>
    <Input v-model="link" placeholder="输入网址" allow-clear />
  </p>

  <p style="margin: 10px 0">
    <Button type="outline" :disabled="!link" @click="extractUrl">提取网页链接</Button>
  </p>

  <p v-for="url in urls">
    <Link :key="url" target="_blank" :href="url">{{ url }}</Link>
  </p>

</template>

<script setup>
import {ref} from "vue"

const link = ref("https://www.runoob.com/python/python-break-statement.html")
const urls = ref([])

const extractUrl = async () => {
  console.log(link.value)
  const urlsRes = await window.pywebview.api.extractUrl(link.value)
  if (!urlsRes) {
    return
  }
  urls.value = urlsRes
}
</script>