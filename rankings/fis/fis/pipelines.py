# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import sys
CURRENT_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
SCRAPY_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
MODULE_DIR = os.path.abspath(os.path.join(SCRAPY_DIR, os.pardir))
BACKEND_DIR = os.path.abspath(os.path.join(MODULE_DIR, os.pardir))
WEBAPPS_DIR = os.path.abspath(os.path.join(BACKEND_DIR, os.pardir))

sys.path.append(BACKEND_DIR)
sys.path.append(MODULE_DIR)
sys.path.append(WEBAPPS_DIR)
print BACKEND_DIR
# os.environ['PYTHONPATH'] = BACKEND_DIR
os.environ['DJANGO_SETTINGS_MODULE'] = 'python_core.settings'

from rankings.models import Races


class FisPipeline(object):

    def process_item(self, item, spider):
        if spider.name not in ['races']:
            return item

        # Here we'll register the current item in the database:
        race = Races()
        race.info = item['info']
        race.category = item['category']
        race.genre = item['genre']
        race.link = item['link']
        race.location = item['location']
        race.discipline = item['discipline']
        race.raceId = item['id']
        race.table = item['table']
        race.date = item['date']
        race.save()
        return item
