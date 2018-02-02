import scrapy
import uuid


class CnnScraper(scrapy.Spider):
    name = "cnn_spider"
    start_urls = [
        'https://www.cnn.com/2018/01/31/politics/nunes-memo-law-enforcement/index.html'
    ]

    def parse(self, response):
        
        #for quote in response.css('.l-container'):
        quote = response.css('.l-container').css('.pg-rail-tall__body')
        #print(quote.extract_first())
        if quote is None or len(quote) == 0:
            yield {

            }
        quote = quote[0]
        yield {
            'headline': quote.css('.el__leafmedia .el__leafmedia--sourced-paragraph::text').extract(),
            'body': quote.css('div.zn-body__paragraph::text').extract(),
            'tags': quote.css('div.tags a.tag::text').extract(),
        }

        text_file = open("cnn_data/" + str(uuid.uuid4()) + ".txt", "w")

        for words in quote.css('div.zn-body__paragraph::text').extract():
            text_file.write(words)

        text_file.close()

        NEXT_PAGE_SELECTOR = 'a ::attr(href)'
        next_pages = response.css(NEXT_PAGE_SELECTOR).extract()
        for next_page in next_pages:
            if 'cnn' in next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )

#quote2 = response.css('div.l-container')[1]
#title2 = quote2.css('div.l-container').extract()[3]
#article_body = response.css('div.l-container')[1].css('div.l-container').css('l-container::text').extract()[3]