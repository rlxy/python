# 共享变量
# - 概念： 当多个线程同时访问一个变量的时候，会产生共享变量的问题

# 不启用多线程，正常执行结果
import threading
sum = 0
loopSum = 100000
def myAdd():
    global sum, loopSum
    for i in range(1, loopSum):
        sum += 1
def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        sum -= 1
#这个没有执行多线程，一个一个来执行
if __name__ == '__main__':
    myAdd()
    print('myAdd最后的sum等于{0}'.format(sum))
    myMinu()
    print('myMinu最后的sum等于{0}'.format(sum))


# 多线程执行两个方法
import threading
sum = 0
loopSum = 100000

def myAdd():
    global sum, loopSum
    for i in range(1, loopSum):
        sum += 1
def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        sum -= 1
#这里启用了多线程，两个程序同时运行，这里本来要出现共享的问题，下面调用join函数，避免了这个问题
if __name__ == '__main__':
    print("Stating ....{0}".format(sum))
    # 启用多线程实例，查看执行结果
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())
    t1.start()
    t1.join()       #join是等待线程结束才会继续往下运行
    t2.start()
    t2.join()
    print("这是两个多线程同时调用sum变量来运行 .... {0}".format(sum))
    #如果上面程序不调用join的话他们会存在共享问题，因为同时的加减，会碰到同时加或减同一个数字
    #这就造成了最后的结果并不等于0


# 解决方案： 锁，
# 锁（LOCK）:
    # 是一个标志，表示一个线程在占用一些资源
    # 使用方法：
    # 上锁
    # 使用共享资源
    # 取消锁，释放锁
# 锁谁：
# 那个资源需要多线程共享，锁那个
# 理解锁：
# 锁其实是一个令牌，并且这个令牌只有一个，访问共享资源时需要去申请这个令牌，
# 只有申请到令牌的线程才能操作共享资源，操作完成后，需将令牌归还
import threading

sum = 0
loopSum = 100000
# 定义锁
lock = threading.Lock()
def myAdd():
    global sum, loopSum
    for i in range(1, loopSum):
        # 加锁，申请锁
        lock.acquire()
        sum += 1
        # 释放锁
        lock.release()
def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        # 加锁，申请锁
        lock.acquire()
        sum -= 1
        # 释放锁
        lock.release()
if __name__ == '__main__':
    print("Stating ....{0}".format(sum))
    # 启用多线程实例，查看执行结果
    t1 = threading.Thread(target=myAdd, args=())
    t2 = threading.Thread(target=myMinu, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("最后打印结束 .... {0}".format(sum))



# 线程安全问题：
    # - 如果一个资源/变量，它对于多线程来讲，不用加锁也不会引起任何问题，则称为线程安全。
    # - 线程不安全变量类型：list,set,dict
    # - 线程安全变量类型：queue
# 生产者消费者问题
    # 一个模型，用来搭建消息队列
# queue 是一个用来存放变量的数据结构，特点是先进先出，内部元素排队，可以理解成一个特殊的list

import threading
import time
import queue
####https://yiyibooks.cn/xx/python_352/library/queue.html#module-queue   queue模块的文档
# python2
# from Queue import Queue

class Produer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(100):
                    count = count + 1
                    msg = "生成产品" + str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    msg = self.name + "消费了" + queue.get()
                    print(msg)
            time.sleep(1)

if __name__ == "__main__":
    queue = queue.Queue()
    for i in range(500):
        queue.put("初始产品："+str(i))

    for i in range(2):
        p = Produer()
        p.start()

    for i in range(5):
        c = Consumer()
        c.start()




# 死锁问题

import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def funca():
    print("A 函数启动....")
    print("A 申请了锁1...")
    lock_1.acquire()
    print("A 等待申请锁2...")
    time.sleep(2)
    lock_2.acquire()            #程序卡死，造成了死锁，因为锁1和锁2分别在函数A 和函数B手里，他们都要得到两把锁才能释放锁
    print("A 释放了锁2...")
    lock_2.release()
    print("A 释放了锁1")
    lock_1.release()
    print("A 函数执行结束...")


def funcb():
    print("B 函数启动...")
    print("B 函数申请锁2...")
    lock_2.acquire()
    print("B 函数等待申请锁1...")
    time.sleep(4)
    print("B 函数申请申请锁1...")
    lock_1.acquire()        #程序会卡在这里，因为锁1被A函数申请去了，而A函数也在等待申请锁2   但是锁2在B函数手里

    print("B 函数释放锁1...")
    lock_1.release()
    print("B 函数释放锁2...")
    lock_2.release()
    print("B 函数执行结束...")


if __name__ == '__main__':
    t1 = threading.Thread(target=funca, args=())        #target是需要运行的程序
    t2 = threading.Thread(target=funcb, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()



# 解决死锁问题
import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()
def funcA():
    print("A 函数启动....")
    print("A 申请了锁1...")
    lock_1.acquire(timeout=4)           #申请四秒的锁1
    print("A 等待申请锁2...")
    time.sleep(2)
    res = lock_2.acquire(timeout=2)         #申请两秒的锁2,如果申请到则返回Trun，超过两秒还没有就返回false
    if res:
        print("A 得到了锁2...")
        lock_2.release()
        print("A 释放了锁2...")
    else:
        print("A 没有申请到锁2...")
        print("A 释放了锁1")
        lock_1.release()
    print("A 函数执行结束...")
def funcB():
    print("B 函数启动...")
    print("B 函数申请锁2...")
    lock_2.acquire()
    print("B 函数等待申请锁1...")
    time.sleep(4)
    print("B 函数申请申请锁1...")
    lock_1.acquire()
    #A函数申请到锁1但一直没有申请到锁2，超过了设置的2秒函数A释放了锁2
    print("B 函数释放锁1...")
    lock_1.release()
    print("B 函数释放锁2...")
    lock_2.release()
    print("B 函数执行结束...")

if __name__ == '__main__':
    t1 = threading.Thread(target=funcA, args=())
    t2 = threading.Thread(target=funcB, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()



# semphore
# - 允许一个资源最多由几个线程同时使用
import threading
import time
# 参数定义同一个资源最多几个线程同时使用
semphore = threading.Semaphore(3)       #最多用于3个多线程同时使用

def func():
    if semphore.acquire():
        for i in range(5):
            print(threading.currentThread().getName() + "get semphore")    #currentThread()返回当前的Thread对象，相当于调用者的线程
            time.sleep(15)
            semphore.release()
            print(threading.currentThread().getName() + "release semphore")

for i in range(8):              #这里设置了有8个多线程
    t1 = threading.Thread(target=func)
    t1.start()

    import threading
    import time

    def func():
        print("I am body")
        time.sleep(4)
        print("bay")

    if __name__ == "__main__":
        # Timer: 是利用多线程在指定时间后启动一个功能
        t1 = threading.Timer(6, func)
        t1.start()
        i = 0
        while i < 6:
            print("{0}..........".format(i))
            time.sleep(2)
            i += 1


# 可重入锁：
# - 可以被一个线程多次申请
# - 主要解决递归调用的时候，需要申请锁的情况（递归调用多次申请锁）
import threading
import time

lock = threading.RLock()

class MyThread(threading.Thread):       #定义一个类
    def run(self):
        global num
        num = 0
        time.sleep(1)
        if lock.acquire():
            num += 1
            msg = self.name + 'set num to ' + str(num)
            print(msg)
            lock.acquire()
            lock.release()
            lock.release()
def testTh():
    for i in range(5):
        t = MyThread
        t.start()           #这个for循环调用了5次类  每次调用都要一个锁
t = testTh()
print(t)


