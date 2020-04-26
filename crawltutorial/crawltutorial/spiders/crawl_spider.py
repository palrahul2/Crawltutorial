import scrapy
from ..items import CrawltutorialItem

class crawlSpider(scrapy.Spider):
    name = 'crawls'
    start_urls = [
        'https://www.imdb.com/list/ls068010962/?sort=list_order,asc&mode=detail&page=1'
    ]

    def parse(self, response):
        items = CrawltutorialItem()

        all_div_crawls = response.css('div.mode-detail')
        for crawls in all_div_crawls:
            actorname =crawls.css('.lister-item-header a::text')[0].extract().strip()
            actorname = [actorname]
            per_traits = crawls.css('.text-small+ p::text')[0].extract().strip()
            per_traits = [per_traits]
            actor_img = crawls.css('img').xpath('@src').extract()
            items['actorname'] = actorname
            items['per_traits'] = per_traits
            items['actor_img'] = actor_img
            #yield {'actorname': actorname, 'per_traits': per_traits, 'actor_img': actor_img}

            yield items




