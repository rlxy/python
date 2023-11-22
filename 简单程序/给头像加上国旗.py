"""
Filename: 给头像加上国旗.py
Author: 药药
Contact: 1579954422@qq.com
introduce：给一个头像的左下角增加一个国旗标志
"""
from PIL import Image
#读取图片
flag = Image.open('flag.png')   #国旗
head = Image.open('head.jpg')   #头像
#计算缩放比例
print(head.width)   #头像的宽640
print(flag.width)   #国旗的宽640
ratio = head.width/flag.width/4     #640/640/4=0.25
print(ratio)    #比例0.25
size = (int(flag.width*ratio),int(flag.height*ratio))   #国旗宽640*0.25=160，国旗高426*0.25=106
print(size)     #计算出了国旗的大小
#缩放国旗图片
flag = flag.resize(size,Image.ANTIALIAS)    #resize是改变图片大小
#计算坐标
position = (head.width-flag.width,head.height-flag.height)
#合成图片并保存
head.paste(flag,position)
head.save('head_flag.jpg','jpeg')   #save 保存