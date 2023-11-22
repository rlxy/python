from bs4 import BeautifulSoup       #网页选择器
import requests             #爬虫库
"""
代码思路：
    1 使用代码去打开书籍详情页，并返回详情页的所有数据
    2 请求成功拿到详情页数据后，做数据筛选
    3 文件操作  with open 去保存txt文本
"""
response= requests.get("http://www.biquw.com/book/94/").text

#Beautifulsoup 需要两个参数 1.筛选的网页 2.html解析库
soup = BeautifulSoup(response,'lxml')

"""
筛选数据的步骤 
    1 提取小说章节名称
    2 提取所有小说章节的a标签中的值，对主域名做字符拼接
    3 在小说内容页中提取小说内容
        小说内容页是一个单独的网页
        可以再次例用requests去请求这个网页
        请求成功之后  进一步的做筛选数据的步骤
"""

data_list = soup.find('ul')
for book in data_list.find_all("a"):
    print("{}:{}".format(book.text,"http://www.biquw.com/book/94/" + book['href']))
    book_url = "http://www.biquw.com/book/94/" + book['href']
    data_book = requests.get(book_url).text
    soup = BeautifulSoup(data_book,'lxml')
    data = soup.find('div',{'id':'htmlContent'}).text

    with open('./剑道独尊/' + book.text + '.text','w',encoding='utf-8') as f :
        f.write(data)