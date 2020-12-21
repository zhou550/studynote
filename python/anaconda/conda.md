# miniconda安装

为什么不直接使用Anaconda?
直接安装Anaconda 意味着您将安装超过一百个包，并涉及下载几百兆字节的安装程序。如果您只想要安装你需要的包，或者具有有限的互联网带宽，那么miniconda则为又一选择，[Miniconda ](http://conda.pydata.org/miniconda.html)允许您创建最小的Python安装包，然后使用[Conda ](http://conda.pydata.org/docs/)命令安装其他软件包，miniconda省去了普通anaconda的图形化界面等其他初始化包和自带软件。
缺点：
需要用户熟悉conda命令下载：

下载地址：https://docs.conda.io/en/latest/miniconda.html

![下载界面](https://img-blog.csdnimg.cn/20200224035413314.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0dob3N0R3Vlc3Q=,size_16,color_FFFFFF,t_70)

1. ### 检查安装

   ## 安装

   安装过程一路Next即可（傻瓜操作）

   注意将anaconda添加到环境变量中，不勾选需要后期在命令行使用的时候自己添加

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200224035438445.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0dob3N0R3Vlc3Q=,size_16,color_FFFFFF,t_70)

   ## 效果展示：

   安装完后会在开始菜单出现如下两个图标：

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200224035527537.png)
   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200224035508392.png)

   在下载完对应的Miniconda安装包之后，可以直接在开始菜单里找到Anaconda Prompt，直接使用Anaconda Prompt而不是cmd终端进入conda操作；或者你也可以按照课程视频所示（遵循[Miniconda安装及添加环境变量———小白教程](http://mp.weixin.qq.com/s/yqyEknvYLIH5E0nMlWEDSQ) ，按照教程中的步骤进行Miniconda的安装和环境变量添加）使用cmd终端进入conda操作。如果你选择了Anaconda Prompt，以后的所有操作就用Anaconda Prompt替代cmd终端，如果你选择了cmd终端，以后所有操作就直接在cmd终端进行。

   输入：conda info 查看conda安装信息

   ```shell
   conda info
   ```

   若能正常输出版本信息等即为安装成功。



## 使用`conda`管理环境和包

- `conda -h`：查看帮助；
- `conda info -e`：查看已有环境；
- `conda create -n <env_name> <package_names>`：创建新环境，并为新环境安装指定的包，可安装指定包的指定版本（可缺省）。例如:`conda create -n py3.5 python=3.5`；
- `source activate <env_name>`：切换到指定环境。Windows不用加`source`；
- `source deactivate`：退出环境至base。Windows不用加`source`；
- `conda remove -n <env_name> --all`：删除指定环境；
- `conda create --name <new_env_name> --clone <copied_env_name>`：复制环境；
- `conda list`：显示当前环境已安装的包；
- `conda search <package_names>`：搜索指定的包。也可使用通配符`*`模糊查找；
- `conda install <package_names>`：在当前环境安装指定的包；
- `conda remove <package_names>`：卸载当前环境的指定包；
- `conda update <package_names>`：更新当前环境的指定包；
- `conda update --all`：更新当前环境的所有包。

> 查看命令的帮助只需后加`-h`即可。例如，`conda create -h`

**查询完整帮助文件**
 `conda create --help` or `conda create -h` 其实“--”参数一般都有简写。

**管理conda和anaconda**
 `conda info` 查询conda信息
 `conda update conda` 升级conda
 `conda update anaconda` 升级anaconda

**管理环境**
 `conda info -e` 环境信息
 `conda create -n test python=2.7` 创建环境test，并指定python版本，此例为2.7
 `source activate test` 激活环境
 `source deactivate test` 关闭环境
 `conda remove --name test --all` 删除环境

**包管理**
 `conda list` 列出所有安装的包的信息
 `conda search beautiful-soup` 查询包
 `conda install -n test beautiful-soup` 安装包，并指定安装环境，如果没有-n test，则安装到当前环境
 `conda update beautiful-soup` 升级包
 `conda remove -n test beautiful-soup` 移除包



作者：ironbeak_owl
链接：https://www.jianshu.com/p/ce8af4e7869d
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

作者：Sui_Xin
链接：https://www.jianshu.com/p/20a92e5eb9af
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# Conda和pip比较

![img](https://upload-images.jianshu.io/upload_images/12713060-25623c3d88871cdf.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

Conda和pip通常被认为几乎完全相同。虽然这两个工具的某些功能重叠，但它们设计用于不同的目的。 [Pip](https://pip.pypa.io/en/stable/)是Python Packaging Authority推荐的用于从[Python Package Index](https://pypi.org/)安装包的工具。 Pip安装打包为wheels或源代码分发的Python软件。后者可能要求系统安装兼容的编译器和库。

[Conda](https://conda.io/docs/)是跨平台的包和环境管理器，可以安装和管理来自[Anaconda repository](https://repo.anaconda.com/)以 [Anaconda Cloud](https://anaconda.org/)的conda包。 Conda包是二进制文件，徐需要使用编译器来安装它们。另外，conda包不仅限于Python软件。它们还可能包含C或C ++库，R包或任何其他软件。

这是conda和pip之间的关键区别。 Pip安装Python包，而conda安装包可能包含用任何语言编写的软件的包。在使用pip之前，必须通过系统包管理器或下载并运行安装程序来安装Python解释器。而Conda可以直接安装Python包以及Python解释器。

另一个区别是conda能够创建可以包含不同版本的Python或其他软件包的隔离环境。在使用数据科学工具时，这非常有用，因为不同的工具可能包含冲突的要求，这些要求可能会阻止它们全部安装到单个环境中。 Pip没有内置的环境支持，而是依赖于[virtualenv](https://virtualenv.pypa.io/en/latest/)或[venv ](https://docs.python.org/3/library/venv.html)等其他工具来创建隔离环境。 pipenv，poetry和hatch wrap pip和virtualenv等工具提供了统一的方法来处理这些环境。

Pip和conda在如何实现环境中的依赖关系方面也有所不同。安装包时，pip会在递归的串行循环中安装依赖项。没有努力确保同时满足所有包的依赖性。如果较早安装的软件包与稍后安装的软件包具有不兼容的依赖性版本，则可能导致破坏的环境。conda使用可确保满足环境中安装的所有包的所有要求。此检查可能需要额外的时间，但有助于防止创建破坏的环境，前期关于依赖关系包的元数据是正确的。

考虑到conda和pip之间的相似性，有些人试图将这些工具结合起来创建数据科学环境也就不足为奇了。将pip与conda结合的主要原因是有些包只能通过pip安装。 Anaconda创酷提供超过1,500个软件包，包括最流行的数据科学，机器学习和AI框架。这些，以及包括conda-forge和bioconda在内的数据通过Anaconda云提供的数千个附加软件包，可以使用conda进行安装。尽管有大量的软件包，但与PyPI上提供的150,000多个软件包相比，它仍然很小。有时候需要的包没有conda包，但在PyPI上有，可以用pip安装。



|    类别    |        conda         |             pip             |
| :--------: | :------------------: | :-------------------------: |
|    管理    |        二进制        |        wheel 或源码         |
| 需要编译器 |          no          |             yes             |
|    语言    |         any          |           Python            |
|  虚拟环境  |         支持         | 通过 virtualenv或venv等支持 |
| 依赖性检查 |         yes          |      屏幕提示用户选择       |
|   包来源   | Anaconda repo和cloud |            PyPi             |