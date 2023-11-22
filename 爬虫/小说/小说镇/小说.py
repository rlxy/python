import urllib.request
from bs4 import BeautifulSoup
import re

response = urllib.request.urlopen("https://www.xs7.org/book/111_111610/")
response = response.read()
response = response.decode("gbk")

soup = BeautifulSoup(response,'lxml')
data_list = soup.find('tbody')

for i in data_list.find_all("a"):
    print("{}:{}".format(i.text,"https://www.xs7.org/book/111_111610/"+ i['href']))
    book_url = "https://www.xs7.org/book/111_111610/"+ i['href']
    data_book = urllib.request.urlopen(book_url)
    data_book = data_book.read().decode("gbk")
    soup = BeautifulSoup(data_book, 'lxml')
    data = soup.find('div',{'id':'content'}).text

    with open("./财运天降/" + i.text + ".text",'w',encoding='utf-8') as f :
        f.write(data)



