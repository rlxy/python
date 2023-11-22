# 多线程 VS 多进程
# 程序： 一堆代码以文本形式存入一个文档
# 进程： 程序运行的一个状态
# 包含地址空间，内存，数据债等
# 每一进程由自己完全独立的运行环境，多进程共享数据是一个问题
# 线程
# 一个进程的独立运行片段，一个进程可以由多个线程
# 轻量化的进程
# 一个进程的多个线程间共享数据和上下文运行环境
# 共享互斥问题
# 全局解释器锁（GIL）
# Python代码的执行是由python虚拟机进行控制
# 在主循环中有切只有一个控制线程在执行
# Python包
# thread : 有问题，不好用，python3改成了_thread
# threading: 通行的包
# 案例01
'''
利用time函数，生产两个函数
顺序调用
计算总的运行时间
'''
import time


def loopl():
    # ctime 得到当前时间
    print('Statr loop l at : ', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print('End loop l at : ', time.ctime())


def loop2():
    # ctime 得到当前时间
    print('Start loop 2 at : ', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print('End loop 2 at : ', time.ctime())


def main():
    print('Starting at : ', time.ctime())
    loopl()
    loop2()
    print('All done at : ', time.ctime())


if __name__ == '__main__':
    main()

# 启用多线程
# -*- coding:utf-8 -*-
'''
利用time函数，生产两个函数
顺序调用
计算总的运行时间
'''


import time
import _thread as thread

def loopl():
    # ctime 得到当前时间
    print('Statr loop l at : ', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print('End loop l at : ', time.ctime())

def loop2():
    # ctime 得到当前时间
    print('Start loop 2 at : ', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print('End loop 2 at : ', time.ctime())

def main():
    print('Starting at : ', time.ctime())
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为start_new_thread
    # 参数两个，一个是需要运行的函数名，第二个是函数的参数作为元组使用，为空则使用空元组
    # 注意⚠️：如果函数只有一个参数，需要参数后有一个逗号
    thread.start_new_thread(loopl, ())
    thread.start_new_thread(loop2, ())
    print('All done at : ', time.ctime())

if __name__ == '__main__':
    main()
    time.sleep(5)
# 上面这个实验说明，这里的多线程和主线程都是同时开始，不会等待某个线程





# 带参数的函数，多线程执行例子

import time
import _thread as thread


def loopl(param):
    print('Statr loop l at : ', time.ctime())
    print("参数 param is ：" + param)
    time.sleep(4)
    print('End loop l at : ', time.ctime())

def loop2(name, name2):
    print('Start loop 2 at : ', time.ctime())
    print("姓名1：" + name, "姓名2 ：", name2)
    time.sleep(2)
    print('End loop 2 at : ', time.ctime())

def main():
    print('Starting at : ', time.ctime())
    thread.start_new_thread(loopl, ("今天天气不错",))     #这里给的参数，就算一个也要加个逗号
    thread.start_new_thread(loop2, ("王大拿", "王呵呵"))
    print('All done at : ', time.ctime())

if __name__ == '__main__':
    main()
    # 一定要有while语句，不然主线程结束，子线程也结束
    # while True:
    time.sleep(5)

# threading的使用
# - 直接利用threading.Thread生成Thread实例
    # - t = threading.Thread(target=xxx,args=(xxx,))
    # - t.statr(): 启动多线程
    # - t.join(): 等待多线程执行完成



import time
import threading


def loopl(param):
    # ctime 得到当前时间
    print('Statr loop l at : ', time.ctime())
    # 打印传入参数
    print("参数 param is ：" + param)
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print('End loop l at : ', time.ctime())


def loop2(name, name2):
    # ctime 得到当前时间
    print('Start loop 2 at : ', time.ctime())
    # 打印参数
    print("姓名1：" + name, "姓名2 ：", name2)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print('End loop 2 at : ', time.ctime())


def main():
    print('Starting at : ', time.ctime())
    t1 = threading.Thread(target=loopl, args=("老王头",))
    t1.start()

    t2 = threading.Thread(target=loop2, args=("张芃芃", "李冬面",))
    t2.start()

    print('All done at : ', time.ctime())


if __name__ == '__main__':
    main()

# JOIN（）用法
# join等线程执行完成后继续往下执行
# -*- coding:utf-8 -*-

import time
import threading


def loopl(param):
    # ctime 得到当前时间
    print('Statr loop l at : ', time.ctime())
    # 打印传入参数
    print("参数 param is ：" + param)
    # 睡眠多长时间，单位是秒
    time.sleep(4)
print('End loop l at : ', time.ctime())


def loop2(name, name2):
    # ctime 得到当前时间
    print('Start loop 2 at : ', time.ctime())
    # 打印参数
    print("姓名1：" + name, "姓名2 ：", name2)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print('End loop 2 at : ', time.ctime())
def main():
    print('Starting at : ', time.ctime())
    t1 = threading.Thread(target=loopl, args=("老王头",))
    t1.start()

    t2 = threading.Thread(target=loop2, args=("张芃芃", "李冬面",))
    t2.start()
    t1.join()
    t2.join()
    # 等待两个线程都执行完毕，才继续往下执行
    print('All done at : ', time.ctime())

if __name__ == '__main__':
    main()


# 守护线程
# - 如果在程序中将子线程设置成守护线程，则子线程会在主线程结束的时候自动退出
# - 一般认为，守护线程不重要或者不运行离开主线程独立运行
# - 守护线程案例能否有效果跟环境相关


# 非守护线程例子

import time
import threading

def fun():
    print("Strat fun")
    time.sleep(2)
    print("End fun")

    print("Main thread")

t1 = threading.Thread(target=fun, args=())
t1.start()

time.sleep(1)

print("Main thread end")


# 守护线程例子


import time
import threading

def fun():
    print("Strat fun")
    time.sleep(2)
    print("End fun")

print("Main thread")

t1 = threading.Thread(target=fun, args=())
# 使用守护线程的方法，必须在start之前设置，否则无效
t1.setDaemon(True)  #将守护下面睡眠中的进程，睡眠结束 所有进程结束
t1.start()          #开始t1进程
time.sleep(1)       #睡眠
print("Main thread end")



# 线程常用属性
# - threading.currentThread: 返回当前线程变量
# - threading.enumerate: 返回一个包含正在运行的线程list,正在运行的线程指的是线程启动后，结束前的线程
# - threading.activeCount: 返回正在运行的线程数量
# - thr.setName: 设置线程名称
# - thr.getName: 获取线程名称


import time
import threading


def loopl(param):
    # ctime 得到当前时间
    print('Statr loop l at : ', time.ctime())
    # 打印传入参数
    print("参数 param is ：" + param)
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print('End loop l at : ', time.ctime())


def loop2(name, name2):
    # ctime 得到当前时间
    print('Start loop 2 at : ', time.ctime())
    # 打印参数
    print("姓名1：" + name, "姓名2 ：", name2)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print('End loop 2 at : ', time.ctime())


def main():
    print('Starting at : ', time.ctime())
    t1 = threading.Thread(target=loopl, args=("老王头",))
    t1.setName("THR_1_loop1")
    t1.start()

    t2 = threading.Thread(target=loop2, args=("张芃芃", "李冬面",))
    t2.setName("THR_2_loop2")
    t2.start()

    # 3秒后，线程2结束运行
    time.sleep(3)

    # enumerat返回当前活着的Thread对象的列表。该列表包括守护线程、由current_thread()创建的虚假线程对象和主线程。
    # 它不包括已终止的线程和尚未开始的线程。
    #上面程序已经睡眠三秒，其中有一个进程结束，所以只能打印一个进程的名字
    for thr in threading.enumerate():
        print("正在运行的线程名字是： {0}".format(thr.getName()))
        print("正在运行的子线程数量为：{0}".format(threading.activeCount()))    #计算运行的线程
        print('All done at : ', time.ctime())
if __name__ == '__main__':
    main()


# 直接继承自threading.Thread
# - 直接继承Thread
# - 重写run()
# - 类实例可以直接运行

#普通写法
# 直接继承threading.Thread 重写run方法
import threading
import time

class ThreadFunc(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global n, lock
        time.sleep(1)
        if lock.acquire():  #当状态是unlocked时，acquire()改变该状态为locked并立即返回。
                            # 当状态是 locked 时，acquire() 阻塞，直到在另一个线程中对 release() 的调用将其改为 unlocked，然后 acquire() 调用重新设置它为 locked 并返回
            print(n,self.name)
            n,self.name
            n += 1
            lock.release()  #release释放一把锁。这可以从任何线程调用，而不仅仅是已经获得锁的线程。

if "__main__" == __name__:
    n = 1
    ThreadList = []
    lock = threading.Lock()         #添加一个lock
    for i in range(1, 200):
        t = ThreadFunc()
        ThreadList.append(t)
    for t in ThreadList:
        t.start()
    for t in ThreadList:
        t.join()        #后面加个join是让他们一个一个打印，否则会打乱顺序


# 企业写法
import threading
from time import sleep, ctime

loop = [4, 2]

class ThreadFunc():
    def __init__(self, name):
        self.name = name

    def loop(self, nloop, nsec):
        '''
        :param nloop: loop函数的名称
        :param nsec: 系统休眠时间
        :return:
        '''
        print("Start loop ", nloop, 'at ', ctime())
        sleep(nsec)
        print("Done loop ", nloop, 'at ', ctime())


def main():
    print("Starting at ", ctime())
    # ThreadFunc("loop").loop 跟以下两个式子相当：
    # t = ThreadFunc("loop")
    # t.loop

    # 以下t1 和 t2 的定义方式相等
    t = ThreadFunc("loop")

    t1 = threading.Thread(target=t.loop, args=('LOOP1', 4))
    #target是将被调用的可调用对象，args是给调用目标的参数元组。默认为()
    # 以下写法更西方化，工业化
    t2 = threading.Thread(target=ThreadFunc('loop').loop, args=('LOOP2', 2))
    # 常见错误写法
    # t1 = threading.Thread(target=ThreadFunc('loop').loop(100,4))
    # t2 = threading.Thread(target=ThreadFunc('loop').loop(100,2))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("ALL done at ", ctime())

if __name__ == '__main__':
    main()

