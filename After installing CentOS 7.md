# After installing CentOS 7

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
                set rtp+=~/.vim/bundle/Vundle.vim
                call vundel#begin()
                Plugin 'gmarik/Vundle.vim'
                call vundle#end()
                filetype plugin indent on
            ```
        - 安装
            ```
                # cd ~/.vim/bundle/YouCompleteMe
                # ./install.py --clang-completer
                // ERROR: folder python-future in /root/.vim/bundle/YouCompleteMe/third_party/ycmd/third_party is empty;
                # ./install.py --clang-completer（第二次）
                // ERROR: folder waitress in /root/.vim/bundle/YouCompleteMe/third_party/ycmd/third_party is empty; 
                // 分别从官网下载这两个文件放到本地。
                # ./install.py --clang-completer（第三次）
                // ERROR: folder waitress in /root/.vim/bundle/YouCompleteMe/third_party/ycmd/third_party is empty;
                // # yum install cmake
                # ./install.py --clang-completer（第四次）
                // ERROR: Python headers are missing in /usr/include/python2.7.
                // # yum install python-devel
                # ./install.py --clang-completer（第五次）
                // 成功。
           ```
       - 复制.ycm_extra_conf.py到～/
            ```
            # cp ~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py ~/
            // 复制失败，没有这个文件，然后自己在~/下自己创建一个.ycm_extra_conf.py
            ```
       - 在.vimrc中添加以下内容（自己瞎猜的）
       - 安装失败，打开vim，出现 no mapping found.
       - 这时发现自己时在root下安装的YouCompleteMe，又参考[官网教程](https://github.com/ycm-core/YouCompleteMe#full-installation-guide)安装。
        1. 检查Vim版本是 Vim7.4.1578以后的版本。 
           - 在vim中使用 `:version查询Vim版本`
           - 在vim中使用 `:echo has('python') || has('python3')`，输出1，表示该Vim是python支持版，返回0，则需要下载python支持的Vim
        2. 安装 Vundle（Vim插件管理器），使用[官方教程](https://github.com/VundleVim/Vundle.vim#about)
           - 在`.vimrc`指定的地方(Vundle安装中会说明)中加入`Plugin 'Valloric/YouCompleteMe'`
           - 在Vim中使用 `:PluginIstall` 安装Vundle插件-YouCompleteMe
           - 安装一个多小时出现错误信息，不能继续安装，改用在～/.vim/bundle/YouCompleteMe文件夹下使用 `git submodule update --init --recursive` 命令(YCM官方教程中提到，如果不使用Vundle安装，则使用这种方法，这里用来接续安装使用Vundle不能继续安装的部分，这种用法是想当然瞎猜的)
        3.    We'll create a new folder where build files will be placed. Run the following:
            ```
                cd ~
                mkdir ycm_build
                cd ycm_build
            ```
            - Now we need to generate the makefiles. If you DON'T care about semantic support for C-family languages or plan to use experimental clangd based completer, run the following command in the ycm_build directory:
                ```
                cmake -G "<generator>" . ~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp
                ```
                where <generator> is Unix Makefiles on Unix systems   
                
            - Now that configuration files have been generated, compile the libraries using this command:
                ```
                    cmake --build . --target ycm_core
                ```

        
        
2. gdb安装
- 使用gdb时报错Missing separate debuginfos, use: debuginfo-install glibc-2.17-157.el7_3.5.x86_64的[解决办法](https://blog.51cto.com/thinklili/2287379)
    - 使用root账户，修改"/etc/yum.repos.d/CentOS-Debuginfo.repo"文件的 enable=1。 
    - 安装glibc：
            ```sudo debuginfo-install glibc-2.17-260.el7_6.6.x86_64```



