# -*- coding: utf-8 -*-
import urllib2
import urlparse

# simple download
def download1(url):
    """Simple downloader"""
    return  urllib2.urlopen(url).read()

def download2(url,  num_retries = 2):
    """Download function that also retries 5XX errors"""
    print '\n-------Start downloading: [', url,']-------\n\n'
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download Error:', e.reason
        
        html = None
        if(num_retries >0):
            if hasattr(e, 'code') and (500 <= e.code < 600):
                # recurs ive l y retry Sxx HTTP errors
                return download(url, num_retries-1)
    return html

def download3(url, user_agent = 'wswp', num_retries = 2):
    """Download function that includes user agent support"""
    print '-------Start downloading: [', url,']-------\n\n'
    headers = {'User-agent:':user_agent}
    request = urllib2.Request(url, headers=headers)
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download Error:', e.reason
        
        html = None
        if(num_retries >0):
            if hasattr(e, 'code') and (500 <= e.code < 600):
                # recurs ive l y retry Sxx HTTP errors
                return download(url, user_agent, num_retries-1)
    return html

#'''
def download4(url, user_agent = 'wswp', proxy=None, num_retries = 2):
    """Download function that includes user agent support"""
    print '-------Start downloading: [', url,']-------\n\n'
    headers = {'User-agent:':user_agent}
    request = urllib2.Request(url, headers=headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download Error:', e.reason
        
        html = None
        if(num_retries >0):
            if hasattr(e, 'code') and (500 <= e.code < 600):
                # recurs ive l y retry Sxx HTTP errors
                return download(url, user_agent, proxy, num_retries-1)
    return html
#'''

download = download4

if __name__ == '__main__':
#    download('http://httpstat.us/500') 
    print
    print download('http://example.webscraping.com')
#     print'\n\n\n--------------------------------------------------------\n\n\n'
#     print download('http://www.seo.net.cn/sitemap')