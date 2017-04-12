# -*- coding: utf-8 -*-

import scrapy
import string
import random
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from dockerscraper.items import DockerscraperItem

from scrapy.http.request import Request


limit = 3

class DockerSpider(CrawlSpider):
    global limit
    name = "docker"
    allowed_domains = ["hub.docker.com"]
    def start_requests(self):
        self.flag = True
        start_url = 'https://hub.docker.com/search/?isAutomated=0&isOfficial=0&page=1&pullCount=10000&q=a&starCount=0'
        dic = open('/usr/share/dict/words','r')
        l = dic.readlines()
        rand_list = random.sample(range(1,len(l)),20000)
        for k in rand_list:
            j = l[k]
            genurls = start_url.split('q=a')
            genurl = genurls[0] + 'q=' + str(j) + genurls[1]
            limit = 3
            for i in range(1,limit):
                urls = genurl.split('page=1')
                yield Request(urls[0] + 'page=' + str(i) + urls[1])
                #if not self.flag:
                    #self.flag = True
                    #break
    def parse(self, response):
        global limit
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@class="RepositoryListItem__repoName___28cOR"]')
        items = []
        if len(sites) <=0:
            self.flag = False
        for site in sites:
		        item = DockerscraperItem()
		        item['name'] = site.extract().split('>')[1].split('<')[0]
		        items.append(item)
        if len(items)>0:
		    limit = limit + 1
        return items
