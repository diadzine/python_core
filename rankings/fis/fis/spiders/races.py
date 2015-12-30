# -*- coding: utf-8 -*-
# Importing Django models

import os
import sys

CURRENT_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
SPIDERS_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
SCRAPY_DIR = os.path.abspath(os.path.join(SPIDERS_DIR, os.pardir))
MODULE_DIR = os.path.abspath(os.path.join(SCRAPY_DIR, os.pardir))
BACKEND_DIR = os.path.abspath(os.path.join(MODULE_DIR, os.pardir))
APP_DIR = os.path.abspath(os.path.join(BACKEND_DIR, os.pardir))
WEBAPPS_DIR = os.path.abspath(os.path.join(APP_DIR, os.pardir))

sys.path.append(BACKEND_DIR + '/')
sys.path.append(APP_DIR + '/')
sys.path.append(MODULE_DIR + '/')
sys.path.append(WEBAPPS_DIR + '/')
# For webfaction server:
sys.path.append('/home/tooski/webapps/python_core/lib/python2.7')
os.environ['DJANGO_SETTINGS_MODULE'] = 'python_core.settings'
# os.environ['DJANGO_SETTINGS_MODULE'] = 'python_core.settings_server'
from django.conf import settings

# Other imports
from scrapy.selector import Selector
from scrapy.spider import BaseSpider
from scrapy.http import Request

from fis.items import FisRaces
from rankings.models import Races
import logging


logger = logging.getLogger('spider')


class MyCrawlerSpider(BaseSpider):
    # nom du crawler à spécifier lors de l'exécution
    name = 'races'

    # domaine(s) sur le ou lesquels le crawler aura le droit d'aller
    allowed_domains = ['data.fis-ski.com']

    # Getting the last raceId we processed
    last_race = Races.objects.all().order_by('raceId').reverse().first()
    last_race = last_race.raceId if last_race else 0
    max_newsid = int(last_race)
    jump = 3000

    def start_requests(self):
        for i in xrange(self.max_newsid, self.max_newsid + self.jump):
            yield Request(
                'http://data.fis-ski.com/dynamic/'
                'results.html?sector=AL&raceid=%d' % i,
                callback=self.parse_item
            )

    def parse_item(self, response):
        hxs = Selector(response)
        item = FisRaces()
        url = response.url
        item['link'] = url
        item['id'] = url[url.index('raceid=') + 7:]

        try:
            item['date'] = hxs.xpath(
                '//div[contains(@class, "padding-content")]'
                '/h3/span/text()'
            ).extract()[0].strip()

            item['location'] = hxs.xpath(
                '//div[contains(@class, "padding-content")]'
                '/h3/a/text()'
            ).extract()[0].strip()

            info = hxs.xpath(
                '//div[contains(@class, "padding-content")]'
                '/div/div/h4/text()'
            ).extract()[0].strip()

        except IndexError:
            logger.warning('No data to parse on race #%s' % item['id'])
            return None

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

        tables = hxs.xpath(
            '//table[contains(@class, "footable table-datas '
            'table-withpadding")]'
        )

        place = (len(tables) - 1)
        item['table'] = tables.extract()[place].strip()

        if 'No results available' in item['table']:
            logger.warning('No result available for race #%s' % item['id'])
            return None

        return item
