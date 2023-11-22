import hashlib              #这个模块提供字符加密功能，将md5和sha模块整合到了一起，支持md5，sha1，sha224，sha256，sha3等算法


string = 'jiami'

md5 = hashlib.md5()
md5.update(string.encode('utf-8'))              #如果直接加密字符串他会报错，所以需要先用encode来进行转码
res = md5.hexdigest()
print('md5加密结果：',res)


sha1 = hashlib.sha1()
sha1.update(string.encode('utf-8'))               #sha1.update()  是用来更新哈希对象以字符串参数
res = sha1.hexdigest()                              ##digest()返回摘要，作为二进制数据字符串值
print('sha1加密结果：',res)


sha256 = hashlib.sha256()
sha256.update(string.encode('utf-8'))
res = sha256.hexdigest()                            ##hexdijgest()返回摘要，作为十六进制数据字符串
print('sha256加密结果：',res)


sha384 = hashlib.sha384()
sha384.update(string.encode('utf-8'))
res = sha384.hexdigest()
print('sha384加密结果：',res)


sha512 = hashlib.sha512()
sha512.update(string.encode('utf-8'))
res = sha512.hexdigest()
print('sha512加密结果：',res)


#如果同一个hash对象重复调用该犯法，则m.m.update(b)等效于m.update(a+b)



#上面的加密方法还存在缺陷，通过撞库可以反解，所以，有必要对加密算法中自定义key在来做加密

low = hashlib.md5()
low.update('ad'.encode('utf-8'))
res = low.hexdigest()
print('普通加密：',res)

high = hashlib.md5(b'beyondjie')
high.update('ad'.encode('utf-8'))
res = high.hexdigest()
print('采用key加密：',res)
























