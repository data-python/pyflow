# README

![](https://luo0412.oss-cn-hangzhou.aliyuncs.com/1655816632094-ar3Y7TQpWfyb-image.png)

![](https://luo0412.oss-cn-hangzhou.aliyuncs.com/1655554208030-tmEMTBPnJxPa-image.png)

![](https://luo0412.oss-cn-hangzhou.aliyuncs.com/1655739959000-YkeRskXaafmy-image.png)

---

# 技术选型 @stack

- pywebview + pyinstaller
  - https://pywebview.flowrl.com/guide/
  - https://github.com/cztomczak/cefpython

```
pywebview -- JavaScript的界面+Python的脚本, 同时薅两个生态的羊毛
```

- vue3 + vite + arco-design-vue
  - https://arco.design/vue/docs/start

```
arco -- 设计风格沉稳中又带着些许风骚
```

- tinydb
  - https://tinydb.readthedocs.io/en/latest/usage.html

```
tinydb -- 本地json数据的增删改查(但它不抗揍)

===
// 后期考虑改成
lowdb
sqlite
```

# 本地启动 @run

```bash
npm run init
# npm run initfix # paramiko等安装失败时可单独安装

npm run init:cef # 或者兼容模式初始化
# npm run initfix:cef # paramiko等安装失败时可单独安装

npm run dev # 启动前端

npm run start # 启动客户端
npm run start:cef # 或者兼容模式启动客户端
```

# 软件打包 @build

```bash
npm run build
npm run build:cef # 或者兼容模式打包
```

# 运行环境 @env

正常打包运行需要先下载[EdgeWebView2Runtime](https://developer.microsoft.com/en-us/microsoft-edge/webview2/)环境, 这比兼容模式下打包的体积要少60M

但如果懒得安装环境, 也可以直接用CEF兼容模式的安装包, 不过在功能和样式上有很多的小bug要兼容处理...

---

# 参考 @ref

- https://github.com/pangao1990/vue-pywebview-pyinstaller
