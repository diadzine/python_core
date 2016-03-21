# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import sys
from time import strptime, mktime
from rankings.models import Races


CURRENT_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
SCRAPY_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
MODULE_DIR = os.path.abspath(os.path.join(SCRAPY_DIR, os.pardir))
BACKEND_DIR = os.path.abspath(os.path.join(MODULE_DIR, os.pardir))
APP_DIR = os.path.abspath(os.path.join(BACKEND_DIR, os.pardir))
WEBAPPS_DIR = os.path.abspath(os.path.join(APP_DIR, os.pardir))

sys.path.append(BACKEND_DIR + '/')
sys.path.append(APP_DIR + '/')
sys.path.append(MODULE_DIR + '/')
sys.path.append(WEBAPPS_DIR + '/')
# os.environ['DJANGO_SETTINGS_MODULE'] = 'python_core.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'python_core.settings_server'


class FisPipeline(object):

    def process_item(self, item, spider):
        if spider.name not in ['races'] or int(item['id']) < 0:
            return item

        # Here we'll register the current item in the database:
        try:
            race = Races.objects.get(raceId=int(item['id']))
        except Races.DoesNotExist:
            race = Races()

        race.raceId = int(item['id'])
        race.info = item['info'].strip()
        race.category = item['category'].strip()
        race.genre = item['genre'].strip()
        race.link = item['link'].strip()
        race.location = item['location'].strip()
        race.discipline = item['discipline'].strip()
        race.raceId = item['id']
        race.table = item['table']
        race.date = mktime(strptime(item['date'].strip(), '%d.%m.%Y'))
        try:
            race.save()
        except:
            import pdb; pdb.set_trace()
        return item
