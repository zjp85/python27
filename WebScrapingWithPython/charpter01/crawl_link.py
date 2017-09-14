# -*- coding: utf-8 -*-
import re
import urllib2
import urlparse
from common import download

color_r = '\033[1;31m'
color_g = '\033[1;32m'
# color_y = '\033[1;33m'
color_b = '\033[1;34m'
color_p = '\033[1;35m'
color_y = '\033[1;36m'

color_end = '\033[0m'

color_err = color_r
color_info = color_g

def get_links(html):
    """return a list of links from html"""
    # a regular expression to extract all links from webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from webpage
    return webpage_regex.findall(html)

def filter_link(url):
    if url == None:
        return True
#     elif (r'http://www.iot-club.cn' != url[0:len(r'http://www.iot-club.cn')]):
    elif re.match(r'^(?!.*http://www.iot-club.cn)', url):
        print color_p, '###---[', url, ']----###', color_end
        return True
    else:
        pass
    
    return False
        

def crawler_link0(seed_url, link_regex):
    """Crawl from the given seed URL following links matched by link_regex"""
    crawl_queue = [seed_url]
    # keep track which URL's have seen before
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        if filter_link(url):
            print color_err,'\n!!!--------[', url, '] ignored--------\n', color_end
            continue
        html = download(url)

        for link in get_links(html):
        # check if link maches expected regex
            if re.match(link_regex, link):
                # form absolute link
                link = urlparse.urljoin(seed_url, link)
                #check if have already seen this link
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)            


crawler_link = crawler_link0

if __name__ == '__main__':
#     crawler_link('http://example.webscraping.com', '/(index|view)')
    crawler_link('http://www.iot-club.cn', '')
    