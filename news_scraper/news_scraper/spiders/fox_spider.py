import scrapy
import uuid

class FoxSpider(scrapy.Spider):
    name = "fox_spider"
    start_urls = [
        'http://www.foxnews.com/politics/2018/02/02/grave-concerns-about-nunes-memo-revealing-sources-methods-appear-unfounded.html'
    ]

    def parse(self, response):
        
        #for quote in response.css('.l-container'):
        quote = response.css('.article-body')
        print(quote.extract_first())
        quote = quote[0]
        yield {
            'headline': quote.css('.el__leafmedia .el__leafmedia--sourced-paragraph::text').extract(),
            'body': response.css('.article-body p::text').extract(),
            'tags': quote.css('div.tags a.tag::text').extract(),
        }

        text_file = open("fox_data/" + str(uuid.uuid4()) + ".txt", "w")

        for words in response.css('.article-body p::text').extract():
            text_file.write(words)

        text_file.close()

        NEXT_PAGE_SELECTOR = 'a ::attr(href)'
        next_pages = response.css(NEXT_PAGE_SELECTOR).extract()
        for next_page in next_pages:

            if 'fox' in next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )

#quote2 = response.css('div.l-container')[1]
#title2 = quote2.css('div.l-container').extract()[3]
#article_body = response.css('div.l-container')[1].css('div.l-container').css('l-container::text').extract()[3]