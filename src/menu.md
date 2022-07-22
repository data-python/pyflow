```js
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
