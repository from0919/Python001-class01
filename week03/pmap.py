import socket
import os
import re
import argparse
import multiprocessing
from multiprocessing import Process
import queue
import threading
import time
import json


class NetMulti(Process):
    '''
    多进程网络工具类
    '''
    def __init__(self,thread_id,queue,parsetype,ip,iplock,port=0):
        super().__init__()
        self.thread_id = thread_id
        self.queue = queue
        self.parsetype = parsetype
        self.ip = ip 
        self.iplock =iplock
        self.port = port

    def run(self):
        '''
        重写run方法
        '''
        
        print(f'启动进程：{self.thread_id}')
        self.iplock.acquire()
        if self.parsetype == 'ping':
            self.ipping()                       
        elif self.parsetype == 'tcp':
            self.iptcp()
        else:
            print('传入参数有误%s'%self.parsetype)
            raise Exception
        time.sleep(1)
        self.iplock.release() # 释放
        print(f'结束进程：{self.thread_id}')

        
    def ipping(self):
        result = os.system('ping %s'%self.ip)
        if result == 0:
            self.queue.put(self.ip)
            print('%s能通信'%self.ip)
        else:
            print('%s不能通信'%self.ip) 

    def iptcp(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server.connect((self.ip, self.port))
            self.queue.put(self.port)
            print('{0} port {1} is open'.format(self.ip, self.port))
        except Exception as err:
            print('{0} port {1} is not open'.format(self.ip, self.port))
        finally:
            server.close()
            
  

def ipparse(ip):
    '''
    解析传入的ip地址段，如1.1.1.1-1.1.1.100
    '''
    
    pattern1 = ('\d+\.\d+.\d+.\d+?')
    pattern2 = ('\d+\.\d+.\d+.\d+\-\d+\.\d+.\d+.\d+')
    print(999)
    print(re.match(pattern2,ip))
    print(re.match(pattern1,ip))
    print(999)
    if re.match(pattern2,ip)!=None:
        iplist = ip.split('-')
        if iplist[0] < iplist[1]:
            ipx = ip.split('-')
            ip2num = lambda x:sum([256**i*int(j) for i,j in enumerate(x.split('.')[::-1])])
            num2ip = lambda x: '.'.join([str(x//(256**i)%256) for i in range(3,-1,-1)])
            listip = [num2ip(i) for i in range(ip2num(ipx[0]),ip2num(ipx[1])+1) if not ((i+1)%256 == 0 or (i)%256 == 0)]
            return listip
        else:
            print('第一个ip {0} 大于第二个ip {1}'.format(iplist[0], iplist[1]))
            raise Exception   
    elif re.match(pattern1,ip)!=None:
        return ip  
    else:
        print('传入参数有误%s'%ip)
        raise Exception


class NetThread(threading.Thread):
    '''
    多线程网络工具类
    '''
    def __init__(self,thread_id,queue,parsetype,ip,iplock,port=0):
        super().__init__() 
        self.thread_id = thread_id  
        self.queue = queue
        self.parsetype = parsetype
        self.ip = ip 
        self.iplock =iplock
        self.port = port

    def run(self):
        '''
        重写run方法
        '''
           
        print(f'启动线程：{self.thread_id}')
        self.iplock.acquire()
        if self.parsetype == 'ping':
            self.ipping() 
            # self.queue.task_done()                      
        elif self.parsetype == 'tcp':
            self.iptcp()
            # self.queue.task_done()
        else:
            print('传入参数有误%s'%self.parsetype)
            raise Exception
        time.sleep(1)
        self.iplock.release() # 释放
        print(f'结束进程：{self.thread_id}')
    
    def ipping(self):
        result = os.system('ping %s'%self.ip)
        if result == 0:
            self.queue.put(self.ip)
            print('%s能通信'%self.ip)
        else:
            print('%s不能通信'%self.ip) 

    def iptcp(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server.connect((self.ip, self.port))
            self.queue.put(self.port)
            print('{0} port {1} is open'.format(self.ip, self.port))
        except Exception as err:
            print('{0} port {1} is not open'.format(self.ip, self.port))
        finally:
            server.close()
    


    




if __name__ == "__main__":
    # pass
    #开始的时间
    st = time.time()
    #定义传入的参数
    '''
    -n：指定并发数量 ,可选参数
    -f ：指定扫描类型，ping或tcp，必选参数
    -ip：IP地址，可以支持连续地址段 1.1.1.1-1.1.1.100，必选参数
    -w：是否保存文件，支持json格式，如xxx.json ,可选参数
    -m: 指定扫描类型，参数proc（进程），thread（线程），必选参数
    -v: 查看程序耗时时间 ,可选参数
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-f')
    parser.add_argument('-ip')
    parser.add_argument('-n',type=int)
    parser.add_argument('-w')
    parser.add_argument('-m',nargs='?',default='proc')
    parser.add_argument('-v',nargs='?',default='123')
    args = parser.parse_args()
    ip = ipparse(args.ip)
    n_mulit = 0
    #进程和线程队列
    ipQueue=multiprocessing.Queue(10)
    threadQueue = queue.Queue(10) 
    #判断是否传入并发参数
    if type(args.n) ==int:
        print('检查并发参数')
        n_mulit =1
    
    #根据是否传入并发参数，确定传入的进程/线程名称
    netprocesslist = []    
    if n_mulit ==0:
        name_temp = 'netprocess1'
        netprocesslist.append(name_temp)
    else:
        for i in range(args.n):
            name_temp = 'netprocess' +str(i)
            netprocesslist.append(name_temp)
        
    #定义ip和端口遍历的迭代器，以及修正并发数量
    iplisttemp = []
    if type(ip) !=list:
        iplisttemp.append(ip)
        ipiter = iter(iplisttemp)
    else:
        ipiter = iter(ip)
        if len(netprocesslist) > len(ip):
            print("并发用户超过了遍历的ip，并发数采用遍历的ip数")
            netprocesslist = netprocesslist[:len(ip)]


    portlist =[]
    if args.f == 'tcp':
        for i in range(20,24):
            portlist.append(i)
        portiter = iter(portlist)
        print(portlist)

    #根据用户传入的‘-m’参数判断是采用进程和线程
    if args.m == 'proc':
        i = 1
        iplock = multiprocessing.Lock()
        #从队列中ip或者端口一个个从端口取出来查询
        result_list = []
        net_mulit_list = []
        print('proc....')
        while True:
            try:
                if args.f == 'ping':
                    for idname in netprocesslist:
                        ip = next(ipiter)
                        procesnet = NetMulti(idname,ipQueue,args.f,ip,iplock)
                        procesnet.start()
                        net_mulit_list.append(procesnet)
                    
                    
                else:
                    for idname in netprocesslist:
                        ip = iplisttemp[0]
                        port = next(portiter)
                        print('port is %d'%port)
                        procesnet = NetMulti(idname,ipQueue,args.f,ip,iplock,port)  
                        procesnet.start()
                        net_mulit_list.append(procesnet)

                # 结束进程
                for t in net_mulit_list:
                    t.join()
                while True:
                    if ipQueue.empty():
                        break
                    else:
                        result_list.append(ipQueue.get())
            
            except StopIteration:
                break
    elif args.m == 'thread':
        i = 1
        iplock = threading.Lock()
        #从队列中ip或者端口一个个从端口取出去查询
        result_list = []
        net_mulit_list = []
        print('thread....')
        while True:
            try:
                if args.f == 'ping':
                    for idname in netprocesslist:
                        ip = next(ipiter)
                        procesnet = NetThread(idname,threadQueue,args.f,ip,iplock)
                        procesnet.start()
                        net_mulit_list.append(procesnet)
                    
                    
                elif args.f == 'ping':
                    for idname in netprocesslist:
                        ip = iplisttemp[0]
                        port = next(portiter)
                        print('port is %d'%port)
                        procesnet = NetThread(idname,threadQueue,args.f,ip,iplock,port)  
                        procesnet.start()
                        net_mulit_list.append(procesnet)

                # 结束线程
                for t in net_mulit_list:
                    t.join()
                while True:
                    if threadQueue.empty():
                        break
                    else:
                        result_list.append(threadQueue.get())
                        threadQueue.task_done()
            
            except StopIteration:
                break
    else:
        print('指定的扫描器模型错误%s'%args.m)


    #结束的时间
    st1 = time.time()

    #判断是否将执行结果保存到文件中
    if args.w !=None:
        output = open(args.w,'a',encoding='utf-8') 
        if args.f == 'tcp':
            json_result ={'ip':args.ip,'test type':'tcp','port':result_list}
            json.dump(json_result,fp=output,ensure_ascii=False) 
        else:
            json_result = {'test type':'ping','ip':result_list}
            json.dump(json_result,fp=output,ensure_ascii=False) 
    #判断是否显示执行时间
    if args.v == None:
        print('执行时间:', st1 - st)





            


    

        

