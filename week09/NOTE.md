学习笔记


5、Django  源码分析之view视图的请求相应完整过程
流程示意：browser ----modewsgi----request middlerwares------responese MIddlewares
url.py ---view middlewares---
模型的查询管理器---object
httprequest产生Request这一例，整个流程都带着这个请求的对象
template不是直接返回，而是通过model---->view
view 返回正确的结果和返回错误
content 上下文
请求----WSGI模块----为每个用户产生WSGI handler（控制整个请求）
WSGI（web server gateway interface）规范
注意：POST 不包含上传文件的数据，上传数据放在_files属性中，只有content-type 是multipart/form-date，才会有数据
返回是有view视图里自己手写的，手动编写httpResopone
中间件进行全局处理
manger.py

6、modle
自定义modle继承models.model，继承id和查询命令
进行简单的CRUD
不需要显示定义主键(id自动化创建)
自动拥有查询管理器对象
可以用ORM API对数据库、表进行CRUD
id --modelbase
元类的父类必须是type，不能是object
实现new的方法，返回的是一个类

7、查询管理器
如何让查询管理器的名称叫object
为什么查询管理器返回Queryset
manager 继承自 BaseManagerFromQueryset类，拥有QuerySet的大部分方法
get create filter
type创建类，查询类
Queryset大量的方法赋值给Queryset新建的对象，Queryset新建的对象 basemanager，basemanager的子类是manager，manager的实例是Object，
objects是basemanager的一个实例
动态添加类（后面补上！！！！！）


8、template模板加载文件
render----render_to_string------get_template-----engine(settings.py(templates----backend))-----
engine.get_templat----find_template-----loader.get_template------?---------template_dirs---get_app_template_dirs(utils.py，在Enginehandller类中)-------

模板引擎加载
engines = enginehandller(slef._templates = setting.TEMPLATES)
@cache_property‘




10、Django 管理页面
migrate创建管理页面
创建管理员账号：
python  manage.py createsupuser
在app目录增加admin.py

index/admin.py
from ./model import Type Name
注册模型
admin.site.register(Type)
admin.site.register(Name)

INSTALLED_APPS
内置后台管理系统
django.contrib.admin

将admin的库同步到mysql中
python manage.py migrate

官方文档中有丰富的管理界面样式


11、表单
表单是以post方式体现
<form> 开始 </form>结束
Django 使用Form对象定义表单
from django import forms
class  LoginForm(forms.Form)：
    username = forms.ChareField()
     password = forms.ChareField(widget= forms.PasswordInput,min_length=6)
常见表单字段 subject,message,sender和cc_myself----参加官方文档
表单在HTML呈现
html{{ form }}
url ----views(引用表单文件)----- 
view试图里定义方法
if request.method === 'POST'
if request.method === 'GET':
 login_form = loginForm()
 return render(request, 'form2.html',{'form': login_form})
12.CSRF防护
只用作post请求
 
{% csrf_token %}
通过中间件实现
setting.py  Django.middleware.csrf.CsrfViewMiddleware
from  django.views.decorators.csrf import csrf_exempt ,csrf_protect
@csrf_exempt @csrf_protect单独控制某一个view视图

13、用户管理认证
用户注册：autheenticate
登录login（request，user）
退出 loginout
注册用户：
python manage.py shell  ---进入交互环境
from  django.contrib.auth.models import User
user = User.objects.create_user('jerry','jerry@jerry.com','jerrypassword')
user.save()
 from django.contrib.auth import authenticate
authenticate(username='jerry',password='jerrypassword')



17 celery 介绍
celery  分布式消息队列
使用celery实现定时任务
celery beat定时任务
安装celery前置步骤 安装redis
redis-server 启动redis
redis.conf注意事项
1、daemonize （非调试环境yes，正式环境no）
2、bind 127.0.0.（公用时0.0.0.0)
3、requirepass 访问密码

启动redis
redis-server ./redis.conf
dump.rdp redis启动文件

安装celery 
pip install celery
pip install redis==2.10.6(redis驱动程序)
pip install celery-with-redis
pip install django-celery
18、celery 定时任务的实现
django管理界面去管理定时任务
celery 集成到django
3、添加app
django-admin startproject MyDjango	
python manager.py startapp djcron

INSTALL_APPS = [
'djcelery',
'djcron'
]
4、迁移生成表
Python manage.py migrate ----创建djcelery、admin数据库和表
5、配置django时区
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
from  celery.schedules import crontab
from celery.schedules import timedelta 时间偏移
BROKER_URL = ‘redis://123456:127.0.0.1:6379/’后段的存储对应的路径
CELERY_IMPORTS = ('djcron.tasks')
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYBEAT_SCHEDULER=''
6、在MyDjango下添加celery.py ------不用做任何更改
初始配置
from celery 从第三方库找
from .celery 从本地找

7、在__init__.py增加
from __future__import absolute_import(写在最前面)
from .celery import app as celery_app
8、在app中创建task.py
from MyDjango.celery import app
@app.task()
def get_task():
    returun 'test'
9、启动生产者和消费者(在项目中启动)
celery -A MyDjango beat -l info 生产者
celery -A MyDjango worker -l info
10、设置何时启动执行
在crontabs 都是*表示每一份都执行一次
*/5 每5
Peridoic 任务和执行任务绑定
19、Flask 上下文与信号
1、WSGI协议的实现-----Werkzeuq
2、Jinjia模板
导入扩展模板
pip install flask
如何运行flask
export  FLASK_APP = hello.py
flask run
文档 
快速上手
url_for 通过函数去反向寻找路径
渲染模板 render_template('hello.html',name= name )
flask和Django的差异
1、flask 没有request关键字，通过上下文去连接
上下文
1、request 和 sesion
信号：Flask 从0.6开始，通过Blink林如
请求和会话
request_ctx_stack
ctx.request.method   ----get
信号
from flask import signals
singals.request_started.connect
20 Tornado 简介与其他常见网络框架

Tornado的同步和异步IO
http_client= HttpClient()
http_client = AsyncHTTPClient()
add_done_callback()回调函数 注册-----发生---调用


toarnado 作为服务端
gevent 并发框架 代码好维护
twisted 异步网络框架 稳定性最好 对tcp和udp都能支持
toarndao  兼容性最好 单进程