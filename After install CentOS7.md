# After install CentOS7

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
