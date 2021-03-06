# -*- coding: utf-8 -*-

# 工程名
BOT_NAME = 'template'
SCRAPY_NAME = 'template'

# 爬虫位置
SPIDER_MODULES = ['template.spiders']
NEWSPIDER_MODULE = 'template.spiders'

# 项目基本配置
# ALLOWED_DOMAINS = ""
# BASE_URL = ""

# chrome://version/  查看用户代理信息，模拟浏览器发送请求
#USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'

# 爬虫爬取的深度
#DEPTH_LIMIT = 4

# 延时设置
#DOWNLOAD_DELAY = 3

# 解析的编码设置，可以在获取的html文档中的meta标签的charset属性获取
#FEED_EXPORT_ENCODING = 'utf-8'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# mongodb数据库配置
#MONGO_HOST = "localhost"  # 主机IP
#MONGO_PORT = 25916  # 端口号
#MONGO_DB = "test_python"  # 库名
#MONGO_COLL = "douban-music"  # collection名
# 数据库如果需要登陆的话
#MONGO_USER = "zhangsan"
#MONGO_PSW = "123456"

# 项目中pipeline的路径及其启动顺序，会对每一个item在pipeline中执行
#ITEM_PIPELINES = {'template.pipelines.testPipeline': 300}

# --------------------  分隔符  ------------------------------------

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
