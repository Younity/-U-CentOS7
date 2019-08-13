# After installing CentOS7

## [EPEL](https://fedoraproject.org/wiki/EPEL)（Extra Packages For Enterprise Linux）
*When I want to install "Goldendict" (a translation software), I found the [EPEL](https://fedoraproject.org/wiki/EPEL)*

software could be install with EPEL:
- GoldenDict  
    ``` # yum install goldendict ```  
    - [About Dictionary1](http://blog.sina.com.cn/s/blog_933b54980102x6hr.html)  
    - [About Dictionary2](https://forum.ubuntu.org.cn/viewtopic.php?f=95&t=265588)
    - [Install mplayer](https://baijiahao.baidu.com/s?id=1598526149664765152&wfr=spider&for=pc)：解决goldendict中无法听单词发音的问题。
    
        ``` 
            // 获取mplayer的安装源：
            # yum localinstall http://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm
            // 安装 mplayer:
            # yum install mplayer
            // 安装 mplayer图形化界面：
            # yum install mplayer-gui
        ```
## 工具
1. [YouCompleteMe](https://github.com/ycm-core/YouCompleteMe)
    - 安装教程:
        - [参考](https://blog.csdn.net/fakine/article/details/91306166)
        - 更新VIM
            ``` 
                # rpm Uvh http://mirror.ghettoforge.org/distributions/gf/gf-release-latest.gf.el7.noarch.rpm
                # rpm --import http://mirror.ghettoforge.org/distributions/gf/RPM-GPG-KEY-gf.el7
                # yum -y remove vim-minimal vim-common vim-enhanced sudo
                # yum -y --enablerepo=gf-plus install vim-enhanced sudo
            ```
        - 更新g++ gcc
            ```
                # yum install centos-release-scl -y
                # yum install devtoolset-3-toolchain -y
                # yum install gcc-c++
                # scl enable devtoolset-3 bash
            ```
        - 下载git，安装YouCompleteMe
            ```
                # yum install git
                # git clone https://github.com/Valloric/YouCompleteMe.git ~/.vim/bundle/YouCompleteMe
                // 此时需要登陆github帐号
                # cd ~/.vim/bundle/YouCompleteMe
                # git submodule update --init --recursive
                // 上一条命令执行完报错：
                Cloning into 'third_party/go/src/golang.org/x/tools'...
                fatal: unable to access 'https://go.googlesource.com/tools/': Failed connect to go.googlesource.com:443; Connection timed out
                Clone of 'https://go.googlesource.com/tools' into submodule path 'third_party/go/src/golang.org/x/tools' failed
                Failed to recurse into submodule path 'third_party/ycmd'
            ```
                [解决办法](https://www.cnblogs.com/YMaster/p/11209813.html)：
                    在github上找到该模块下载到以下路径.                  
                    ```
                        # cd ~/.vim/bundle/YouCompleteMe/third_party/ycmd/third_party/go/src/golang.org/x
                        # git clone https://github.com/golang/tools.git
                    ```
       - 在～/下创建.vimrc
            ```
                # vim ~/.vimrc
                // 在该.vimrc中输入以下内容
                set nocompatible
                filetype off
                set
