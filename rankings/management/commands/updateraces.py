#-*- coding: utf-8 -*-
import os
import shutil

from django.core.management.base import BaseCommand, CommandError
# from polls.models import Poll

# CURRENT_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
# BACKEND_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
# APP_DIR = os.path.abspath(os.path.join(BACKEND_DIR, os.pardir))
# WEBAPPS_DIR = os.path.abspath(os.path.join(APP_DIR, os.pardir))

CURRENT_DIR = '/home/tooski/webapps/python_core/python_core/rankings/'
BACKEND_DIR = '/home/tooski/webapps/python_core/python_core/'
APP_DIR = '/home/tooski/webapps/python_core/'
WEBAPPS_DIR = '/home/tooski/webapps/'
#
# CURRENT_DIR = '/home/seba-1511/Dropbox/Dev/tooski/python_core/rankings/'
# BACKEND_DIR = '/home/seba-1511/Dropbox/Dev/tooski/python_core/'
# APP_DIR = '/home/seba-1511/Dropbox/Dev/tooski/'
# WEBAPPS_DIR = '/home/seba-1511/Dropbox/Dev/tooski/'


class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):

# We get the leaderboard rankings and move them to the Apache server:
        os.system('cd ' + CURRENT_DIR +
                  '/fis/ && scrapy crawl ranking -o ranking.json -t json')
        # Testing:
        shutil.copy(CURRENT_DIR + '/fis/ranking.json',
                    WEBAPPS_DIR + '/website/ranking.json')
        # Server
        # shutil.copy(CURRENT_DIR + '/fis/ranking.json',
        #             WEBAPPS_DIR + '/website/ranking.json')

        # We should use the pipeline system of scrapy with the races.
        os.system('cd ' + CURRENT_DIR + '/fis/ && scrapy crawl races')
