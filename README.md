Waterfall
=========

Waterfall是一个开源的水印系统框架，为了水印嵌入、提取、检测、攻击提供统一的接口。


Purposes
--------

1. 为用户提供易用的接口来进行水印的相关操作，提供API、CLI等。
2. 为水印算法开发者提供统一的算法开发框架。


Structures
----------

* Cover: 抽象概念，指被嵌入水印的载体，可能含有水印，也可能没有，分为如下两类：
  - Discrete Cover: Cover中存储的为离散量，常见的Discrete Cover包括位图、采样后的声波等。
  - Continuous Cover[^1]: Cover中存储的为连续量，常见的Continuous Cover包括矢量图、模拟信号等。

* Watermark: 被嵌入到载体中的内容，为一串byte，可以是字符串，也可以是其他数据经过编码得到。

* Secret Space: 对于不可见水印而言，水印是不希望被Cover的传播者和使用者观测到的，基于这一点，我们通常会采用
     一些可逆变换把Cover转换到一个特定的线性空间中进行水印的嵌入，之后再通过逆变换还原Cover。
     从数据结构的角度来看，Secret Space有以下两个特点：
  - secret space与空域是两个相互同构的线性空间
  - secret space应该易于嵌入watermark，表现为向量或矩阵
  - secret space应该有一个对应的revert函数用于还原Cover


Functions
---------

从编程角度来看，水印的嵌入包括如下步骤：

* Read: 从媒体文件中读取Cover数据。

* Transform：将Cover进行变换，转化到Secret Space。

* Encode: 对水印数据进行编码及加密，以便进行水印的嵌入。

* Embed：将Watermark嵌入到Secret Space中。

* Revert: 对Secret Space调用该函数得到Cover数据。

* Write: 将嵌入后的Cover写入到媒体文件中。

水印的提取包括如下步骤：

* Read: 从媒体文件中读取Cover数据。

* Transform: 将Cover进行变换，转化到Secret Space。

* Extract: 从Secret Space中提取Watermark。

* Decode: 对水印数据进行解码和解密，得到所嵌入的水印。

水印的检测包括如下步骤：

* Read: 从媒体文件中读取Cover数据。

* Detect: 对Cover进行统计分析，判断是否存在水印。

* Try: 遍历常见的水印算法，判断是否存在水印。

水印的攻击一般来针对不同的Cover类型有不同的攻击策略，该框架暂时不包括水印攻击的过程，但是未来会有。

可以发现，在水印的嵌入、提取、检测中，重复出现了如下步骤：

* Read与Write

* Transform与对应的Revert

* Embed与对应的Extract

* Encode与对应的Decode

本框架的意义在于，实现通用的Read与Write、Transform与Revert、Encode与Decode，实现常见的Embed与Extract，
让水印算法开发者能专注于新的Embed与Extract的开发，方便算法开发者进行算法效率、效果的比较。


[^1]: 当前的框架中不包含对Continuous Cover的支持，对于Continuous Conver可以转化为Discrete Cover进行处理。
