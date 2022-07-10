<template>
    <div v-for="menuItem in menu">
        <SubMenu
            v-if="menuItem.isOk != false && menuItem.children && menuItem.children.length > 0 && menuItem.children.some(i => i.isOk != false)"
            :key="menuItem.name">
            <template #title v-slot="{menuItem}">
                <IconCalendar></IconCalendar> {{ menuItem.title }}
            </template>

            <SideItem :menu="menuItem.children" />
        </SubMenu>
        <MenuItem v-else-if="menuItem.isOk != false && !menuItem.children" :key="menuItem.name">{{ menuItem.title }}
        </MenuItem>
    </div>
</template>

<script setup>
import {
//   IconHome,
  IconCalendar,
//   IconCheckCircle,
} from '@arco-design/web-vue/es/icon';
</script>

<script>
export default {
    name: 'SideItem',
    props: {
        menu: Array
    }
}
</script>