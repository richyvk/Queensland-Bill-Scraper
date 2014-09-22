Queensland-Bill-Scraper
=======================
This very basic web scraper can be used to extract metadata about Bills that are current listed as "before the House" on the Quensland Parliament website.

Metadata that is extracted includes Bill name, URL, introducing member, stage, EN URL, and explanatory speech URL.

It is written using a framework called Scrapy which is written in Python.

To run Queensland Bill Scraper you need the following installed:

- Python 2.7
- PIP - recommended for installing Scrapy and LMXL
- Scrapy - https://scrapy.org
- lxml - http://lxml.de
- OpenSSL - preinstalled on Mac and Linux, no idea how to install it on Windows I'm afraid

To use Queensland Bill Scraper:

- Copy all files and folders to a local folder
- navigate to the local folder in your Terminal
- Type scrapy crawl qldbillscraper to run the scraper in your Terminal
- To dump scraped data to a file you can use scrapy crawl qldbillscraper -o followed by the file to save to, e.g. scrapy crawl qldbillscraper -o bills.json for a json file. file formats supported are json, csv and xml.

This is very much a work in progress, and will eventually be used as part of a larger project that I have planned. Further development of the scraper may happen, but may not depending on what I need.




