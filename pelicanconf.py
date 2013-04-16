#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os

AUTHOR = u'Olivier Cort\xe8s'
SITENAME = u'Licorn\xae: efficient server management'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = os.path.expanduser("~/sources/pelican-themes/licorn.org")

TYPOGRIFY = False
STATIC_PATHS = ('images', 'pdf', )
DEFAULT_CATEGORY = 'News'
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

# Blogroll
LINKS = ((u'Official documentation', 'http://docs.licorn.org/'),
         (u'Development & Support', 'https://trello.com/licorn'),
         (u'Tarballs downloads',
          'https://duncan.licorn.org:3356/share/olive/licorn/'),
         (u'Licorn® on Twitter®', 'https://twitter.com/Licorn_info'),)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False
