import scrapy


class GplaySpider(scrapy.Spider):
    name = "gplay"
    inside = {}

    def start_requests(self):
        seed = input("\n\n\nEnter Seed URL : ")
        print("processing for", seed, ".....\n\n")
        urls = [seed]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        name = response.css('h1.AHFaub')
        downloads = response.css('span.htlgb')
        downloads = downloads.css('span::text').getall()
        rating = response.css('div.BHMmbe')
        adds = response.css('div.bSIuKf')
        genre = response.css('span.T32cc.UAO9ie')

        try:
            x = self.inside[name.css('span::text').get()]

        except:
            self.inside[name.css('span::text').get()] = 1
            yield{
                'App Name': name.css('span::text').get(),
                'Last Updated': downloads[0],
                'Installs': downloads[4],
                'Ratings': rating.css('div::text').get(),
                'Ads': adds.css('div::text').get(),
                'Genre': genre.css('a::text').getall()[1],
            }
            next_app = response.css('div.wXUyZd a::attr(href)').getall()
            for app in next_app:
                if app is not None:
                    app = response.urljoin(app)
                    yield scrapy.Request(app, callback=self.parse)
