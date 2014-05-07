# -*- coding: utf-8 -*-
from scrapy.selector import Selector

from scrapy.spider import BaseSpider
from scrapy.http import Request

from fis.items import FisRaces


class MyCrawlerSpider(BaseSpider):
    # nom du crawler à spécifier lors de l'exécution
    name = 'races'

    # domaine(s) sur le ou lesquels le crawler aura le droit d'aller
    allowed_domains = ['data.fis-ski.com']

    # We'll save this kind of variable in a pickle file and load it each time.
    max_newsid = 16015

    def start_requests(self):
        for i in xrange(16000, self.max_newsid):
            yield Request(
                'http://data.fis-ski.com/dynamic/results.html?sector=AL&raceid=%d' % i,
                callback=self.parse_item)

    def parse_item(self, response):
        # TODO: Save the table in json/string format as a variable of item.
        hxs = Selector(response)
        item = FisRaces()
        url = response.url
        item['link'] = url
        item['id'] = url[url.index('raceid=') + 7:]
        item['date'] = hxs.xpath(
            '//div[contains(@class, "padding-content")]/h3/span/text()').extract()[0].strip()
        item['location'] = hxs.xpath(
            '//div[contains(@class, "padding-content")]/h3/a/text()').extract()[0].strip()

        info = hxs.xpath(
            '//div[contains(@class, "padding-content")]/div/div/h4/text()').extract()[0].strip()
        item['info'] = info
        item['genre'] = 'H' if 'Men' in info else 'F'

        if 'World Cup' in info:
            item['category'] = 'WC'
        elif 'European Cup' in info:
            item['category'] = 'EC'
        elif 'FIS Race' in info:
            item['category'] = 'FIS'
        elif 'Citizen' in info:
            item['category'] = 'CIT'
        elif 'National Junior' in info:
            item['category'] = 'NJR'
        elif 'Junior' in info:
            item['category'] = 'JR'
        else:
            item['category'] = 'Other'

        if 'Giant Slalom' in info:
            item['discipline'] = 'GS'
        elif 'Downhill' in info:
            item['discipline'] = 'DH'
        elif 'Slalom' in info:
            item['discipline'] = 'SL'
        elif 'Super G' in info:
            item['discipline'] = 'SG'
        elif 'Super Combined' in info:
            item['dicipline'] = 'SC'
        else:
            item['discipline'] = 'Other'

        item['table'] = hxs.xpath(
            '//table[contains(@class, "footable table-datas table-withpadding")]').extract()[2].strip()

        return item
