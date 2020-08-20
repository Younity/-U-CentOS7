# 用U盘安装CentOS 7

## 安装步骤：

1. 下载[CentOS 7](https://www.centos.org/)和[UltraISO](https://www.ultraiso.com/download.html)。

2. 使用UltraISO`写入硬盘映像`命令将`CentOS-7-x86_64-DVD-1810.iso`写入U盘，成功写入后，U盘名为`CentOS 7 x8`，此时U盘相当于一张光盘。

3. 打开U盘，删除`EFI文件夹`（第一次安装没有删除，结果在磁盘分区之后报错）。

4. 重启，设置BIOS从U盘启动（我用的Lenovo S41默认从U盘启动），之后，在选择界面选中`Install CentOS 7`选项，按`e`进入编辑，然后删除字符串`LABEL=CentOS\x207\x20x86_64 quiet`中的`6_64`，按下`Ctrl+x`执行。（这一步操作是保证LABEL的值与第2步中的U盘名一致，这样才能从U盘启动，windows限制了LABEL的长度为11，多余的部分被截断。）

5. 等待进入图形安装界面，设置语言，在`软件`选项中选择`GNOME Desktop`（默认是最小安装，即没有图形界面）。

6. 设置安装位置，选择在win7系统下压缩的`100G可用空间`，选择`我要配置分区`，然后选择`自动创建分区`（第一次分区时报错，然后删除EFI文件->`第3步`，重新安装就OK了）。

7. 点击`开始安装`，进入安装界面，此时可以设置`root密码`以及`创建用户`，等待20min左右，安装成功。

8. 安装CentOS 7后，电脑重启没有windows7启动项的解决办法:  

    8.1 进入root模式。在Terminal中输入`vi /etc/grub.d/40_custom`  

    8.2 在打开的文件`40_custom`末尾添加[代码(40_custom.txt)](https://github.com/Younity/-U-CentOS7/blob/master/40_custom.txt)(`windows7`是启动项要显示出来的名字，`chainloader`和`+1`之间有一个空格)：  

    8.3 在Terminal中输入`grub2-mkconfig -o /boot/grub2/grub.cfg` 
    
    8.4 在Terminal中输入`vi /boot/grub2/grub.cfg`  
    
    8.5 在打开的文件`grub.cfg`末尾添加[代码(grub.cfg)](https://github.com/Younity/-U-CentOS7/blob/master/grub.cfg)

    8.6 在Terminal中输入`grub2-mkconfig -o /boot/grub2/grub.cfg`。
    
9. 删除win10双系统中的centos7

    原文链接：https://blog.csdn.net/qq_38731633/article/details/78548459

    第一步：使用文件 "[覆盖linux引导](https://github.com/Younity/Use-CentOS-7/tree/master/%E8%A6%86%E7%9B%96linux%E5%BC%95%E5%AF%BC)" 中的MbrFix64.exe (64位系统，32位系统用MbrFix.exe)，将其放在C:/Windows/system32下，然后使用 "管理员模式" 打开命令提示符，使用命令 "cd ../.." ，进入C盘根目录，即 "c:>"，输入命令 "MbrFix64 /drive 0 fixmbr /yes"，这样就把linux的 grub 引导覆盖了，重启电脑，就没有linux的开机选择项了。

    第二步，在我的电脑，右键选择管理，磁盘管理，找到没有盘符标识的linux系统分区，右键删除卷，即可。
  
