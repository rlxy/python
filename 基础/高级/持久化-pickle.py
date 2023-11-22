#序列化（持久化，落地） ：把程序运行中的信息保存在磁盘上
#反序列化：序列号的逆过程
#pickle：python提供的序列化模块
#pickle.dump：序列化        #把信息存到某个文件里
#pickle.load：反序列化           #打印某个文件里面的信息
                #序列化案例
# import pickle
# age = 19
# with open(r'需要操作文件名','wb') as f :
#     pickle.dump(age,f)
# #反序列化
# import pickle
# with open(r'需要操作的文件名' , 'wb') as f :
#     age = pickle.load(f)
#     print(age)


#持久化 shelve
#持久化工具
#类似字典，用kv对保存数据，存取方式也和字典类似
#open  close
# import shelve
#使用shelve创建文件并使用
#打开文件
#shv相当于一个字典
# shv = shelve.open(r'shv.db')
# shv['one'] = 1
# shv['two'] = 2
# shv['three'] = 3
# shv.close()
#上面案例说明shelve自动创建的不仅仅是一个shv.db文件，还包括其他格式文件

#shelve读取案例
# shv = shelve.open(r'shv.db')
#
# print(shv['one'])
# print(shv['three'])


#shelve特性
#不支持多个应用并行写入
    #为了解决这个问题，open的时候可以使用flag = r
#写回问题
    # shelv一般情况下不会等待持久化对象进行任何修改
    # 解决方案：强制回写：writeback = true

# shelve 以只读打开
# import shelve
#
# shv = shelve.open(r'shv.db',flag='r')
#
# try:
#     k1 = shv['one']
#     print(k1)
# finally:
#     shv.close()



# import shelve
#
#
# shv = shelve.open(r'shv.db')
# try:
#     shv['one'] = {"eins":1,"zwei":2,"drei":3}
# finally:
#     shv.close()

# shv = shelve.open(r'shv.db')
# try:
#     one = shv['one']
#     print(one)
# finally:
#     shv.close()



# # shelve 使用强制写回

# import shelve

# shv = shelve.open(r'shv.db',flag='r')

# try:
#     k1 = shv['one']
#     print(k1)
#     # 此时，一旦shelve关闭，则内容还在内存中，没有回写数据库
#     k1["eins"] = 100
# finally:
#     shv.close()

# shv = shelve.open(r'shv.db')
# try:
#     one = shv['one']
#     print(one)
# finally:
#     shv.close()

# # shelve 使用强制写回
# import shelve

# shv = shelve.open(r'shv.db',writeback=True)
# try:
#     k1 = shv['one']
#     print(k1)
#     # 通过writeback 强制回写
#     k1["eins"] = 100
# finally:
#     shv.close()

# shv = shelve.open(r'shv.db')
# try:
#     one = shv['one']
#     print(one)
# finally:
#     shv.close()



# # shelve 使用with管理上下文环境

# with shelve.open(r'shv.db',writeback=True) as shv:
#     k1 = shv['one']
#     print(k1)
#     # 通过writeback 强制回写
#     k1["eins"] = 10000
# with shelve.open(r'shv.db') as shv:
#     print(shv['one'])




