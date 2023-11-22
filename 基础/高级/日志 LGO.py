# 日志相关概念
# 日志写在磁盘上，进行IO操作，写日志不要太频繁

# 日志级别（level）
    #不同用户关注不同的程序信息
    #DEBUG
    #INFO
    #NOTICE
    #WARNING
    #ERROR
    #CRITICAL
    #ALERT
    #EMERGENCY

# IO操作 =》 不要频繁操作

# LOG的作用
    # 调试
    # 了解软件的运行情况
    # 分析定位问题

# 日志信息
    # time ： 必须有
    # 地点 ： 那个类那个函数出现问题
    # level：问题级别
    # 内容：

# 成熟的第三方日志
    # log4j
    # log4php
    # logging


# logging模块
# 日志级别
    # 级别可自定义
    # DEBUG
    # INFO
    # WARNING
    # ERROR
    # CRITICAL

# 初始化／写日志实例需要制定级别，只有当级别等于或高于制定级别才能被记录
# 使用方法
    # 直接使用logging（封装了其他组件）
    # logging四大组件直接定制

# logging 模块级别的日记
# 使用以下几个函数
    # logging.debug(msg,*args,**kwargs) 创建一条严重级别为DEBUG的日志记录
    # logging.info(msg,*args,**kwargs) 创建一条严重级别为info的日志记录
    # logging.warning(msg,*args,**kwargs) 创建一条严重级别为warning的日志记录
    # logging.error(msg,*args,**kwargs) 创建一条严重级别为error的日志记录
    # logging.critical(msg,*args,**kwargs) 创建一条严重级别为critical的日志记录
    # logging.log(level,*args,**kwargs) 创建一条严重级别为level的日志记录
    # logging.basicConfig( **kwargs) 对root logger进行一次性配置


# logging.basicConfig( **kwargs)     对root logger进行一次性配置
    # 只在第一次调用的时候起作用
    # 不配置logger则使用默认值
        # 输出： sys.stderr
        # 级别： WARNING
        # 格式： level：log_name:content


import logging

# %（这里面的是参数）s   都是format的参数   asctime是显示错误的时间    levelname是显示错误级别的名称     message是打印下面logging.debug设置的字符串
LOG_FORMAT = '%(asctime)s====%(levelname)s====%(message)s'

#filename 创建一个文件，把日志存进去  level 设置什么级别的错误才写进日志
logging.basicConfig(filename="log.log",level=logging.DEBUG,format=LOG_FORMAT)
logging.debug('this is debug log')



# ## logging模块的处理流程
# - 四大组件
#     - 日志器（Logger）： 产生日志的一个接口
#     - 处理器（Handler）： 把产生的日志发送到相应的目的地
#     - 过滤器（Filter）：更精细的控制那些日志输出
#     - 格式器（Formatter）：对输出信息进行格式化
# - Logger
#     - 产生一个日志
#     - 操作
#         - Logger.setLevel() 设置日志器会处理日志消息的最低严重级别
#         - Logger.addHandler() 和 Logger.removeHandler 为该logger对象添加和移除一个处理器
#         - Logger.addFilter() 和 Logger.removeFilter() 为该logger对象添加和移除一个过滤器
#         - Logger.exception() 创建类似于Logger.error的日志消息
#         -Logger.log():获取一个明确的日志level参数类创建一个日志记录
#     - 如何得到一个logger对象
#         - 实例化
#         - logger.getLogger()
# - Handler
#     - 把log发送到指定的位置
#     - 方法
#         - setLevel 设计级别
#         - setFormat 设置格式
#         - addFilter,removeFilter 添加和移除一个过滤器
#     - 不要直接使用，handler是基类
#         - logging.StreamHandler 将日志消息发送到输出到Stram,如：std.out,std.err 或任何file-like对象。
#         - logging.FileHandler  将日志消息发送到磁盘文件，默认情况下文件大小会无限增长
#         - logging.handlers.RotatingFileHandler 将日志消息发送到磁盘文件，并支持日志文件按大小切割
#         - logging.handlers.TimedRotatingFileHandler 将日志消息发送到磁盘文件，并支持日志文件按时间切割
#         - logging.handlers.HTTPHandler 将日志消息以GET或POST的方式发送给一个HTTP服务器
#         - logging.handlers.SMTHandler 将日志消息发给一个指定的email 地址
#         - logging.NullHandler 该Handler实例会忽略error message，通常被象使用logging的library开发者使用
# - Format
#     - 直接实例化
#     - 可继承Format添加特殊内容
#     - 三个参数
#         - fmt: 指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
#         - datetime: 指定日期格式化字符串，如果部指定该参数则默认使用“%Y-%m-%d %H:%M:%S”
# - Filter类
#     - 可以被Handler和Logger 使用
#     - 控制传递过来的信息的具体内容
