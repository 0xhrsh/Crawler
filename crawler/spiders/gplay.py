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
        downloads = response.css('span.htlgb')
        downloads = downloads.css('span::text').getall()
        # for x in downloads:
        #     print("=======>",x)
        yield{
            'App Name': name.css('span::text').get(),
            'Updated': downloads[0],
            'Installs': downloads[4],
            # 'Reviews': reviews.css('span::text').get(),
        }
        next_app = response.css('div.wXUyZd a::attr(href)').get()
        if next_app is not None:
            next_app = response.urljoin(next_app)
            yield scrapy.Request(next_app, callback=self.parse)

            