# gdb: [reference:](https://akaedu.github.io/book/)

### 入门

1. 单步调试

	```gdb				进入调试  	
	start			开始执行程序 
				
	list(l) 		列出源代码，每次10行  
	list(l)	 -n		列出第n行开始的源代码
		 -fn		列出函数fn的源代码

	step(s)			执行语句，会进入函数  
	next(n)			执行语句，不会进入函数  
	finish			连续运行到当前函数返回，然后等待命令  
				
	backtrace(bt)		查看各级调用函数及参数
	frame(f)		选择栈帧  
	info(i) locals		查看当前栈帧中局部变量的值  
				
	print(p)		打印表达式的值，通过表达式可以修改变量的值或调用函数  
	set var			修改变量的值  

	quit(q)			退出gdb
	```
2. 断点和条件断点
	```
	break(b) -n		设置断点-在第n行
		 -fn		设置断点-在函数fn开头
	
	break ... if ...	设置条件断点
	
	info(i) breakpoints	查看设置的断点

	disable breakpoints	禁用断点
	enable			启用断点

	delete breakpoints	删除断点

	display var		跟踪查看变量var的值
	undisplay var		取消跟踪查看变量var

	run(r)			从头开始运行程序
	continue(c)		从当前位置开始连续运行程序
	```
3. 观察点和段错误(watchpoints and segmentation fault)
	```
	watch			设置观察点  
	info(i) watchpoints	查看当前设置了哪些观察点  
	x			从某个位置打印存储单元的内容（按字节打印，不区分字节属于哪个变量）  

	backtrace(bt)		查看各级调用函数及参数,使用bt查看发生段错误的行
	```

