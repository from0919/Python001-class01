学习笔记
安装mysql总结：
1、windows安装后，需要按照这个链接（https://www.jb51.net/article/182233.htm）做些前置准备工作（包括root的初始密码）
2、mysql如果安装在C盘，操作系统是win10,我遇到了“没有权限在mysql目录下新增my.ini文件”的问题，按照下面两个步骤操作
a、安装gpedit.msc，这样才能修改管理员权限 参照连接https://www.jianshu.com/p/949508a0b22d
b、修改组策略，参照连接http://www.xitongcheng.com/jiaocheng/win10_article_52909.html

模拟登陆石墨总结
1、寻找输入用户名和密码的登录路径时，可以使用xpath的相对路径如下面，但是这些写显得很累赘，而且不够灵活
browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('tmc81@163.com')

2、也可以使用属性定位，这样的代码比较简洁也比较灵活
 browser.find_element_by_xpath("//input[@name='mobileOrEmail']").send_keys('tmc81@163.com')
 
 
 疑问：
 1、请问下老师，发异常发生的是DownloaderMiddlewareManager类的download方法，这个方法要怎么才能重写？
 
 作业1要求对“下载部分增加异常捕获和处理机制”，我是将HttpProxyMiddleware模块的process_request方法进行了异常捕获，
 但是如果是代理ip不可用，报错的地方是如下；
 Traceback (most recent call last):
  File "d:\program files (x86)\python\lib\site-packages\scrapy\core\downloader\middleware.py", line 44, in process_request
    return (yield download_func(request=request, spider=spider))


