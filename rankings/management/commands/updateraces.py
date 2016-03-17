#-*- coding: utf-8 -*-
import os
import shutil

from django.core.management.base import BaseCommand, CommandError


WEBAPPS_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '..', '..', '..', '..'
    )
)
RANKINGS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'fis')
)
WEBSITE_DIR = os.path.join(WEBAPPS_DIR, 'website')

FIS_RANKING_PATH = os.path.join(RANKINGS_DIR, 'ranking.json')
WEBSITE_RANKING_PATH = os.path.join(WEBSITE_DIR, 'ranking.json')


class Command(BaseCommand):
    args = 'None'
    help = 'Updates the table to the latest races, directly scrapped from the FIS website.'

    def handle(self, *args, **options):
        try:
            os.remove(WEBSITE_RANKING_PATH)
            os.remove(FIS_RANKING_PATH)
        except OSError:
            pass

        # We get the leaderboard rankings and move them to the Apache server:
        os.chdir(RANKINGS_DIR)
        os.system('scrapy crawl ranking -o ranking.json -t json')
        try:
            shutil.copy(FIS_RANKING_PATH, WEBSITE_RANKING_PATH)
        except IOError:
            print 'File ranking.json is missing'
        os.system('scrapy crawl races')
