# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class FisRaces(Item):
    location = Field()
    id = Field()
    link = Field()
    date = Field()
    category = Field()
    genre = Field()
    info = Field()
    discipline = Field()


class FisRanking(Item):
    link = Field()
    info = Field()
    men = Field()
    women = Field()
