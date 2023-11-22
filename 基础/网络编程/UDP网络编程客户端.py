'''
Client端流程
    1，建立通信的socket
    2，发送内容到指定服务器
    3，接收服务器给定的反馈内容
'''
import socket

def clientFunc():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    text = input('请输入你需要发送的信息：')

    #发送的数据必须是bytes格式
    data = text.encode()

    #发送
    sock.sendto(data,('192.168.43.54',4444))

    #解码接受到的数据
    data = data.decode()

    print(data)

if __name__ == '__main__':
    clientFunc()
