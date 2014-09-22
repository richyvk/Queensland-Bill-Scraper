import scrapy
from qld_bill_scraper.items import QldParlBill

class QldBillSpider(scrapy.Spider):
    name = "qldbillscraper"
    allowed_domains = ["http://www.parliament.qld.gov.au/"]
    start_urls = [
        "http://www.parliament.qld.gov.au/work-of-assembly/bills-and-legislation/Bills-before-the-House"
    ]
    
    def parse(self, response):
        for sel in response.xpath('//div[@class="bill"]'):
            item = QldParlBill()
            item['billName'] = sel.xpath('div[@class="bill-title"]/h4/a/text()').extract()
            item['billUrl'] = sel.xpath('div[@class="bill-title"]/h4/a/@href').extract()
            item['billIntroBy'] = sel.xpath('div[@class="bill-info"]/p/strong/text()').extract()
            item['billStage'] = sel.xpath('div[@class="bill-info"]/p/text()[2]').extract()
            item['billEnUrl'] = sel.xpath('div[@class="bill-docs"]/p/a[2]/@href').extract()
            item['billExpSpeechUrl'] = sel.xpath('div[@class="bill-docs"]/p/a[3]/@href').extract()
            yield item