import scrapy


class CategorySpider(scrapy.Spider):
    name = "category"

    def start_requests(self):
        urls = [
            'https://www.n11.com/mutfak-gerecleri/yemek-pisirme?q=g%C3%BClsan'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for col_div in response.css('li.column'):

            yield {
                'product_id': col_div.css('div.pro a::attr(data-id)').get(),
                'product_name': col_div.css('div.pro a::attr(title)').get(),
                'product_link': col_div.css('div.pro a::attr(href)').get(),
                'seller_link': col_div.css('a.sallerInfo::attr(href)').get(),
                'seller_name': col_div.css('a.sallerInfo span.sallerName::text').get(),

            }

        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)


