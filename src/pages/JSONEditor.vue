<template>

<div style="height: calc(100% - 20px); margin-top: 10px;">
  <JSONEditor v-model="code"></JSONEditor>
</div>

</template>


<script setup>
import {ref} from "vue"
import JSONEditor from '../components/JSONEditor.vue';
const code = ref(`{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$ref": "#/definitions/mySchema",
  "definitions": {
    "mySchema": {
      "type": "object",
      "properties": {
        "myString": {
          "type": "string",
          "minLength": 5
        },
        "myUnion": {
          "type": ["number", "boolean"]
        }
      },
      "additionalProperties": false,
      "required": ["myString", "myUnion"]
    }
  }
}`)
</script>


<style scoped>

</style>
