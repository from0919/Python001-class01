#作业1：区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：
'''
容器序列：list、tuple 、collections.deque
扁平序列：str、dict
可变序列：list、dict、collections.deque
不可变序列：tuple ，str
'''
#作业2：自定义一个 python 函数，实现 map() 函数的功能。
def map1(func2,arg1):
    mm = []
    if hasattr( arg1, '__iter__' ): 
        for i in arg1:
            temp = func2(i)
            mm.append(temp)   
        return mm
    else:
        raise Exception(f"变量{arg1}不是iterable")

#作业3：实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
import time
def timer(func):
    def inner(*args,**kwargs):
        st1 = time.time()
        func(*args,**kwargs)
        st2 = time.time()
        inter_time = (st2-st1)
        print('执行时间:', inter_time)
    return inner
@timer
def test1():
    for i in range(10):
        print(i)








