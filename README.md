# 基于matplotlib的散点图动态可视化

之前在学校突发奇想，想搞一个散点图动态可视化，一直记在脑海中，前天终于放假，花了好几个小时，从零开始，把整个项目做起来了。  

大概设想是：将一个班级的所有人的语文成绩与全校排名分别作为横坐标与纵坐标绘制不同颜色的点，左下角标上此人的名字，用一个三次函数进行不同时期数据之间的插值，模拟点的先加速后减速的平滑运动效果，将每一帧绘制成图片，使用ffmpeg将图片序列合成为视频。

效果图如下
![](/img.PNG)
<!-- more -->

## 演示视频
视频地址：https://www.bilibili.com/video/av45763098  
ps:视频中的所有信息包括人名均为用于演示的自动生成

## 开源地址
GitHub：https://github.com/HK-SHAO/Scatter-Visualization
具体如何使用，暂时没时间说明，等更新