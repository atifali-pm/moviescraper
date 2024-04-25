import scrapy

from moviescraper.items import MovieItem


class MoviespiderSpider(scrapy.Spider):
    name = "moviespider"
    allowed_domains = ["www.justwatch.com"]
    start_urls = ["https://www.justwatch.com/in/movies/"]

    def parse(self, response):
        movies = response.css('div .title-list-grid__item')

        for movie in movies:
            relative_url = movie.css('a').attrib['href']
            movie_url = 'https://www.justwatch.com' + relative_url

            yield response.follow(movie_url, callback=self.parse_movie_page)

    def parse_movie_page(self, response):

      
        subheading_values = response.css('div.detail-infos div.detail-infos__value')

        # casts = response.css('div.title-credits__actor')
        # cast = casts[0].css("::text").get() + ", " + casts[1].css("::text").get() + ", "+ casts[2].css("::text").get() + ", "+ casts[3].css("::text").get() + ", "+ casts[4].css("::text").get() + ", "+ casts[5].css("::text").get() + ", "+ casts[6].css("::text").get()


        # yield {
        #     'url' : response.url,
        #     'title' : response.css('div .title-block h1 ::text').get(),
        #     'synopsis': response.css('p.text-wrap-pre-line ::text').get(),
        #     'streaming_charts': subheading_values[0].css("::text").get(),
        #     'rating': subheading_values[1].css("::text").get(),
        #     'genres': subheading_values[2].css("::text").get(),
        #     'runtime': subheading_values[3].css("::text").get(),
        #     'age_rating': subheading_values[4].css("::text").get(),
        #     'production_country': subheading_values[5].css("::text").get(),
        #     'director': subheading_values[6].css("::text").get(),
        #     'casts': cast,
        # }

        casts = response.css('div.title-credits__actor')
        # cast = casts[0].css("::text").get() + ", " + casts[1].css("::text").get() + ", "+ casts[2].css("::text").get() + ", "+ casts[3].css("::text").get() + ", "+ casts[4].css("::text").get() + ", "+ casts[5].css("::text").get() + ", "+ casts[6].css("::text").get()

        movie_item = MovieItem()

        movie_item['url'] = response.url
        movie_item['title'] = response.css('div .title-block h1 ::text').get()
        movie_item['synopsis'] = response.css('p.text-wrap-pre-line ::text').get()
        movie_item['streaming_charts'] = subheading_values[0].css("::text").get()
        movie_item['rating'] = subheading_values[1].css("::text").get()
        movie_item['genres'] = subheading_values[2].css("::text").get()
        movie_item['runtime'] = subheading_values[3].css("::text").get()
        movie_item['age_rating'] = subheading_values[4].css("::text").get()
        movie_item['production_country'] = subheading_values[5].css("::text").get()
        movie_item['director'] = subheading_values[6].css("::text").get()
        movie_item['casts'] = casts[0].css("::text").get()

        yield movie_item
        

