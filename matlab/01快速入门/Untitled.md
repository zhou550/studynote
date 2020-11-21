## 函数

| ==[`ans`](https://ww2.mathworks.cn/help/matlab/ref/ans.html)== | ==最近计算的答案==               |
| ------------------------------------------------------------ | -------------------------------- |
| ==[`clc`](https://ww2.mathworks.cn/help/matlab/ref/clc.html)== | ==清空命令行窗口==               |
| [`diary`](https://ww2.mathworks.cn/help/matlab/ref/diary.html) | 将命令行窗口文本记录到日志文件中 |
| [`format`](https://ww2.mathworks.cn/help/matlab/ref/format.html) | 设置命令行窗口输出显示格式       |
| [`home`](https://ww2.mathworks.cn/help/matlab/ref/home.html) | 发送光标复位                     |
| [`iskeyword`](https://ww2.mathworks.cn/help/matlab/ref/iskeyword.html) | 确定输入是否为 MATLAB 关键字     |
| [`more`](https://ww2.mathworks.cn/help/matlab/ref/more.html) | 控制命令行窗口中的分页输出       |
| [`commandwindow`](https://ww2.mathworks.cn/help/matlab/ref/commandwindow.html) | 选择命令行窗口                   |
| [`commandhistory`](https://ww2.mathworks.cn/help/matlab/ref/commandhistory.html) | 打开命令历史记录窗口             |



## 表达式



### 变量



与大多数其他编程语言一样，MATLAB® 语言提供数学*表达式*，但与大多数编程语言不同的是，这些表达式涉及整个矩阵。

MATLAB 不需要任何类型声明或维度说明。当 MATLAB 遇到新的变量名称时，它会自动创建变量，并分配适当大小的存储。如果此变量已存在，MATLAB 会更改其内容，并根据需要分配新存储。例如，

```
num_students = 25
```



创建一个名为 `num_students` 的 1×1 矩阵，并将值 25 存储在该矩阵的单一元素中。要查看分配给任何变量的矩阵，只需输入变量名称即可。



变量名称包括一个字母，后面可以跟随任意数目的字母、数字或下划线。MATLAB 区分大小写；它可以区分大写和小写字母。`A` 和 `a` *不*是相同变量。

尽管变量名称可以为任意长度，MATLAB 仅使用名称的前 `N` 个字符（其中 `N` 是函数 [`namelengthmax`](https://ww2.mathworks.cn/help/matlab/ref/namelengthmax.html) 返回的数字），并忽略其余字符。因此，很重要的一点是，应使每个变量名称的前 `N` 个字符保持唯一，以便 MATLAB 能够区分变量。

```
N = namelengthmax
N =
    63
```

### 数字



MATLAB 使用传统的十进制记数法以及可选的小数点和前导加号或减号来表示数字。科学记数法使用字母 `e` 来指定 10 次方的缩放因子。虚数使用 `i` 或 `j` 作为后缀。下面给出了合法数字的一些示例：

```
3              -99            0.0001
9.6397238      1.60210e-20    6.02252e23
1i             -3.14159j      3e5i
```



MATLAB 使用 IEEE® 浮点标准规定的 *long* 格式在内部存储所有数字。浮点数的有限*精度*约为 16 位有效小数位数，有限*范围*约为 10-308 至 10+308。

以双精度格式表示的数字的最大精度为 52 位。任何需要 52 位以上的双精度数字都会损失一定精度。例如，下面的代码因截断而将两个不相等的值显示为相等：

```
x = 36028797018963968;
y = 36028797018963972;
x == y
ans =
      1
```

整数的可用精度为 8 位、16 位、32 位和 64 位。将相同数字存储为 64 位整数会保留精度：

```
x = uint64(36028797018963968);
y = uint64(36028797018963972);
x == y
ans =
      0
```



MATLAB 软件存储复数的实部和虚部。该软件根据上下文采用不同方法来处理各个部分的量值。例如，[`sort`](https://ww2.mathworks.cn/help/matlab/ref/sort.html) 函数根据量值进行排序，如果量值相等，则根据相位角度排序。

```
sort([3+4i, 4+3i])
ans =
   4.0000 + 3.0000i   3.0000 + 4.0000i
```

这是由相位角度所致：

```
angle(3+4i)
ans =
    0.9273
angle(4+3i)
ans =
    0.6435 
```

“等于”关系运算符 `==` 要求实部和虚部相等。其他二进制关系运算符 `>`、`<`、`>=` 和 `<=` 忽略数字的虚部，而仅考虑实部。

### 矩阵运算符



表达式使用大家熟悉的算术运算符和优先法则。

| `+`   | 加法         |
| ----- | ------------ |
| -     | 减法         |
| `*`   | 乘法         |
| `/`   | 除法         |
| `\`   | 左除         |
| `^`   | 幂           |
| `'`   | 复共轭转置   |
| `( )` | 指定计算顺序 |

### 数组运算符



如果矩阵不用于线性代数运算，则成为二维数值数组。数组的算术运算按元素执行。这意味着，加法和减法运算对数组和矩阵都是相同的，但乘法运算不相同。MATLAB 的乘法数组运算表示法中包含点，也就是小数点。



运算符列表包括

| `+`  | 加法           |
| ---- | -------------- |
| `-`  | 减法           |
| `.*` | 逐元素乘法     |
| `./` | 逐元素除法     |
| `.\` | 逐元素左除     |
| `.^` | 逐元素幂       |
| `.'` | 非共轭数组转置 |



如果使用数组乘法将丢勒的幻方矩阵自乘

```
A.*A
```

则会生成一个数组，该数组包含介于 1 至 16 之间的整数的平方，并且以不常见的顺序排列：

```
ans =
   256     9     4   169
    25   100   121    64
    81    36    49   144
    16   225   196     1
```

#### 构建表

数组运算对构建表非常有用。假定 `n` 为列向量

```
n = (0:9)';
```

然后，

```
pows = [n  n.^2  2.^n]
```

构建一个平方和 2 次幂的表：

```
pows =
     0     0     1
     1     1     2
     2     4     4
     3     9     8
     4    16    16
     5    25    32
     6    36    64
     7    49   128
     8    64   256
     9    81   512
```

初等数学函数逐元素处理数组元素。因此

```
format short g
x = (1:0.1:2)';
logs = [x log10(x)]
```

构建一个对数表。

```
 logs =
      1.0            0 
      1.1      0.04139
      1.2      0.07918
      1.3      0.11394
      1.4      0.14613
      1.5      0.17609
      1.6      0.20412
      1.7      0.23045
      1.8      0.25527
      1.9      0.27875
      2.0      0.30103
```

### 函数



MATLAB 提供了大量标准初等数学函数，包括 [`abs`](https://ww2.mathworks.cn/help/matlab/ref/abs.html)、[`sqrt`](https://ww2.mathworks.cn/help/matlab/ref/sqrt.html)、[`exp`](https://ww2.mathworks.cn/help/matlab/ref/exp.html) 和 [`sin`](https://ww2.mathworks.cn/help/matlab/ref/sin.html)。生成负数的平方根或对数不会导致错误；系统会自动生成相应的复数结果。MATLAB 还提供了许多其他高等数学函数，包括贝塞尔函数和 gamma 函数。其中的大多数函数都接受复数参数。有关初等数学函数的列表，请键入

```
help elfun
```



有关更多高等数学函数和矩阵函数的列表，请键入

```
help specfun
help elmat
```



某些函数（例如，[`sqrt`](https://ww2.mathworks.cn/help/matlab/ref/sqrt.html) 和 [`sin`](https://ww2.mathworks.cn/help/matlab/ref/sin.html)）是*内置*函数。内置函数是 MATLAB 核心的一部分，因此这些函数非常高效，但计算详细信息是不可访问的。其他函数使用 MATLAB 编程语言实现，因此可以访问其计算详细信息。

内置函数与其他函数之间存在一些差异。例如，对于内置函数，您看不到代码。对于其他函数，您可以看到代码，甚至可以根据需要修改代码。



一些特殊函数提供了有用的常量值。

| [`pi`](https://ww2.mathworks.cn/help/matlab/ref/pi.html)     | 3.14159265...           |
| ------------------------------------------------------------ | ----------------------- |
| [`i`](https://ww2.mathworks.cn/help/matlab/ref/i.html)       | 虚数单位 G−1            |
| [`j`](https://ww2.mathworks.cn/help/matlab/ref/j.html)       | 与 `i` 相同             |
| [`eps`](https://ww2.mathworks.cn/help/matlab/ref/eps.html)   | 浮点相对精度 *ε*=2−52   |
| [`realmin`](https://ww2.mathworks.cn/help/matlab/ref/realmin.html) | 最小浮点数 2−1022       |
| [`realmax`](https://ww2.mathworks.cn/help/matlab/ref/realmax.html) | 最大浮点数 (2−*ε*)21023 |
| [`Inf`](https://ww2.mathworks.cn/help/matlab/ref/inf.html)   | 无穷大                  |
| [`NaN`](https://ww2.mathworks.cn/help/matlab/ref/nan.html)   | 非数字                  |



通过将非零值除以零或计算明确定义的*溢出*（即超过 [`realmax`](https://ww2.mathworks.cn/help/matlab/ref/realmax.html)）的数学表达式，会生成无穷大。通过尝试计算 `0/0` 或 `Inf`-`Inf` 等没有明确定义的数值的表达式，会生成非数字。

函数名称不会保留。您可以使用如下新变量覆盖任何函数名称

```
eps = 1.e-6
```

并在后续计算中使用该值。可以使用以下命令恢复原始函数

```
clear eps
```

### 表达式示例



您已经学习了 MATLAB 表达式的几个示例。下面是一些其他示例及生成的值：

```
rho = (1+sqrt(5))/2
rho =
    1.6180

a = abs(3+4i)
a =
     5

z = sqrt(besselk(4/3,rho-i))
z =
   0.3730+ 0.3214i

huge = exp(log(realmax))
huge =
  1.7977e+308

toobig = pi*huge
toobig =
   Inf
```

# 调用函数

要调用函数，例如 `max`，请将其输入参数括在圆括号中：

```
A = [1 3 5];
max(A)
ans = 5
```

如果存在多个输入参数，请使用逗号加以分隔：

```
B = [10 6 4];
max(A,B)
ans = 1×3

    10     6     5
```

通过将函数赋值给变量，返回该函数的输出：

```
maxA = max(A)
maxA = 5
```

如果存在多个输出参数，请将其括在方括号中：

```
[maxA,location] = max(A)
maxA = 5
location = 3
```

将任何字符输入括在单引号中：

```
disp('hello world')
hello world
```

要调用不需要任何输入且不会返回任何输出的函数，请只键入函数名称：

```
clc
```

`clc` 函数清空命令行窗口。