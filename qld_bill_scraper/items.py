import scrapy

# defining scrapy item for a Queensland Bill

class QldParlBill(scrapy.Item):
    # defining Bill metadata that is scraped
    billName = scrapy.Field()
    billUrl = scrapy.Field()
    billIntroBy = scrapy.Field() #Introducing member
    billStage = scrapy.Field()
    billEnUrl = scrapy.Field() #Explanatory note URL
    billExpSpeechUrl = scrapy.Field() #Introductory speech URL
    pass
