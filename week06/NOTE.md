学习笔记
学习内容：
1、网页访问查询路径
访问网页----> ROOT_URLCONF ---->urls.py--->urlpatterns----->自定义app的url.py----->自定义app的views.py
2、MTV三大模型
模型（Model）数据传入或者传出
模板（Template）页面展示，和static配合使用
视图（Views）网页访问请求接入，返回展示内容或指向模板
3、Mydjao处理流程
网页访问----->项目url---->app url---->views---->template
4、view量种函数处理
render：指向template中的网页
redirect：重定向其他url

作业内容：
1、MySQL 存储短评内容
1.1、使用scrapy创建爬虫项目
scrapy  startproject douban
cd douban 
scrapy genspider movie maoyan.com
1.2、使用BeautifulSoup进行爬取，页面F12查看和实际返回体可能存在差异，在爬取是可以将response打印出来，便于寻找特征属性
1.3、使用mysql存储数据，服务器连接写入setting
2、展示高于 3 星级（不包括 3 星级）的短评内容和它对应的星级
2.1 创建项目和app
django-admin startproject MyDjango
cd MyDjango
python manage.py startapp douban1
2.2 数据库导入ORM
遇到一个坑，windows系统下，通过下面两种方式导入 “python manager.py inspectdb  > app/models.py”或将 “python manager.py inspectdb“回显内容贴到app下的models.py中
