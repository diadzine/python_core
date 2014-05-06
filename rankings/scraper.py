# -*- coding: utf-8 -*-
import os
# from rankings.models import Races

os.system('cd ./fis/ && scrapy crawl ranking -o ranking.json -t json')
