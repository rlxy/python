import socket
import time
def clientFunc():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    text = input('请输入你需要发送的信息：')
    data = text.encode()
    sock.sendto(data,('192.168.42.74',4444))
    data,addr = sock.recvfrom(500)
    text = data.decode()
    print(text)

    print(data)
if __name__ == '__main__':
    while True:
        try :
            print('客户端开启')
            clientFunc()
            print('消息发送成功')
        except Exception as e :
            print(e)
        time.sleep(1)