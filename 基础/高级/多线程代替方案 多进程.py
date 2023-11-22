# 线程代替方案
    # subprocess
        # 完全跳过线程，使用进程
        # 是派生进行的主要替代方案
        # python2.4后进入
    # multiprocessiong
        # 使用thronging接口派生，使用子进程
        # 允许为多核或者多cpu派生进程，接口跟threading非常相似
        # python2.6
    # concurrent.futures
        # 新的异步执行模块
        # 任务级别的操作
        # python3.2后引入
    # 多进程
    # 进程间通讯（InterprocessCommunication,IPC）
    # 进程之间无任何共享状态
    # 进程的创建
    # 直接生成Process实例对象。
    # 派生子类。
    # # 直接生成Process实例对象
    # -*- coding:utf-8 -*-

import multiprocessing
from time import sleep, ctime


def clock(interval):
    i = 0
    while i < 5:
        print("The time is %s" % ctime())
        sleep(interval)
        i += 1


if __name__ == '__main__':
    p = multiprocessing.Process(target=clock, args=(5,))
    p.start()

# 派生子类
# -*- coding:utf-8 -*-

import multiprocessing
from time import sleep, ctime


class ClockProcess(multiprocessing.Process):
    """
        两个函数比较
        1、init构造函数
        2、run
    """

    def __init__(self, interval):
        super().__init__()
        self.interval = interval

    def run(self):
        i = 0
        while i < 5:
            print("The time is %s" % ctime())
            sleep(self.interval)
            i += 1


if __name__ == "__main__":
    p = ClockProcess(3)
    p.start()

# 在os中查看pid,ppid的关系
# -*- coding:utf-8 -*-
from multiprocessing import Process
import os


def info(title):
    print(title)
    print("module name:", __name__)
    # 得到父进程的ID
    print("parent process:", os.getppid())
    # 得到本身进程的ID
    print("process id :", os.getpid())


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('whj',))
    p.start()


# 生产者消费者模型
# JoinableQueue
# -*- coding:utf-8 -*-
import multiprocessing
from time import sleep, ctime


def consumer(input_q):
    print("Into consumer:", ctime())
    i = 0
    while i < 100:
        # 预处理项
        item = input_q.get()
        print("pull", item, "out of q")  # 此项替换为有用的工作
        input_q.task_done()  # 发出信号通知任务完成
        i += 1
        print("Out of consumer:", ctime())


def producer(sequence, output_q):
    print("Into producer:", ctime())
    for item in sequence:
        output_q.put(item)
        print("put", item, "into q")
    print("Out of producer:", ctime())


if __name__ == "__main__":
    q = multiprocessing.JoinableQueue()
    # 运行消费者进行
    qc = multiprocessing.Process(target=consumer, args=(q,))
    qc.daemon = True
    qc.start()

    # 生产多个项，sequence代表要发给消费者的序列项
    # 在实践中，这可能是生成器的输出或通过一些其他方法的返回
    sequence = [1, 2, 3, 4]
    producer(sequence, q)
    # 等待所有项被处理
    q.join()

# 对列中哨兵的使用：通知作用
# -*- coding:utf-8 -*-
import multiprocessing
from time import sleep, ctime


def consumer(input_q):
    print("Into consumer:", ctime())
    while True:
        # 预处理项
        item = input_q.get()
        if item is None:
            break
        print("pull", item, "out of q")  # 此项替换为有用的工作
        input_q.task_done()  # 发出信号通知任务完成
        print("Out of consumer:", ctime())


def producer(sequence, output_q):
    print("Into producer:", ctime())
    for item in sequence:
        output_q.put(item)
        print("put", item, "into q")
    print("Out of producer:", ctime())


if __name__ == "__main__":
    q = multiprocessing.JoinableQueue()
    # 运行消费者进行
    qc = multiprocessing.Process(target=consumer, args=(q,))
    qc.daemon = True
    qc.start()

    # 生产多个项，sequence代表要发给消费者的序列项
    # 在实践中，这可能是生成器的输出或通过一些其他方法的返回
    sequence = [1, 2, 3, 4, -1]
    producer(sequence, q)
    q.put(None)  # 哨兵值
    # 等待所有项被处理
    qc.join()
