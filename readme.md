# News Scraper (Nunes Memo)

Based on the Scrapy library, these two spiders are built to collect information from CNN and FOX (respectively). The data is stored in text files, and then the second portion of the code visualizes this data.

## Getting Started

<TODO>

### Prerequisites


### Installing

Install the wordcloud generator:

repo: https://github.com/amueller/word_cloud
pip install wordcloud


## About

### Goals

### Tests

I did a test, starting with two different articles for CNN and Fox, each focused on the nunes memo. The spiders start at their respective articles, and then begins crawling to links on that page that link to the respective domain of the initial article. This way I can jump through any recommended articles without having to code too much intelligence. There is an issue of articles being over represented, and it would be good to add a portion that tests if data has already been scraped.

### CNN WordCloud

![alt text](https://raw.githubusercontent.com/samcrane8/news-crawler/master/cnn_wordcloud.png)

### Fox WordCloud

![alt text](https://raw.githubusercontent.com/samcrane8/news-crawler/master/fox_wordcloud.png)

## Crawl Statistics

### Speed

This portion will show the speed at which this webcrawler is reading articles.
    
| Site | Time Elapsed (1 minute) |
| ------------- | ------------- |
| CNN | 295 pgs.  |
| FOX  | 458 pgs. |

## Authors

* **Sam Crane** 

## License

I haven't set up a license yet. I will get around to it!


## Acknowledgments

* Inspired by having to do an assignment for CS4675 at Georgia Tech on webscrapers.
