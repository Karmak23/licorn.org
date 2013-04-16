#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = 'http://licorn.org'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
#RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/atom.xml'

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = 'UA-2868362-7'
