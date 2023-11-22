scrapy文档(https://doc.scrapy.org/en/latest/)

- scrapy包含各个部件：
    - scrapyEngine:核心部件，引擎,总指挥：负责数据和信号在不同模块间的传递
    - scheduler调度器：一个队列，存放引擎发过来的request请求
    - Downloader下载器：把引擎发来的request发出请求，得到response并返回给引擎
    - Spider爬虫：处理引擎发来的response，提取数据，提取url，并交给引擎
    - ItemPipeline管道:处理引擎发过来的item(数据)，比如存储
    - DownloaderMiddleware下载中间件：自定义的下载的功能或组件，比如有时候我们需要把header伪装一下
    - SpiderMiddleware爬虫中间件：对spider进行扩展，可以自定义requests请求和进行response过滤
- 模拟爬虫项目流程
    - 创建一个scrapy项目：scrapy startproject xxx
    - 生成一个爬虫：scrapy genspider itcast "itcast.cn"
    - 提取数据：完善spider，使用xpath,re等方式进行过滤
    - 保存数据：pipeline中保存数据
    