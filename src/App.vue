<template>
  <Layout class="layout-demo">

    <LayoutSider collapsible :collapsed-width="65" :width="280">

      <Row class="logo">
        <Col :span="8">
        <Button type="text">导航定制</Button>
        </Col>
        <Col :span="8">
        <Button type="text" @click="toggleDark">{{ !isDark ? "腹黑模式" : "停止腹黑" }}</Button>
        </Col>
        <Col :span="8">
        <Button type="text" @click="openLink">手动更新</Button>
        </Col>
      </Row>


      <Menu :style="{ width: '100%' }" @menu-item-click="onClickMenuItem">

        <SideItem :menu="menuList" />


      </Menu>

    </LayoutSider>

    <LayoutContent>
      <router-view></router-view>
    </LayoutContent>
  </Layout>

</template>

<script setup>
import { ref } from "vue"
import { useRouter } from 'vue-router';

import SideItem from "./components/SideItem.vue";
// Notification.info({ content: `You select ${key}`, showIcon: true });
import menu from "./menu";
const router = useRouter();

const isDark = ref(false)
const menuList = ref(menu)

const onClickMenuItem = (key) => {
  // Notification.info({ content: `You select ${key}`, showIcon: true });
  router.push(key)
}

const openLink = () => {
  window.open("https://github.com/data-python/pyflow/releases")
}

const toggleDark = () => {
  if (document.body.getAttribute('arco-theme')) {
    isDark.value = false
    document.body.removeAttribute('arco-theme');
  } else {
    isDark.value = true
    document.body.setAttribute('arco-theme', 'dark')
  }
}

</script>


<style>
html,
body {
  height: 100%;
}

#app {
  height: 100%;
  overflow-y: hidden;
}
</style>

<style scoped>
.layout-demo {
  box-sizing: border-box;
  height: 100%;
  background: var(--color-fill-2);
  border: 1px solid var(--color-border);
}

.layout-demo :deep(.arco-layout-sider) {
  /*min-width: 300px;*/
}

.layout-demo :deep(.arco-layout-sider) .logo {
  /* height: 32px; */
  /* line-height: 32px; */
  /* font-weight: bold; */
  margin: 8px;
  /* color: white; */
  background: rgba(255, 255, 255, 0.2);
  text-align: center;
  overflow: hidden;
}

.layout-demo :deep(.arco-layout-sider-light) .logo {
  background: var(--color-fill-2);
}

.layout-demo :deep(.arco-layout-header) {
  height: 64px;
  line-height: 64px;
  background: var(--color-bg-3);
}

.layout-demo :deep(.arco-layout-footer) {
  height: 48px;
  font-weight: 400;
  font-size: 14px;
  line-height: 48px;
}

.layout-demo :deep(.arco-layout-content) {
  padding: 16px;
  color: var(--color-text-2);
  font-weight: 400;
  font-size: 14px;
  background: var(--color-bg-3);
}

.layout-demo :deep(.arco-layout-footer) {}
</style>
