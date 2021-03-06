# -*- coding: utf-8 -*-
import re
import urllib2
import urlparse

color_r = '\033[1;31m'
color_g = '\033[1;32m'
# color_y = '\033[1;33m'
color_b = '\033[1;34m'
color_p = '\033[1;35m'
color_y = '\033[1;36m'

color_end = '\033[0m'

color_err = color_r
color_info = color_g
color_warn = color_p

# simple download
def download1(url):
    """Simple downloader"""
    return  urllib2.urlopen(url).read()

def download2(url,  num_retries = 2):
    """Download function that also retries 5XX errors"""
    print '\n-------downloading: [', url,']-------\n'
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download Error:', e.reason
        
        html = None
        if(num_retries >0):
            if hasattr(e, 'code') and (500 <= e.code < 600):
                # recurs ive l y retry Sxx HTTP errors
                return download2(url, num_retries-1)
    return html

def download3(url, user_agent = 'wswp', num_retries = 2):
    """Download function that includes user agent support"""
    print '-------downloading: [', url,']-------\n\n'    
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
                return download3(url, user_agent, num_retries-1)
    return html

#'''
def download4(url, user_agent = 'wswp', proxy=None, num_retries = 2):
    """Download function that includes user agent support"""
    print '-------downloading: [', url,']-------\n\n'
    headers = {'User-agent:':user_agent}
    request = urllib2.Request(url, headers=headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        # check if url is legal
        if re.match(r'^https?:/{2}\w.+$', url):
            html = urllib2.urlopen(url).read()
        else:
            return None
        """
        html = urllib2.urlopen(url).read()
        """
    except urllib2.URLError as e:
        print 'Download Error:', e.reason        
        html = None
        if(num_retries >0):
            if hasattr(e, 'code') and (500 <= e.code < 600):
                # recurs ive l y retry Sxx HTTP errors
                return download4(url, user_agent, proxy, num_retries-1)
    return html
#'''

# add agent support
def download5(url, user_agent = 'wswp', proxy=None, num_retries = 2):
    """Download function that includes user agent support"""
    print '-------downloading: [', url,']-------\n\n'
    headers = {'User-agent:':user_agent}
    request = urllib2.Request(url, headers=headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        # check if url is legal
        if re.match(r'^https?:/{2}\w.+$', url):
            response = opener.open(request)
            html = response.read()
            code = response.code
        else:
            return None
    except urllib2.URLError as e:
        print 'Download Error:', e.reason        
        html = ''
        if(num_retries >0):
            if hasattr(e, 'code') and (500 <= e.code < 600):
                # recurs ive l y retry Sxx HTTP errors
                return download4(url, user_agent, proxy, num_retries-1)

    return html

download = download5

if __name__ == '__main__':
#    download('http://httpstat.us/500') 
    print
    print download('http://example.webscraping.com')