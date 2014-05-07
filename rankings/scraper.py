# -*- coding: utf-8 -*-
import os
import shutil

CURRENT_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
BACKEND_DIR = os.path.abspath(os.path.join(CURRENT_DIR, os.pardir))
APP_DIR = os.path.abspath(os.path.join(BACKEND_DIR, os.pardir))
WEBAPPS_DIR = os.path.abspath(os.path.join(APP_DIR, os.pardir))

# We get the leaederboard rankings and move them to the Apache server:
os.system('cd ' + CURRENT_DIR +
          '/fis/ && scrapy crawl ranking -o ranking.json -t json')
shutil.copy(CURRENT_DIR + '/fis/ranking.json',
            WEBAPPS_DIR + '/website/ranking.json')

# We should use the pipeline system of scrapy with the races.
os.system('cd ' + CURRENT_DIR + '/fis/ && scrapy crawl races')
