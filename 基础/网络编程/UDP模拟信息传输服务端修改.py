import socket
import time
def serverFunc():
    #1，建立socket
    sock =  socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    addr = ("192.168.42.74",6666)
    sock.bind(addr)
    data,addr = sock.recvfrom(500)
    text =  data.decode()
    print(text)
    rsp = input("请输入你要回复的消息：")
    data = rsp.encode()
    sock.sendto(data,addr)
if __name__ == '__main__' :
    while True :
        try :
            print('服务器启动，正在接受消息')
            serverFunc()
            print('发送成功')
        except Exception as e :
            print(e)
        time.sleep(1)