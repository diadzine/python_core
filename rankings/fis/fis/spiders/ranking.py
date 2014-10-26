# -*- coding: utf-8 -*-
from scrapy.selector import Selector

from scrapy.spider import BaseSpider
from scrapy.http import Request

from fis.items import FisRanking


class RankingSpider(BaseSpider):
    # nom du crawler à spécifier lors de l'exécution
    name = 'ranking'

    # domaine(s) sur le ou lesquels le crawler aura le droit d'aller
    allowed_domains = ['www.fis-ski.com']

    def start_requests(self):
        # When saving, the file should be moved to the root of /website.
        # So that the js can parse, it is directly served by Apache and doesn't
        # require connection to th DB. Use shutil.copy(src, dest)
        yield Request('http://www.fis-ski.com/alpine-skiing/leader-board/',
                      callback=self.parse_item)

    def parse_item(self, response):
        hxs = Selector(response)
        item = FisRanking()
        item['link'] = response.url

        rows = hxs.xpath('//div[contains(@class, "dcm-leaderBoard")]//tr')
        men = []
        women = []
        men_flag = False
        previous_row = 0
        for row in rows:
            name = row.xpath(
                'td/div/a/span[contains(@class, "dcm-athName")]/text()').extract()
            country = row.xpath(
                'td/div/div[contains(@class, "dcm-noc")]/text()').extract()
            row = row.xpath('td/text()').extract()
            if row and int(row[0]) <= 25:
                place = row[0]
                score = row[2]
                name = name[0]
                country = country[0]
                if int(row[0]) < previous_row:
                    men_flag = True
                previous_row = int(row[0])
                if men_flag:
                    men.append([place, name, country, score])
                else:
                    women.append([place, name, country, score])

        item['men'] = men
        item['women'] = women
        return item
