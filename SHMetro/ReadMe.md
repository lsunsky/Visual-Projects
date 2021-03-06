# 上海地铁时间图

要浏览该项目的最新成果，访问：[这里](https://wklchris.github.io/Visual-Projects/SHMetro/SHMetro.html)

本项目在室友 [@方包子](https://github.com/fangyixin)（以下简称方）的支持下完成。同济嘉定出行干货以及上海出行杂烩，推荐一波微信号：@包子曰。

- [项目更新日志](#项目更新日志)
- [项目背景](#项目背景)
  - [起源](#起源)
  - [新篇](#新篇)
  - [篇末语](#篇末语)

## 项目更新日志

- [ ] 绘制站点图
- [ ] 绘制线路
  - [ ] 确定站间线路走向算法
- [ ] 绘制图例内容
  - [ ] 火车站或机场
  - [ ] 罗盘
  - [ ] 水域
  - [ ] 图例说明
- [ ] 交互设计
  - [ ] 悬停显示
    - [x] 站名及线路
    - [ ] 卫生间信息
  - [ ] 单击触发事件

## 项目背景

### 起源

上海官方的地铁图更新速度较慢，时间信息查询也较不方便，数值也不全然准确。为此，在2015年底至2016年初，方与本人（@wklchris）协力绘制了多版 pdf 版本的地铁时间图，用于快速查询站到站之间的用时。当时，主要的出图部分由方以 AutoCAD 出图完成，我负责 PS 时间戳以及一些收尾工作。协力完成的时间图均通过微信号发布。

之后，上海新动工了地铁项目，地铁图需要更新。从v1.4左右的版本开始，我已不再负责相关的工作；不过我的时间戳记模板的仍然使用了一段时间。微信号的此后的出图，一直由方单独负责。我在2016年初帮他写过一个简陋的 C\# 程序（仓库在[这里](https://github.com/wklchris/RouteMapDrawing)），也不知道他有没有在使用。 

### 新篇

2018年初，我得有机会学习了一门数据可视化课程，了解了 D3.js 的强大之处，由此萌生了在 Web 端实现该项目的想法。由方提供 AutoCAD 版本中的坐标数据，由我负责网页端的全部绘制实现，以及交互功能。

### 篇末语

本项目相当于由 Github 托管，相当稳定可靠。一祝友谊长青，次祝项目长存。


*一八年三月廿四日 于加州戴维斯*
