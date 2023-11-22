#凯撒密码是一种替换加密的技术，明文中的所有字母都在字母表上向后（或向前）按照一个固定数目进行偏移后被替换成密文
#这里向后偏移了4位
import base64
str = 'e6Z9i~]8R~U~QHE{RnY{QXg~QnQ{^XVlRXlp^XI5Q6Q6SKY8jUAA'    #看最后的两个A =ascll码十进制为65，而A是61，猜测为凯撒密码和base64结合

text1=''
for i in str :
    t=chr(ord(i)-4)         #ord转换成 十进制  chr是返回当前整数对应的ascll字符
    text1+=t
print(base64.b64decode(text1))