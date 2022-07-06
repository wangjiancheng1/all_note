<!--
 * @Author: WangJC 781424275@qq.com
 * @Date: 2022-07-01 16:21:04
 * @LastEditors: WangJC 781424275@qq.com
 * @LastEditTime: 2022-07-01 16:23:07
 * @FilePath: \c++\virtual.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
* 
-->
# 虚函数

virtual: 虚函数是指一个类中你希望重载的成员函数，当你用一个基类指针或引用指向一个继承类对象的时候，你调用一个虚函数，实际调用的是继承类的版本。