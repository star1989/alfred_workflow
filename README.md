# 金山翻译&时间的workflow

## 项目链接
[https://github.com/star1989/star_workflow](https://github.com/star1989/star_workflow)

## 金山翻译
### **功能:**
* 中英文翻译
* 音标
* 发音(***默认美式***)
* 复制(当前选中行文本,内容分为:音标,释意几行展示,可以自由复制)
    * 注:复制的同时都会有读音
    * 复制示例:`am:[stɑr] ,en:[stɑ:(r)]`
* 添加单词HOOK

### 按键
*dc*
> 对应中文的单词,而且也离左手近,比较方便(主要是懒)

### 效果
* 英文翻译
![英文翻译截图](http://bimg.cxstars.com/2017-01-20-14848765913701.jpg)

* 中文翻译
![中文翻译截图](http://bimg.cxstars.com/2017-01-21-14850042653066.jpg)

* 添加单词HOOK
![添加单词HOOK图](http://bimg.cxstars.com/2017-01-25-14853523310481.jpg)

* 添加单词通知
![添加单词通知](http://bimg.cxstars.com/2017-01-25-14853524781043.jpg)

### 金山API
项目里我已经放上我自己的API KEY,方便跟我一样懒的道友们.
不过也建议大家自行申请,非常方便.[金山词霸API](http://open.iciba.com/?c=api)
修改文件`jsfy.py`:
`app_key = "put your api key"`

## time

### 显示时间相关的信息:日期,时间,周几,今天是一年中的多少天,本周是一年中的多少周

### 按键
*now*
> 为了节约mac上状态的位置,而且可以通过workflow快速的复制当天的时间信息,方便我懒得输TODO里的日期之类的.同时也提醒自己时间飞快,惜时务事.

### 效果
![now截图](http://bimg.cxstars.com/2017-02-01-屏幕快照 2017-02-01 20.57.39.png)

## 参考资料
* [Alfred-Workflow Python](http://www.deanishe.net/alfred-workflow/)
* [Alfred office help](https://www.alfredapp.com/help/workflows/)

## ToDoList
* 金山翻译
    * ~~添加单词到单词本(v1.3:2017-01-25)~~
    * ~~中翻英(v1.1:2017-01-21)~~
    * ~~单词顺序列表/当天应记单词列表API(2017-02-01)~~
    * 安卓单词APP
    * 每日一句
* time
    * 历史上的今天


