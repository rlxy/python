'''
Server端流程
    1，建立socket，socket是负责具体通信的一个实例
    2，绑定，为创建的socket指派固定的端口和ip地址
    3，接受对方发送内容
    4，给对方发送反馈，此步骤为非必须步骤
'''


#socket模块负责socket编程
import socket

#模拟服务器函数
def serverFunc():
    #1，建立socket

    #socket.AF_INET ： 使用ipv4 协议
    #socket.SOCK_DGRAM ： 使用UDP通信
    sock =  socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #2，绑定ip和port
    # 这个ip地址代表的是机器本身
    #随机选择端口  不行就换
    #地址是一个tuple类型，（ip,port）
    addr = ("192.168.43.54",6666)
    sock.bind(addr)

    #接受对方消息
    #等待方式只能等
    #recvfrom 接受的返回值是一个远足，前一项表示数据，后一项表示地址
    #参数的含义是缓冲区大小
    #rst = sock,recvfrom(500)     sock返回的是tuple类型，这样还不如直接用下面方法 直接返回给那两个变量
    data,addr = sock.recvfrom(500)  #recv是receive(接收)的缩写    data是对方给我发的消息


    #发送过来的数据是bytes格式，必须通过解码才能得到str格式内容
    text =  data.decode()       #decode默认utf-8格式
    print(text)


    #给对方返回的消息
    rsp = input("请输入你要发送的消息")

    #给对方发送的消息还需要转换成bytes格式，否则服务器看不懂
    data = rsp.encode()     #encode是编码  默认编码方式也是utf-8
    sock.sendto(data,addr)  #前面已经获取了对方的ip  这里发送数据过去


if __name__ == '__main__' :
    print('服务器启动，准备发送信息')
    serverFunc()
    print('发送成功，结束服务器')
























