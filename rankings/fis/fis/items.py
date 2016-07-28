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
    table = Field()

    # def __repr__(self):
    #     """only print out few data after exiting the Pipeline"""
    #     return repr({
    #         "id": self["id"],
    #         "category": self["category"],
    #         "date": self["date"],
    #         "discipline": self["discipline"],
    #         "genre": self["genre"],
    #         "info": self["info"],
    #         "location": self["location"],
    #         "link": self["link"],
    #     })


class FisRanking(Item):
    id = Field()
    link = Field()
    info = Field()
    men = Field()
    women = Field()
