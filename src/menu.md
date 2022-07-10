```js

 


        <SubMenu key="News">
          <template #title>
            <IconCalendar></IconCalendar> [1-3]新闻资讯
          </template>
          <MenuItem key="TopHub">今日热榜
          <IconCheckCircle />
          </MenuItem>
          <MenuItem key="RSSFeed">RSS订阅
          <IconCheckCircle />
          </MenuItem>
          <MenuItem key="DataIndex">数据指数
          <IconCheckCircle />
          </MenuItem>
        </SubMenu>
        <SubMenu key="Design">
          <template #title>
            <IconCalendar></IconCalendar> [1-5]设计素材
          </template>
          <MenuItem key="IconPick">Icon
          <IconCheckCircle />
          </MenuItem>
          <SubMenu key="PicDesign" title="图片">
            <MenuItem key="PicTiler">图片像素化
            <IconCheckCircle />
            </MenuItem>
            <MenuItem key="WallPaper">壁纸</MenuItem>
            <MenuItem key="EmojiFight">表情包</MenuItem>
          </SubMenu>
          <SubMenu key="FontDesign" title="字体">
            <MenuItem key="HandWrite">模拟手写字体
            <IconCheckCircle />
            </MenuItem>
          </SubMenu>
        </SubMenu>
        <SubMenu key="EditorExec">
          <template #title>
            <IconCalendar></IconCalendar> [1-6]代码执行器
          </template>
          <SubMenu key="Editor" title="编辑器">
            <MenuItem key="MdEditor">Markdown编辑器
            <IconCheckCircle />
            </MenuItem>
            <MenuItem key="JSONEditor">JSON编辑器
            <IconCheckCircle />
            </MenuItem>
          </SubMenu>
          <MenuItem key="ExecPython">Python执行器
          <IconCheckCircle />
          </MenuItem>
        </SubMenu>
        <SubMenu key="Improve">
          <template #title>
            <IconCalendar></IconCalendar> [1-6]效率工具
          </template>
          <MenuItem key="TodoList">待办清单</MenuItem>
          <MenuItem key="PinMemo">备忘录</MenuItem>
          <MenuItem key="QrCode">二维码
          <IconCheckCircle />
          </MenuItem>
          <MenuItem key="ShortUrl">短地址</MenuItem>
          <MenuItem key="Coin">汇率换算</MenuItem>
          <MenuItem key="RandomAvatar">随机头像</MenuItem>
          <MenuItem key="CountStat">字数统计</MenuItem>
          <MenuItem key="TextDiff">文本比对</MenuItem>
          <MenuItem key="Lottery">抽奖</MenuItem>
        </SubMenu>
        <SubMenu key="Office">
          <template #title>
            <IconCalendar></IconCalendar> [1-7]办公文档
          </template>
          <MenuItem key="Zip">解压缩</MenuItem>
          <SubMenu key="Batch" title="批量操作">
            <MenuItem key="RenameBatch">批量重命名</MenuItem>
          </SubMenu>
          <SubMenu key="OfficeExcel" title="Excel">
            <MenuItem key="ExcelMerge">Excel合并</MenuItem>
          </SubMenu>
          <SubMenu key="OfficePdf" title="PDF">
            <MenuItem key="PdfOutline">生成PDF目录大纲
            <IconCheckCircle />
            </MenuItem>
          </SubMenu>
          <SubMenu key="Email" title="邮件">
            <MenuItem key="SendEmail">邮件群发</MenuItem>
          </SubMenu>
          <SubMenu key="Markdown" title="Markdown">
            <MenuItem key="MdSlidev">MD生成PPT(slidev)</MenuItem>
            <MenuItem key="MdCoolma">MD显示增强(coolma)
            <IconCheckCircle />
            </MenuItem>
          </SubMenu>
        </SubMenu>
        <SubMenu key="Media">
          <template #title>
            <IconCalendar></IconCalendar> [1-7]多媒体
          </template>
          <SubMenu key="MediaPic" title="图片">
            <MenuItem key="PicMin">图片压缩
            <IconCheckCircle />
            </MenuItem>
            <MenuItem key="RemoveBg">抠除背景
            <IconCheckCircle />
            </MenuItem>
            <MenuItem key="PicStitch">图片拼接</MenuItem>
            <MenuItem key="PicWatermark">图片加水印</MenuItem>
          </SubMenu>
          <SubMenu key="MediaVideo" title="视频">
            <MenuItem key="VideoEdit">视频剪辑
            <IconCheckCircle />
            </MenuItem>
          </SubMenu>
        </SubMenu>
        <SubMenu key="Convert">
          <template #title>
            <IconCalendar></IconCalendar> [1-7]格式转换
          </template>
          <SubMenu key="ConvertJSON" title="JSON">
            <MenuItem key="JSON2CSV">JSON转CSV
            <IconCheckCircle />
            </MenuItem>
          </SubMenu>
          <SubMenu key="ConvertExcel" title="Excel">
            <MenuItem key="Excel2JSON">Excel转JSON</MenuItem>
          </SubMenu>
          <SubMenu key="ConvertTXT" title="TXT">
            <MenuItem key="Txt2Word">TXT转Word</MenuItem>
          </SubMenu>
          <SubMenu key="ConvertPDF" title="PDF">
            <MenuItem key="Pdf2Pic">PDF转图片</MenuItem>
            <MenuItem key="Pdf2Word">PDF转Word</MenuItem>
          </SubMenu>
        </SubMenu>
        <SubMenu key="Devops">
          <template #title>
            <IconCalendar></IconCalendar> [3-5]开发助手
          </template>
          <MenuItem key="Postman">简易版Postman</MenuItem>
        </SubMenu>
        <SubMenu key="Cloud">
          <template #title>
            <IconCalendar></IconCalendar> [3-6]云服务
          </template>
          <MenuItem key="AliyunOss">阿里云OSS图床
          <IconCheckCircle />
          </MenuItem>
        </SubMenu>
        <MenuItem key="MathExpr">
        <IconCalendar></IconCalendar>
        [5-1]数学运算
        <IconCheckCircle />
        </MenuItem>
        <SubMenu key="DataV">
          <template #title>
            <IconCalendar></IconCalendar> [4-7]数据可视化
          </template>
          <MenuItem key="PosterGithub">Github日历海报
          <IconCheckCircle />
          </MenuItem>
          <MenuItem key="CityTraffic">城市交通脉络
          <IconCheckCircle />
          </MenuItem>
        </SubMenu>
        <SubMenu key="Spider">
          <template #title>
            <IconCalendar></IconCalendar> [5-4]网络爬虫
          </template>
          <SubMenu key="ContentExtract" title="内容提取">
            <MenuItem key="ExtractUrl">网址提取
            <IconCheckCircle />
            </MenuItem>
            <MenuItem key="ExtractNews">新闻正文提取
            <IconCheckCircle />
            </MenuItem>
            <MenuItem key="ArchiveBox">网页归档
            <IconCheckCircle />
            </MenuItem>
          </SubMenu>
          <SubMenu key="TxtWebsite" title="图文网站">
            <MenuItem key="SpiderWeibo">微博
            <IconCheckCircle />
            </MenuItem>
            <MenuItem key="SpiderZhihu">知乎</MenuItem>
            <MenuItem key="SpiderDouban">豆瓣</MenuItem>
            <MenuItem key="SpiderJuejin">掘金</MenuItem>
          </SubMenu>
          <SubMenu key="VidWebsite" title="视频网站">
            <MenuItem key="DownloadBiliBili">哔哩哔哩
            <IconCheckCircle />
            </MenuItem>
          </SubMenu>
        </SubMenu>
        <SubMenu key="Analysis">
          <template #title>
            <IconCalendar></IconCalendar> [5-4]数据分析
          </template>
          <SubMenu key="AnalysisNumpy" title="Numpy脚本">
            <MenuItem key="NumpyModel">Numpy简单示例</MenuItem>
          </SubMenu>
          <SubMenu key="AnalysisScipy" title="Scipy脚本">
            <MenuItem key="ScipyModel">Scipy简单示例</MenuItem>
          </SubMenu>
        </SubMenu>
        <SubMenu key="SRE">
          <template #title>
            <IconCalendar></IconCalendar> [5-5]自动化脚本
          </template>
          <MenuItem key="DeployFe">前端SSH部署
          <IconCheckCircle />
          </MenuItem>
          <MenuItem key="RPACmd">自动化操作
          <IconCheckCircle />
          </MenuItem>
          <SubMenu key="CornTask" title="定时任务">
            <MenuItem key="DBBackup">数据库定时备份</MenuItem>
          </SubMenu>
        </SubMenu>
        <SubMenu key="AI">
          <template #title>
            <IconCalendar></IconCalendar> [5-6]智能助手
          </template>
          <MenuItem key="OCR">OCR</MenuItem>
          <SubMenu key="NLP" title="NLP">
            <MenuItem key="NlpJieba">结巴分词器
            <IconCheckCircle />
            </MenuItem>
            <MenuItem key="TextFilter">敏感词
            <IconCheckCircle />
            </MenuItem>
          </SubMenu>
        </SubMenu>
        <SubMenu key="MiniGame">
          <template #title>
            <IconCalendar></IconCalendar> [6-5]小游戏
          </template>
          <MenuItem key="GameNav">小游戏导航
          <IconCheckCircle />
          </MenuItem>
          <SubMenu key="PzlGame" title="益智游戏">
            <MenuItem key="Snake">贪吃蛇</MenuItem>
          </SubMenu>
        </SubMenu>
        <SubMenu key="Estate">
          <template #title>
            <IconCalendar></IconCalendar> [7-7Estate]房产建筑
          </template>
          <MenuItem key="EstatePrice">房价查询
          <IconCheckCircle />
          </MenuItem>
        </SubMenu>
        <SubMenu key="Local">
          <template #title>
            <IconCalendar></IconCalendar> [7-7Local]本地生活
          </template>
          <MenuItem key="LocalLife">医疗科普
          <IconCheckCircle />
          </MenuItem>
        </SubMenu>

        <SubMenu key="Fin">
          <template #title>
            <IconCalendar></IconCalendar> [7-7Fin]经济金融
          </template>
          <MenuItem key="CoinNav">数字货币
          <IconCheckCircle />
          </MenuItem>
          <MenuItem key="QuanTrade">量化交易
          <IconCheckCircle />
          </MenuItem>
          <MenuItem key="StockWave">基金涨跌</MenuItem>
        </SubMenu>
        <SubMenu key="Edu">
          <template #title>
            <IconCalendar></IconCalendar> [7-7Edu]教育培训
          </template>
          <MenuItem key="Survey">问卷调查</MenuItem>
        </SubMenu>
        <SubMenu key="Music">
          <template #title>
            <IconCalendar></IconCalendar> [8-4]音乐
          </template>
          <MenuItem key="MusicNoice">白噪音
          <IconCheckCircle />
          </MenuItem>
          <MenuItem key="PlaylistSync">歌单同步
          <IconCheckCircle />
          </MenuItem>
        </SubMenu>
```
