<template>
  <div class="editor" ref="dom"></div>
</template>

<script setup>
// @fix loadForeign 
// https://juejin.cn/post/6933463466111926286
import { onMounted, ref } from 'vue';
import * as monaco from 'monaco-editor';

const props = defineProps({
  modelValue: String,
});

const emit = defineEmits(['update:modelValue']);

const dom = ref();

let instance;

onMounted(() => {
  const pythonModel = monaco.editor.createModel(props.modelValue, 'python');

  instance = monaco.editor.create(dom.value, {
    // readOnly: true,
    model: pythonModel,
    tabSize: 2,
    automaticLayout: true,
    scrollBeyondLastLine: false,
  });

  instance.onDidChangeModelContent(() => {
    const value = instance.getValue();
    emit('update:modelValue', value);
  });
});
</script>

<style scoped>
.editor {
  height: 100%;
}
</style>

