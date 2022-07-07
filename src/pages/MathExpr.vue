<template>
    <InputNumber :style="{ width: '100px' }" v-model="a"/>
    <Button>+</Button>
    <InputNumber :style="{ width: '100px' }" v-model="b"/>
    <Button type="outline" @click="getSum">=</Button>
    <Input :style="{ width: '100px' }" readonly v-model="result"/>

  <p>

  </p>
</template>

<script setup>
import {ref} from "vue";
import { Notification } from "@arco-design/web-vue";

const a = ref(0.1);
const b = ref(0.2);
const result = ref(null);

const getSum = async () => {
  const res = await window.pywebview.api.getSum(a.value, b.value)
  result.value = res
  // Notification.info("计算结果: " + res);
};

</script>