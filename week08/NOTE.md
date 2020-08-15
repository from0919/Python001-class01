学习笔记
1. 变量的赋值
c = b = a 将a的值复制给b和c
1.1 可变数据类型（对象的引用）
列表
字典
1.2 不可变数据类型（对象本身）
整形int
浮点型 
字符串
元祖
传递对象本身，传递对象的引用

2. 容器序列的深浅拷贝

2.1 序列
容器序列  list tuple  collectons.deque 存放不同的数据类型
扁平序列：str,byes，bytearr 存放同一个数据类型
2.2 列表
list(list1)开辟了一个新的内存空间存放
切片操作也会创建的新的列表
2.3 深浅拷贝
import copy
深拷贝和浅拷贝只对容器序列有效
copy （浅拷贝）
copy.deepcocpy (深拷贝，申请一块新的内存)

3. 字典与扩展内置数据类型
namedtuple
poin = namedtuple()
a-b ,a__sub__(b)

4. 函数的调用
函数 可调用对象
调用问题：
不带括号，传递函数对象
带括号，传递函数的返回值

5. 变量作用域
Type Hint 变量类型提示
LEGB规则
L local 函数内的名字空间
E Enclosing function  locals 
G  Global
B builtin

6. 函数工具与高阶函数
6.1  各种类型的函数
偏函数：固定函数的某些参数
高阶函数：函数的参数是函数 -----lambda替代
lambada 只是表达式，不是所有的函数逻辑都能封装进去
高阶函数：参数是函数，返回值是函数
常见的 map reduce filter 
lambda  传入的参数：表达式
map(函数，参数) 迭代器
6.2 偏函数
add_1 = functools.partial(add,1)
add_1(10) 
import itertools 
functools itertools

7. 闭包
返回的关键字
return
yield

返回的对象
可调用的对象--闭包（装饰器）
my_line.__code__.co_varnames  编译后函数体的局部变量
my_line.__code__.co_freevars 编译后函数体的外部变量
my_line.__closure__[0].co_freevars
定义态  

8. 装饰器介绍
装饰器底层是由闭包实现
增加而不可变的函数
装饰器强调函数的定义态而不是运行态

flask 

9. 被装饰函数带参数和返回值的处理
func.__name__
被装饰函数的参数个数和内部函数个数一样
被装饰函数带不定长参数
foo2(a,b,c)
inner（*args,**wargs）
被装饰函数有返回值，内部函数也要有返回值
装饰器带参数 ----外出再嵌套一层函数
装饰器堆叠


10. Python内置装饰器
functools
functools.warps
@warps（func）
LRU.cache(淘汰机制，缓存)
@functools.lru_cache
collections

11. 类装饰器
__call__必须使用
11.1类做装饰器三个不同点
接受参数，引入__init__
外层函数,要写__call__
__call__的第一个参数是self
类也可以装饰类 
12. 官方文档中的装饰器代码阅读指南
PEP 新的功能，新功能添加的前因后果
      python的语法规范
dataclass
typehint类型提示
python功能
版本的注记说明
pep
13. 对象协议与鸭子类型
支撑实现协议：魔术方法
鸭子类型：定义的对象，没有初始化类型
容器类协议
__str__打印对象时，默认输出该方法的返回值
__getitem__、__set del_
__iter__
__call__可调用对象协议
比较大小的协议
__eg__
__gt__

__get__
__se__

__hash
上下文管理器
with上下文
__enter__()
__exit__()
f-string 
__str__字符串返回
__repr__ 程序之间调用
14. yield语句
生成器本质就是迭代器
在函数中使用yield关键字，可以实现生成器
生成器可以让函数返回迭代对象
迭代器终止时，会抛出stoplteration异常
函数被yield会暂停，局部变量也会被保存
可迭代  __iter__
next  __next__
Iterables  > Iterator > Generator
hasatter()
setatte动态添加属性
15. 迭代器使用的注意事项
import itertools
itertools.count()计数器
itertools.cycle(()）循环遍历
itertools.repeat 重复
itertools.chain 
字典插入操作后，字典迭代器会立即失效
列表插入，不会损坏迭代器，会自动变长
迭代器只能取一次，列表可以取多次

16. yield表达式
jump = yiled index

next(iterator) 
iterator.send(2)
next() 等于send(None)
yield暂停程序
yield可以为变量赋值
yield 实现循环控制，IO------协程

17. 协程简介
提高IO密集型工作效率
协程是异步的，线程是同步的
协程是非抢占市的，线程是抢占市的
线程是被动调度的，协程是主动调度的
协程是可以暂停函数的执行，保留上一次调用时的状态，是增强型生成器
协程是用户级的任务调度，线程是内核及的任务调度
协程适用于IO密集型程序，不适用于CPU密集型程序的处理
异步编程
python3.5 await取代yield from
import asynico
async def def py35_core():
    await stuff()
注意：await接受的对象的对象必须是awaitable对象
awaitable对象定义了__await__()方法
awaitable对象
1、协程corouting
2、任务task
3、未来对象Future
事件循环
注册，循环
asyncio.run(main())
协程调用过程：
调用协程时，会被注册到ioloop,返回corouting对象
用ensure_future 封装为Future对象
提交给ioloop

18. aiohttp简介
asynico 偏向于底层
asynio.get_event_loop()
run_until_complete
ensure_future
协程没有办法占多个cpu
asynico.run


