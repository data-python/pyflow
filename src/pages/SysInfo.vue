<template>
  <span>用户名：{{ creator }}</span>

  <p>
     <Button type="outline" @click="getOwner">
      更新本机用户名
    </Button>
  </p>
 

</template>

<script setup>
import {ref, onMounted} from "vue";

let creator = ref("");
const tableName = "SysInfo"

onMounted(async () => {
  const res = await window.pywebview.api.getTable(tableName)
  console.log(res)
  if (!res) {
    return
  }
  creator.value = res.user
})

const init = async (userName) => {
  await window.pywebview.api.upsertTable(tableName, {user: userName}, 0)
}

const getOwner = async () => {
  const res = await window.pywebview.api.getOwner()
  creator.value = res
  init(res)
}

</script>