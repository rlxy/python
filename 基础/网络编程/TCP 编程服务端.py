import socket

def tcp_srv():
    #1，建立socket负责具体通信，这个socket其实只负责接受对方的请求，正真通信的是链接后需要用到两个参数
    #AF_INET: 含义同udp一直
    #sock_STREAM :表明是使用的tcp通信
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #2绑定端口和地址
    #此地址是tuple类型，第一部分未字符串，里面天ip，第二部分为端口
    addr = ('127.0.0.1',8998)
    sock.bind(addr)
    #监听接入的访问socket
    sock.listen()

    while True :
        #4，接受访问的socket，可以理解接受访问即建立了一个通讯的链接通道
        #accept返回的元组第一个元素赋值给skt，第二个赋值给addr
        skt,addr = sock.accept()
        #5，接受对方的发送内容，利用接收到的socket接收内容
        #500代表接收使用的buffersize
        msg = skt.recv(500)
        #接受到的是bytes格式内容
        #想得到str格式的，需要解码
        msg = msg.decode()

        rst = 'Received msg : {0} from {1}'.format(msg,addr)
        print(rst)
        #6,如果有必要，给对方发送反馈信息
        skt.send(rst.encode())

        #7，关闭链接通路
        skt.close()

if __name__ == '__main__':
    print("Starting tcp server.....")
    tcp_srv()
    print('Ending tcp server.....')


