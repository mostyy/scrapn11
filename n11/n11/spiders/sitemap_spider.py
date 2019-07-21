import scrapy


class SitemapSpider(scrapy.Spider):
    name = "sitemap"

    def start_requests(self):
        urls = [
            'https://www.n11.com/site-haritasi/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('li.subCatMenuItem a'):
            print(quote)
            yield {
                'link': quote.attrib['href'],
                'title': quote.attrib['title'],
            }

    def parse_(self, response):
        page = response.url.split("/")[-2]
        filename = 'sitemap-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)