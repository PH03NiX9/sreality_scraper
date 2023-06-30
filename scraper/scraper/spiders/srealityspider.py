import scrapy


class SrealityspiderSpider(scrapy.Spider):
    name = "srealityspider"
    allowed_domains = ["sreality.cz"]
    start_urls = ["https://sreality.cz"]

    def parse(self, response):
        pass
