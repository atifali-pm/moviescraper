# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviescraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass


class MovieItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    synopsis = scrapy.Field()
    streaming_charts =  scrapy.Field()
    rating =  scrapy.Field()
    genres = scrapy.Field()
    runtime = scrapy.Field()
    age_rating = scrapy.Field()
    production_country = scrapy.Field()
    director = scrapy.Field()
    casts = scrapy.Field()