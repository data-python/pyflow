export default [
  {
    name: 'SysInfo',
    title: '[0-5]系统信息',
    // show: false,
  },
  {
    name: "SQL",
    title: "[0-6]SQL查询",
    children: [
      {
        name: "CSVQuery",
        title: "SQL形式查询CSV"
      }
    ]
  },
  {
    name: "Network",
    title: "[0-8]网络传输",
    children: [
      {
        name: "FileShare",
        title: "文件分享",
        isOk: false,
      }
    ]
  },
  {
    name: "Security",
    title: "[0-9]信息安全",
    children: [
      {
        name: "Decode",
        title: "编解码",
        isOk: false,
      },
      {
        name: "FileCrypt",
        title: "文件加解密",
      },
      {
        name: "BlindWatermark",
        title: "图片盲水印"
      },
      {
        name: "GithubMonitor",
        title: "Github密码泄露监控"
      }
    ]
  },
  {
    name: "Translate",
    title: "[1-2]语言翻译",
    children: [{
      name: "TranslDeep",
      title: "翻译"
    },
    {
      name: "Dict",
      title: "词典",
    }
    ]
  }

]        