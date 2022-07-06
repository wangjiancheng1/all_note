<!--
 * @Author: WangJC 781424275@qq.com
 * @Date: 2022-06-07 14:10:00
 * @LastEditors: WangJC 781424275@qq.com
 * @LastEditTime: 2022-06-07 15:27:34
 * @FilePath: \halcon\parameter.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# **halcon**

**图像类型格式**

‘byte’ 每像素1字节，无符号 值范围: (0到255)

‘int1’ 每像素1字节，有符号 值范围: (-128到127)

‘uint2’ 每像素2字节，无符号 值范围: (0到65535)

‘int2’ 每像素2字节，有符号 值范围: (-32768到32767)

‘int4’ 每像素4字节，有符号 值范围: (-2147483648到2147483647)

‘int8’ 每像素8字节，有符号（仅适用于x64系统） 值范围: (-9223372036854775808到9223372036854775807)

‘real’ 每像素4字节，浮点类型，6位有效十进制数字精度 值范围: (-3.4e38到3.4e38)

‘complex’ real类型的两个矩阵，向量

‘vector_field_relative’ real类型的两个矩阵，向量

‘vector_field_absolute’ real类型的两个矩阵，绝对坐标

‘direction’ 每像素1字节，无符号 值范围: (0到179)，角度除以2
注意:数值180到254被自动设置为值255，这被解释为未定义的角度。

‘cyclic’ 每像素1字节，无符号，循环算术 范围: (0到255)

https://blog.csdn.net/weixin_43488529/article/details/120533402

在Halcon算子的参数中，依次为：(输入图形参数:输出图形参数:输入控制参数:输出控制参数)；并且其输入参数不会被算子改变。

## halcon 参数类别
### 1.图形参数 Iconic (image, region, XLD)
#### (1) Images

在Halcon中，Image = Channel + Domain（定义域） , 像素点存放在Channel矩阵中，根据ROI来描述Image。

***Image相关操作：***

**输入**：从文件、从设备

**生成**：外部图像数据、空内存区域；

**显示**：disp_image()图像首通道灰度图；disp_color() 彩色图；disp_channel()某特定通道；disp_obj() 自动判别类别；

**缩放**：set_part() 设置显示区域；set_part_style() 设置显示参数；

**说明：**

1. Multiple channels //多通道图像，可以是灰度图像或RGB图像

2. Arbitrary region of interest //ROI区域图像

3. Multiple pixel types(byte, (u)int1/2/4,real, complex, direction, cyclic, vector_field)

byte, uint2 //灰度图像的标准编码

int1, int2 //Difference of two images or derivates with integer precision（？？）int4 //两幅灰度图的频谱

direction //图片边缘的梯度方向

real //边缘提取及特定灰度值的轮廓

complex //图片频率分布

cyclic //Assigning one "gray" value to each color（？？）

vector_field //连续图形的光学流分布

#### (2) Regions

以行列坐标形式储存，有广泛的应用，特点是高效，可利用同态算子。比如用阈值对图像分割的结果，其他系统中称为BOLB,AREA等。

#### (3) Extended Line Description (XLD)（亚像素精度。 有两种基本的 XLD 结构：轮廓和多边形）

图像均用像素点保存，而像素点是整型的，不连续的，Halcon做了拓展，定义了亚像素（subpixel）的描述几何轮廓的对象：xld，主要用在亚像素测量的背景下，可用于如提取边缘、构建轮廓等等，xld在模板匹配、图形校准等多方面有重要的用途。

**说明：**

Subpixel accurate line and edge detection（亚像素精度的线和边缘检测）

Generic point list based data structure（依据数据结构产生点的表）

Handling of contours, polygons, lines, parallels, etc.（对轮廓，多边形，线等进行操作）


### 2.控制参数Control (string, integer, real, handle)

String类型变量由单引号''括起来；此外还有一些特殊字符；

Boolean型变量包括 true ( = 1 ), false ( = 0 ) ；不为零的整数将被认为true:但绝大多数的Halcon函数接受字符串型的表达：'true','false'，而非逻辑型表达；

此外，Halcon支持的类型还包括图形元组、控制变量元组及句柄：

元组的概念，使得可以用一个变量传递数个对象，可以由重载后的函数来进行处理；图形元组的下标从1开始，控制变量元组下标从0开始；句柄则可以用来描述窗体、文件等等，句柄不能是常量。