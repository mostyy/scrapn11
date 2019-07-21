import scrapy


class CategorySpider(scrapy.Spider):
    name = "category"

    def start_requests(self):
        urls = [
            'https://www.n11.com/mutfak-gerecleri'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('li.column'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }

        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

        # for quote in response.css('li.subCatMenuItem a'):
        #     print(quote)
        #     yield {
        #         'link': quote.attrib['href'],
        #         'title': quote.attrib['title'],
        #     }

