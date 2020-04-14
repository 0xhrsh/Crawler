import scrapy


class GplaySpider(scrapy.Spider):
    name = "gplay"

    def start_requests(self):
        urls = ['https://play.google.com/store/apps/details?id=com.google.android.apps.docs']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        name = response.css('h1.AHFaub')
        yield{
            'app name': name.css('span::text').get(),
        }
        next_app = response.css('div.wXUyZd a::attr(href)').get()
        if next_app is not None:
            next_app = response.urljoin(next_app)
            yield scrapy.Request(next_app, callback=self.parse)

            