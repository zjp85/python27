# -*- coding: utf-8 -*-

import itertools
from common import download
from timeit import itertools


def iteration1():    
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/view/-%d' % page
        html = download(url)
        if html is None:
            break
        else:
            # success - can scrape the result
            pass

def iteration2():    
    max_errors = 5
    num_errors = 0
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/view/-{}'.format(page)
        html = download(url)
        if html is None:
            # received an error trying to download this webpage
            num_errors += 1
            if num_errors == max_errors:
                # reached maximum amount of errors in a row so exit
                break
            # so assume have reached the last country ID and can stop downloading
        else:
            # success - can scrape the result
            num_errors = 0
        

iteration = iteration2

if '__name__' == '__main__':
    iteration()