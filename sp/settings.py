BOT_NAME = 'sp'
SPIDER_MODULES = ['sp.spiders']
NEWSPIDER_MODULE = 'sp.spiders'
ITEM_PIPELINES = {'sp.pipelines.Pipeline': 300}
COOKIES_ENBALE=False