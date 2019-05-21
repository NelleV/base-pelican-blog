#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nelle'
SITENAME = 'Stuff…'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

 # We are using the custom minimal theme:
THEME = './themes/minimal/'
MARKPUP = ("md", )


# Blogroll
LINKS = (         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Custom functions available to all templates:
import calendar
import ntpath

GITHUB_ISSUE_PATH='https://github.com/bytefish/bytefish.de/issues'
GITHUB_SOURCE_PATH='https://github.com/bytefish/bytefish.de/blob/master/blog'

def getGitHubPage(source_file):
    filename = getBasename(source_file)
    return '{0}/{1}'.format(GITHUB_SOURCE_PATH, filename)

def getBasename(path):
    return ntpath.basename(path)

def month_name(month_number):
    return calendar.month_name[month_number]

# Probably replace those with simpler methods:
from operator import itemgetter, methodcaller

def sortTupleByIndex(items, index=0, reverse=True):
  return sorted(items, key=lambda tup: len(tup[index]), reverse=reverse)

def sortDictByKey(items, key, reverse=True, default=None):
  if default is None:
    return sorted(items, key=itemgetter(key), reverse=reverse) 
  return sorted(items, key=methodcaller('get', key, default), reverse=reverse) 



JINJA_FILTERS = {
    'month_name' : month_name,
    'sortTupleByIndex': sortTupleByIndex,
    'sortDictByKey': sortDictByKey,
    'basename' : getBasename,
    'asGitHubPage' : getGitHubPage
  }

