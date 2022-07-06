/*
 * @Author: WangJC 781424275@qq.com
 * @Date: 2022-07-01 16:25:27
 * @LastEditors: WangJC 781424275@qq.com
 * @LastEditTime: 2022-07-01 18:50:42
 * @FilePath: \c++\virtual.cpp
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
#include "stdio.h" 
#include "conio.h"
 
class Parent
 
{
	
public:
	char data[20];
	void Function1();	
	virtual void Function2();   // 这里声明Function2是虚函数
	
}parent;
 
void Parent::Function1()
{
	printf("This is parent,function1\n");
}
 
void Parent::Function2()
 
{
	printf("This is parent,function2\n");
}
 
class Child:public Parent
 
{
	void Function1();
	void Function2();
	
} child;
 
void Child::Function1()
 
{
	printf("This is child,function1\n");
}
 
void Child::Function2()
 
{
	printf("This is child,function2\n");
}
 
int main(int argc, char* argv[])
 
{
	Parent *p;  // 定义一个基类指针
	if(_getch()=='c')     // 如果输入一个小写字母c	
		p=&child;         // 指向继承类对象
	else	
		p=&parent;       // 否则指向基类对象
	p->Function1();   // 这里在编译时会直接给出Parent::Function1()的入口地址。	
	p->Function2();    // 注意这里，执行的是哪一个Function2？
	return 0;
}