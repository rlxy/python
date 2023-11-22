import os
from time import time
import requests
from bs4 import BeautifulSoup   #筛选数据
from queue import Queue     #队列，保证信息在多线程间安全交换
from threading import Thread


class DownloadBiaoqingbao(Thread):
    #重写构造函数
    def __init__(self,queue,path):
        Thread.__init__(self)
        #声明类属性
        self.queue = queue
        self.path = path

        if not os.path.exists(path) :
            os.makedirs(path)
    def run(self):
        while True :
            url = self.queue.get()

            try:
                download_biaoqingbaos(url,self.path)
            finally:
                #后续调用告诉队列 任务处理是完整的
                self.queue.task_done()

#用于下载表情包的函数
def download_biaoqingbaos(url,path):
    #url = 'https://fabiaoqing.com/biaoqing/lists/page/1.html'
    response = requests.get(url)    #发送请求
    #使用网页选择器对放回的html去做数据筛选 lxml：html解析库
    soup = BeautifulSoup(response.content,'lxml')
    img_list = soup.find_all('img',class_='ui image lazy')


    for img in img_list :
        image = img.get("data-original")
        title = img.get("title")
        print('{}:{}'.format(title,image))

# url = "https://fabiaoqing.com/biaoqing/lists/page/1.html"
# download_biaoqingbaos(url)

        try:
            with open(path + title + os.path.splitext(image)[-1],'wb') as f :
                img = requests.get(image).content
                f.write(img)
        except OSError :
            print('文件写入错误....')
            break

if __name__ == '__main__':
    start = time()
    #构建url
    _url = 'https://fabiaoqing.com/biaoqing/lists/page/{page}.html'
    urls = [_url.format(page=page) for page in range(1,201)]
    queue = Queue()
    path = '../图片'

    #创建线程
    for x in range(10) :
        worker = DownloadBiaoqingbao(queue,path)
        #设置守护进程
        worker.daemon = True
        worker.start()

    #加入队列
    for url in urls :
        queue.put(url)

    #实际意义是等到队列为空，在执行其他操作
    queue.join()
    print('下载完成，总耗时：',time() - start)