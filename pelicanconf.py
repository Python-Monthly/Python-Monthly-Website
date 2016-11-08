#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Python Monthly'
SITENAME = 'Python Monthly'
SITEURL = ''
THEME = 'pelican-clean-blog'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/Python-Monthly'),
          ('google','https://plus.google.com/112952259748021652374'),
          ('envelope','mailto:info@pythonmonthly.com'),
	  ('slack','https://pythonmonthly.slack.com'),
	  ('youtube','https://www.youtube.com/channel/UC7ROIuBkGtLpCIMsgoIwv0Q'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


THEME = 'theme/pelican-clean-blog'

#Nav Menu Options
MENUITEMS = [
	('Videos', 'category/videos.html')
	]
