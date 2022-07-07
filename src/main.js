import { createApp } from 'vue'
import App from './App.vue';
import { createRouter, createWebHashHistory } from "vue-router"

import ArcoVue from '@arco-design/web-vue';
import '@arco-design/web-vue/dist/arco.css';

const pages = import.meta.glob('./pages/*.vue');
const routes = Object.keys(pages).map((path)=>{
    let name = path.match(/\/pages(.*)\.vue$/)[1]
    if (name.substring(name.length - 5) == 'index'){
        name = name.slice(0, -5);
    }

    return {
        name: name.replace("/", ""),
        path: name === '/index' ? '/': name,
        component: pages[path]
    }
})

console.log(routes)
// const routes = [
//     { path: '/', component: () => import('./pages/index.vue') },
//     { name: 'about', path: '/about', component: () => import('./pages/index.vue') },
// ]
routes.push({
    path: '/:pathMatch(.*)*',
    name: 'notFound',
    component: () => import('./pages/404.vue'),
})

const router = createRouter({
    // 4. 内部提供了 history 模式的实现。为了简单起见，我们在这里使用 hash 模式。
    history: createWebHashHistory(),
    routes, // `routes: routes` 的缩写
})


const app = createApp(App);
app.use(router);
app.use(ArcoVue, {
    componentPrefix: ''
});
app.mount('#app');


