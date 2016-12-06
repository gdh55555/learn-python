#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: spider.py )
#Mail: gdhe55555@gmail.com
#Created Time: 2016-12-05 16:33:41

#=====================================

import requests
from pyquery import PyQuery as Pq

class SegmentfaultQuestionSpider(object):

    def __init__(self, segmentfault_id):
        self.url = 'https://segmentfault.com/q/{0}'.format(segmentfault_id)
        self._dom = None

    @property
    def dom(self):
        if not self._dom:
            document = requests.get(self.url)
            document.encoding = 'utf-8'
            self._dom = Pq(document.text)
        return self._dom

    @property
    def title(self):
        return self.dom('h1#questionTitle').text()

    @property
    def content(self):
        return self.dom('.question.fmt').html()

    @property
    def answers(self):
        return list(answer.html() for answer in self.dom('.answer.fmt').items())

    @property
    def tags(self):
        return self.dom('ul.taglist--inline > li').text().split()

class SegmentfaultTagSpider(object):
    def __init__(self, tag_name, page=1):
        self.url = 'https://segmentfault.com/t/%s?type=newest&page=%s'%(tag_name, page)
        self.tag_name = tag_name
        self.page = page
        self._dom = None

    @property
    def dom(self):
        if not self._dom:
            document = requests.get(self.url)
            document.encoding = 'utf-8'
            self._dom = Pq(document.text)
            self._dom.make_links_absolute(base_url='http://segmentfault.com/')
        return self._dom

    @property
    def questions(self):
        return [question.attr('href') for question in self.dom('h2.title > a').items()]

    @property
    def has_next_page(self):
        return bool(self.dom('ul.pagination > li.next'))

    def next_page(self):
        if self.has_next_page:
            print(self.page)
            self.__init__(tag_name=self.tag_name, page = self.page+1)
        else:
            return None
