学习笔记
一、课堂笔记
1. 类属性与对象属性
python 2.2以前 古典类，以后 新式类
object基础类
类的两大成员：属性和方法
属性
a、类属性宇对象属性
b、类属性字段在内存中只保存一份
c、对象属性在每个对象都保存一份
self 约定俗成，可以改成任一一个名字
__dict__查看属性
实例不能修改类的静态属性
type(a)
id(a)
a.__class__()

2. 类的属性作用域
类.属性 新增类属性
dir 查看类所带的属性
内置类型不能增加属性和方法
setattr，给指定类添加属性名字和值
网上查询给内置类添加属性和方法
_age  人为不可修改，
__fly  私有属性,python对其改名，防止被修改，防止程序误调用
__init__ 、魔术方法,跟随着系统进行变化
().__class_ 返回所属类
().__class_.__base__ 返回父类
().__class_.__base__[0]
().__class_.__base__[0].__subclasses__() 返回父类的所有子类

3. 类方法描述器
@ 语法糖，在原有方法上加上特殊的功能
@classmethod 类方法
@staticmethod 静态方法
普通方法  self.方法
类方法   cls.方法，调用时会把cls替换成类
静态方法 由类调用，无参数
__init__ 初始化函数
初始化类 必调用的方法
接受参数
__new__ 构造函数
import 
绑定方法
实例找__dict__，再去类里找
@classmethod 子类调用父类的方法，当类需要构造
1、子类调用父类的方法
2、函数调用类，并且返回类的时候

4. 静态方法描述器
staticmethod 判断和类型转换

5. 描述器高级应用__getattribute__
对实例获取属性
__getattribute__对有属性的访问都会调用该方法
__getattr()使用与未定义的属性


7. 描述器原理&属性描述符
描述器 实现特定协议（描述符）的工具
property 属性描述符
__get__
__set__
__delete
property 把方法封装成属性(只读)
# 被装饰函数建议使用相同的gender2
# 不使用setter 并不能真正意义上实现无法写入，gender被改名为 _Article__gender
property本质不是函数，而是特殊类
如果实现了__get__()和__set__数据描述符
如果仅仅定义了__get__(),则称为数据描述符

8. 面向对象编程-继承
object 和 type都属于type类（class 'type'）
type 元类
object的父类为空，没有继承任何类
type的父类为object类 
单一继承
多重继承
菱形继承
MRO
MRO和C3算法
super._getattribute
print('object', object.__class__, object.__bases__)
print('type', type.__class__, type.__bases__)
# type元类由type自身创建，object类由元类type创建
# type类继承了object类
新式类 广式优先
.mro 显示调用顺序
有向无环图DAG (入度为0的节点)

9. solid设计原则与设计模式&单例模式
单一责任原则  
开发封闭原则
里氏替换原则
单例模式
1、对象只存在一个实例
__new__ 静态方法
__init__ 实例方法
__new__先被调用，__init__后被调用
装饰器 
1、装饰器
2、__new__
3、import

10. 工厂模式
静态工厂模式  根据传入的参数不同，创建不同的类
类工厂模式

11. 元类
创建类的类 type,是类的模板
控制如何来创建类，
元类的实例为类
创建元类的两种方法
1、type
2、class

type(类名称，父类的元祖，类的成员)
Foo = type('Foo',(),{'say_hi':hi})

metaclass = DelValue 元类
元类必须继承type
必须实现new方法
13 mixin
抽象基类
避免继承错误，使类层次易于理解和维护
无法实现化基类
如果忘记在其中一个子类中实现接口方法，要及早报错
abstractmethod
Minxin
__bases__ 


二、作业笔记
super().__init__(*args),子类引用时，参数个数应与父类实例属性保持一致