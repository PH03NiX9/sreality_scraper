import scrapy
import json


class SrealitySpider(scrapy.Spider):
    name = "srealityspider"
    allowed_domains = ["sreality.cz"]

    def start_requests(self):
        base_url = "https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&page="
        total_listings = 0
        page = 1

        while total_listings < 500 and page <= 20:
            url = base_url + str(page)
            yield scrapy.Request(url, callback=self.parse)
            page += 1

    def parse(self, response):
        data = json.loads(response.body)
        items = data["_embedded"]["estates"]
        for item in items[:500]:
            title = item["name"]
            images = item.get("_links", {}).get("images", [])
            image_urls = [image["href"] for image in images]

            yield {
                'title': title,
                'image_urls': image_urls
            }
