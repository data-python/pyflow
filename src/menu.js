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
    children: [
      {
        name: "TranslDeep",
        title: "翻译"
      },
      {
        name: "Dict",
        title: "词典",
      }
    ]
  },

  {
    name: "News",
    title: "[1-3]新闻资讯",
    children: [
      {
        name: "TopHub",
        title: "今日热榜"
      },
      {
        name: "RSSFeed",
        title: "RSS订阅",
      },
      {
        name: "DataIndex",
        title: "数据指数",
      },
    ]
  },

  {
    name: "Design",
    title: "[1-5]设计素材",
    children: [
      {
        name: "IconPick",
        title: "Icon"
      },
      {
        name: "PicDesign",
        title: "图片设计",
        children: [
          {
            name: "PicTiler",
            title: "图片像素化"
          },
          {
            name: "WallPaper",
            title: "壁纸",
          },
          {
            name: "EmojiFight",
            title: "表情包",
          },
        ]
      },

      {
        name: "FontDesign",
        title: "字体设计",
        children: [
          {
            name: "HandWrite",
            title: "模拟手写字体"
          },
        ]
      },

    ]
  },

  {
    name: "EditorExec",
    title: "[1-6]代码执行器",
    children: [
      {
        name: "Editor",
        title: "编辑器",
        children: [
          {
            name: "MdEditor",
            title: "Markdown编辑器",
          },
          {
            name: "JSONEditor",
            title: "JSON编辑器",
          }
        ]
      },
      {
        name: "ExecPython",
        title: "Python执行器",
      },

    ]
  },

  {
    name: "ImproveTools",
    title: "[1-6]效率工具",
    children: [
      {
        name: "TodoList",
        title: "待办清单",
      },
      {
        name: "PinMemo",
        title: "备忘录",
      },
      {
        name: "QrCode",
        title: "二维码",
      },

      {
        name: "ShortUrl",
        title: "短地址",
      },
      {
        name: "Coin",
        title: "汇率换算",
      },
      {
        name: "RandomAvatar",
        title: "随机头像",
      },
      {
        name: "CountStat",
        title: "字数统计",
      },
      {
        name: "TextDiff",
        title: "文本比对",
      },
      {
        name: "Lottery",
        title: "抽奖",
      },
    ]
  },

  {
    name: "Office",
    title: "[1-7]办公文档",
    children: [
      {
        name: "Zip",
        title: "解压缩",
      },
      {
        name: "Batch",
        title: "批量操作",
        children: [
          {
            name: "BatchRename",
            title: "批量重命名",
          },
        ]
      },
      {
        name: "OfficeExcel",
        title: "Excel",
        children: [
          {
            name: "ExcelMerge",
            title: "Excel合并"
          }
        ]
      },
      {
        name: "OfficePdf",
        title: "Pdf",
        children: [
          {
            name: "PdfOutline",
            title: "生成PDF目录大纲"
          }
        ]
      },
      {
        name: "Email",
        title: "邮件",
        children: [
          {
            name: "SendEmail",
            title: "邮件群发"
          }
        ]
      },

      {
        name: "Markdown",
        title: "Markdown",
        children: [
          {
            name: "MdSlidev",
            title: "MD生成PPT",
          },
          {
            name: "MdCoolma",
            title: "MD显示增强",
          }
        ]
      }

    ]
  }, 


]        