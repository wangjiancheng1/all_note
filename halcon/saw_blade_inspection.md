<!--
 * @Author: WangJC 781424275@qq.com
 * @Date: 2022-06-07 14:33:40
 * @LastEditors: WangJC 781424275@qq.com
 * @LastEditTime: 2022-06-08 22:35:34
 * @FilePath: \halcon\saw_blade_inspection.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# Halcon 测量锯齿角度
```
***** 初始化
*
* 宏定义角度常量
PI := rad(180)  
PI_2 := rad(90)
* 
* 显示初始化
dev_update_off ()
read_image (Image, 'saw_blade/saw_01')
get_image_size (Image, Width, Height)
* 关闭活动图形窗口
dev_close_window ()
* 打开一个保留给定图像纵横比的新图形窗口。
dev_open_window_fit_image (Image, 0, 0, 640, 640, WindowHandleMain)
* 设置窗口显示字体样式
set_display_font (WindowHandleMain, 16, 'mono', 'true', 'false')
* 获取创建的图像窗口属性参数
get_window_extents (WindowHandleMain, WindowRow, WindowColumn, WindowWidth, WindowHeight)
* 打开一个新的图形窗口
dev_open_window (400, WindowWidth / 2, 300, 300, 'black', WindowHandleZoom)
* 设置图形窗口显示线宽
dev_set_line_width (2)

***** 主循环 ：对给定7张锯齿图片进行图像处理分别获得每张图片上各锯齿角度
for Index1 := 1 to 7 by 1
    *
    * 预处理
    * 读取锯片图像(路径匹配)
    read_image (Image, 'saw_blade/saw_' + Index1$'02')
    * 进行亚像素精确阈值分割，得到锯片的轮廓。
    threshold_sub_pix (Image, Border, 128)
    * 将阈值分割后的轮廓按'lines_circles'模式分割成多段直线、圆弧。
    segment_contours_xld (Border, ContoursSplit, 'lines_circles', 5, 6, 4)
    * 通过形状特征选择分割后的多段轮廓。
    select_shape_xld (ContoursSplit, SelectedContours, 'contlength', 'and', 30, 200)
    * 获取所有分割轮廓(线段、圆弧)的总数量
    count_obj (SelectedContours, Number)

    *
    * 过滤出所有直线并获取计算直线方向
    * 创建一个空的用来存储所有直线的图像对象
    gen_empty_obj (ToothSides)
    * 遍历所有分割轮廓，根据属性值，筛选出直线。
    for Index2 := 1 to Number by 1
        * 根据索引值从选取对应分割轮廓
        select_obj (SelectedContours, SelectedContour, Index2)
        * 获得分割轮廓的全局属性值。
        get_contour_global_attrib_xld (SelectedContour, 'cont_approx', Attrib)
        * 对于直线，属性为-1。
        if (Attrib == -1)
            * 将直线存入存储直线数组中
           concat_obj (ToothSides, SelectedContour, ToothSides)
        endif
    endfor
    * 根据选出的直线相对位置进行排序
    sort_contours_xld (ToothSides, ToothSidesSorted, 'upper_left', 'true', 'column')
    * 拟合xld的直线
    fit_line_contour_xld (ToothSidesSorted, 'tukey', -1, 0, 5, 2, Rows1, Columns1, Rows2, Columns2, Nr, Nc, Dist)
    * 计算直线的方向
    line_orientation (Rows1, Columns1, Rows2, Columns2, Orientations)

    *
    * 测量属于同一齿的两边之间的夹角
    * 创建一个空数组，用来存放角度
    Angles := []
    * 检查第一个锯齿是否是完全齿，如果不完全，从第二颗牙齿开始测量
    if (Rows1[0] > Rows2[0])
        Start := 1
    else
        Start := 2
    endif
    * 遍历所有以上获得线段方向，通过将属于同一个锯齿的两条线段方向作差，进而求得所有锯齿角度
    for Index2 := Start to |Orientations| - 1 by 2
        Angle := abs(Orientations[Index2 - 1] - Orientations[Index2])
        * 确保角度在区间[0,PI/2]内。
        if (Angle > PI_2)
            Angle := PI - Angle
        endif

        *
        * 结果显示
        * 自定义函数：将结果显示在主图形窗口和副图形窗口
        dev_display_tooth (Image, ToothSides, Index2, Rows1, Columns1, Rows2, Columns2, WindowHandleMain, WindowHandleZoom)
        * 激活图形窗口，设置显示文本
        dev_set_window (WindowHandleMain)
        dev_disp_text ('Tooth ' + (Index2 + 1) / 2, 'window', 10, 10, 'black', [], [])
        dev_disp_text ('Included Angle: ' + deg(Angle)$'.2f' + ' deg', 'window', 35, 10, 'black', [], [])
        dev_disp_text ('Press Run (F5) to continue', 'window', 'bottom', 'right', 'black', [], [])
        * 将一张图片上计算处理的锯齿角度全部存放在一个角度数组中
        Angles := [Angles,Angle]
        stop ()
    endfor
endfor

***** 结束
* 主窗口结束显示
dev_set_window (WindowHandleMain)
dev_disp_text ('      End of program      ', 'window', 'bottom', 'right', 'black', [], [])
* 关闭副图形窗口
dev_set_window (WindowHandleZoom)
dev_close_window ()
```