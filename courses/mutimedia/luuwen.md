2.1条。心电二值图像提取的分层算法

彩色图像通常包含三个通道：R（红色），

G（绿色），B（蓝色）。可以描述每个通道下的图像

分别作为矩阵R（m，n），G（m，n）和B（m，n）。m和n表示矩阵的行数和列数。像素

每个通道的矩阵值在0~255之间。

由于不同的图像通道有各自的特点

像素值的梯度和分布是完全不同的。

通过三均值聚类将像素值分为三个层次

[23]在每个通道。图1（a）中显示了这三个级别。它

可见光照效应在R

通道和网格线主要出现在G、B通道中。灵感来自

这些观测值，提出了一种心电二值图像的分层算法

在R、G、B上实现了由两层组成的提取。图1（B）和一个示例描述了整个框架

如图1（a）所示。

2.1.1条。第一层：子信道滤波

第一层在G、B通道上实现，用于网格过滤。由于电网本身拥有相对较高的频率，它们

在G、B通道的频域内可以很好地去除。

在G、B通道的频域中采用二维傅里叶变换和巴特沃斯滤波器去除网格，

然后通过傅里叶逆变换将两个通道转换回空间do  main。最后，将这两个处理过的通道叠加在原始的R通道上（该通道保持不变），得到输出的3通道图像I’。整齐

提取心电信号波形，采用图像二值化方法

Otsu等人[17]应用于I 。对上述程序进行了总结

作为：

I =二进制  R，G ，B 

（1）

I ：第一层的输出，即叠加通道。

R： 原始图像的R通道信号。

G ，B ：经巴特沃斯处理后的G ，B ：G和B通道信号

频域滤波。

第一层的输出如上图所示

以及图1（a）中的第三列。可以观察到

大约三分之二的网格线被删除。不过，在那里

仍然有一些网格线尚未删除，因为

照明效果不均匀。第二层进一步介绍

去解决它。

2.1.2条。第二层自适应滤波器

第二层针对R通道进行自适应滤波算法（AFA），以消除干扰的影响。具体地说，首先将R通道R（m，n）的矩阵按步长分为多个不重叠的图像块

图像高度的十分之一。下一步是自适应地确定某个块是否包含信号。这个

可以通过计算每个块的方差来确定

指示块的分散程度。在包含ECG信号的块中，方差往往比背景块更大（更分散）。通过定义所有块变量的平均值作为阈值，所有这些块因此被分类-

分成两类。方差比

threshold实际上是包含信号的类。这种

块由Ostu算法进一步处理[24]。另一个呢

类，我们将它们设置为0作为背景。最后，这些块被重新组合成一个完整的二值图像。总结了算法

在算法1中，如图2所示。

与全局阈值法相比，本文提出的自适应滤波算法有效地应用于局部块单元

通过测量考虑图像的局部特性

使用方差的离散度（在我们的实验中被证明是no信号之间固有的差异之一

块和信号块），从而成功地提取了心电轨迹。

随后的Ostu算法生成一个二值图像，作为下一阶段QRS识别器的理想输入图像。