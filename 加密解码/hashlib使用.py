import hashlib
'''
它是一种算法，称为hash算法，散列算法，摘要算法，他能把任意长度的二进制数据转化位固定长度的数据
他不可反解，但是可以通过撞库来破解
'''
import hmac

#加密算法虽然厉害，但有时候存在缺陷，通过撞库可以反解，所以有必要对加密算法中添加自定义key再来做加密
hashmd5 = hashlib.md5('salt'.encode('utf-8'))   #加密
print('md5:',hashmd5.hexdigest())
hashmd5.update('password'.encode('utf-8'))  #password通过哈希算法得出一个16进制的32位数字
print('md5:',hashmd5.hexdigest())      #打印这个32位数字

hashsha1 = hashlib.sha1('salt'.encode('utf-8'))
print('sha1:',hashsha1.hexdigest())
hashsha1.update('password'.encode('utf-8'))
print('sha1:',hashsha1.hexdigest())

hashsha224 = hashlib.sha224('salt'.encode())
print('hashsha224:',hashsha224.hexdigest())
hashsha224.update('password'.encode())
print('hashsha224:',hashsha224.hexdigest())

hashsha256 = hashlib.sha224('salt'.encode())
print('hashsha256:',hashsha256.hexdigest())
hashsha256.update('password'.encode())
print('hashsha256:',hashsha256.hexdigest())



hmacobj = hmac.new('salt'.encode())
print('hmacobj：',hmacobj.hexdigest())
hmacobj.update('password'.encode())
print('hmacobj：',hmacobj.hexdigest())




def testhash(obj):
    hsobj = hashlib.md5()
    import os
    if os.path.isfile(obj):
        fobj = open(obj, "rb")
        while True:
            block = fobj.read(2048)
            if not block:
                break
            hsobj.update(block)
    else:
        hsobj.update(obj.encode())
    return hsobj.hexdigest()

m = testhash("filepath or string")
print(m)





