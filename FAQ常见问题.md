# FAQ常见问题

# 待解决

- cef兼容模式下打包,monaco-editor报错 -- ReferenceError: queueMicrotask is not defined @tofix
  - https://apidocs.cn/blog/front/nodejs/queueMicrotaskIsNotDefined.html

![](https://luo0412.oss-cn-hangzhou.aliyuncs.com/1655412225995-MZ4iFANKsaNb.png)

- Python脚本同时运行多个上传任务的时候报错 @tofix

# 已解决

- pip安装paramiko失败 -- Could not build wheels for pycuda which use PEP 517 and cannot be installed directly @fix
  - https://visualstudio.microsoft.com/downloads/
  - https://blog.csdn.net/weixin_43400774/article/details/124042243

```
主要原因是pip(pyenv)版本问题 可以升级版本或指定路径单独安装

python -m pip install -U --force-reinstall pip

pip install paramiko --target=./pyenv/pyenv/Lib/site-packages
# pip install paramiko --target=./pyenv/pyenvCEF/Lib/site-packages

===
// 其他
cryptography
rust环境
Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools"
```

---

# 参考 @ref