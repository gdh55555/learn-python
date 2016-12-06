#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: spider.py )
#Mail: gdhe55555@gmail.com
#Created Time: 2016-12-06 09:01:47

#=====================================

from sfspider import spider
from python_spider.web.models import Answer, Question, Tag

class ContentSpider(spider.SegmentfaultQuestionSpider):

    def save(self):
        sf_id = self.url.split('/')[-1]
        tags = [Tag.objects.get_or_create(title=tag_title)[0] for tag_title in self.tags]
        question, created = Question.objects.get_or_create(
            sf_id = sf_id,
            defaults={'title':self.title, 'content':self.content}
        )
        question.tags.add(*tags)
        question.save()
        for answer in self.answers:
            Answer.objects.get_or_create(content=answer, question=question)
        return question, created

class TagSpider(spider.SegmentfaultTagSpider):

    def crawl(self):
        sf_ids = [url.split('/')[-1] for url in self.questions]
        for sf_id in sf_ids:
            question, created = ContentSpider(sf_id).save()

        def crawl_all_page(self):
            while True:
                print(u'正在抓取TAG:%s, 分页:%s ' %(self.tag_name, self.page))
                self.crawl()
                if not self.has_next_page:
                    break
                else:
                    self.next_page()
