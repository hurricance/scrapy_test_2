import scrapy
from scrapy.http import Request
from sp.items import Information

class Spider(scrapy.Spider):
    name = "info" #爬虫的名字是new
    allowed_domains = ["bj.fang.lianjia.com"] #允许爬取的网站域名
    custom_settings = {
        'ITEM_PIPELINES' : {'sp.pipelines.Pipeline' : 300},
    }
    start_urls = ["https://bj.fang.lianjia.com/loupan/pg3/"]
    pagenum = 3
    def parse(self, response):
        self.pagenum += 1
        item = Information() #生成一个在items.py中定义好的Myitem对象,用于接收爬取的数据
        for each in response.xpath('/html/body/div[3]/ul[2]/li[*]'):
            item['region'] = each.xpath('div/div[2]/span[1]/text()').extract()
            item['unit_price'] = each.xpath('div/div[6]/div[1]/span[1]/text()').extract()
            item['total_price'] = each.xpath('div/div[6]/div[2]/text()').extract()
            yield(item) #返回item数据给到pipelines模块

        if self.pagenum < 8:
            url = f"https://bj.fang.lianjia.com/loupan/pg{self.pagenum}/"
            url = response.urljoin(url)
            yield Request(url, callback=self.parse)
