# 用U盘安装CentOS7

## 安装步骤：
1. 下载CentOS7和UltraISO。
2. 使用UltraISO将CentOS7的ISO文件写入U盘，成功写入后，U盘名为`CentOS 7 x8`，此时U盘相当于一张光盘。
3. 打开U盘，删除EFI文件夹（第一次安装没有删除，结果在磁盘分区之后报错）。
4. 重启，设置BIOS从U盘启动，之后，在选择界面选中`Install CentOS 7`选项，
按“e”进入编辑，删除字符串`LABEL=CentOS\x207\x20x86_64 quiet`中的`6_64`，按下Ctrl+x执行。
（windows限制了LABEL的长度为11，多余的部分被截断。这一步操作是保证LABEL的值与第2步中的U盘名一致，这样才能从U盘启动）
5. 等待进入图形安装界面，设置语言，在`软件`选项中选择`GNOME Desktop`（默认是最小安装，即没有图形界面）。
6. 设置安装位置，选择在win7系统下压缩的`100G可用空间`，选择`我要配置分区`，然后选择`自动创建分区`（第一次分区时报错，然后删除EFI文件->`第3步`，重新安装就OK了）。
7. 点击`开始安装`，进入安装界面，此时可以设置root密码以及创建用户,等待20min左右，安装成功。
8. 安装CentOS7后，电脑重启没有windows7启动项的解决办法:  

        8.1 进入root模式。在Terminal中输入`vi /etc/grub.d/40_custom`
        8.2 在打开的文件末尾添加以下代码：
  ```
  menuentry 'windows7' {
    set root=(hd0,1)
    chainloader +1
    }
  ```
  (说明：'windows7'是启动项要显示出来的名字，`chainloader`和`+1`之间有一个空格)
        8.3 在Terminal中输入`grub2-mkconfig -o /boot/grub2/grub.cfg`
        8.4 在Terminal中输入`vi /boot/grub2/grub.cfg`
        8.5 在打开的文件末尾添加一以下代码：
  ```
  menuentry'window7' {
    insmod chain
    insmod ntfs
    set root=(hd0,msdos1)
    chainloader +1
  }
  
  menuentry 'window7 search' {
    insmod chain
    insmod ntfs
    search -f /ntldr
    chainloader +1
  }
  ```
        8.6 在Terminal中输入`grub2-mkconfig -o /boot/grub2/grub.cfg`。
  
