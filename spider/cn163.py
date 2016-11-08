#!/usr/bin/python
#-*- coding:utf-8 -*-
__author__ = "goodhe"

#=====================================

#File Name: cn163.spy
#Mail: gdhe55555@gmail.com
#Created Time: 2016-11-07 22:53:59

#=====================================

#爬取cn163的美剧的内容

import requests
import re
import sys
import threading
import time

reload(sys)
sys.setdefaultencoding("utf-8")

class Archives(object):
    def save_links(self, url):
        try:
            data = requests.get(url, timeout = 3)
            content = data.text
            link_pat = re.compile('"(ed2k://\|file\|[^"]+?\.(S\d+)(E\d+)[^"]+?1024X\d{3}[^"]+?)"')
            name_pat = re.compile(r'<h2 class="entry_title">(.*?)</h2>', re.S)
            links = set(re.findall(link_pat, content))
            name = re.findall(name_pat, content)
            links_dict = {}
            count = len(links)
        except Exception,e:
            print "Get ed2k error"
            pass

        for i in links:
            print i
            links_dict[int(i[1][1:3])*100 + int(i[2][1:3])] = i
        try:
            print name[0]
            with open(name[0].replace('/', ' ') + '.txt', 'w') as f:
                print name[0]
                for i in sorted(list(links_dict.keys())):
                    f.write(links_dict[i][0] + '\n')
                print "get links...", name[0], count
        except Exception,e:
            print "Write file error"
            pass
    def get_urls(self):
        try:
            for i in range(2010, 25000):
                base_url = 'http://cn163.net/archives/'
                url = base_url + str(i) + '/'
                if requests.get(url).status_code == 404:
                    continue
                else:
                    self.save_links(url)
        except Exception,e:
            print "Get links error"
            pass
    def main(self):
        thread1 = threading.Thread(target=self.get_urls())
        thread1.start()
        thread1.join()

if __name__ == "__main__":
    print "BEGIN"
    start = time.time()
    a = Archives()
    a.main()
    end = time.time()
    print end - start
    print "END"
