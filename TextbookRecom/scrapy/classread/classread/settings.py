BOT_NAME = 'classread'

SPIDER_MODULES = ['classread.spiders']
NEWSPIDER_MODULE = 'classread.spiders'

ITEM_PIPELINES = {
    'classread.pipelines.ClassreadPipeline': 30,
    'classread.pipelines.DBPipeline': 100,
    # 'classread.pipelines.DangDownLoadPipeline': 300
}

MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'tbook'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'root'