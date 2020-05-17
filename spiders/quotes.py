from urllib.request import Request

import scrapy
from ..items import DemoProjectItem

class CodeSpider(scrapy.Spider):
    name = 'timeout-errback'
    custom_settings = {'DOWNLOAD_TIMEOUT': 3}
    name = "quotes"
    start_urls = ["https://taphaps.com/melissa-michael-mooneyhan-tornado/",
                'https://mashviral.com/democrats-gather-at-marquette-university/',
                "https://zodiac-horoscoop.nl/daghoroscoop/tweeling/",
                "https://www.prioritisemytravel.com/boxing-day-deal-book-a-disneyland-paris-break-from-only-199pp/",
                "https://newyear2020s.com/happy-valentines-day-2020/",
                "https://espanadiario.es/meteo/tiempo-espana-viernes-31-enero-2020",
                "https://baymorhouse.com/ogrod-na-trzecim-pietrze-czyli-jak-zaaranzowac-balkon/"]

    def parse(self, response):
        items = DemoProjectItem()
        base_url = response.url
        if response.status == 200:
            i=0
            present = response.xpath("//script[contains(., 'window._taboola')]").extract_first(default="not-found")
            if present == 'not-found':
                print("Not Exist")
                items["url"] = base_url
                yield items

            else:
                print("Exists")
                items["url"] = base_url
                yield items
        else:
            print("Url Not Found{}"+response.url)

    def errback(self, failure):
        self.logger.info('Handled by the errback: %s (%s exception)', failure.request.url, str(failure.value))
        return {'url': failure.request.url}


