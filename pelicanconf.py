#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Jérémie Ferry'
SITENAME = 'Le Labo Du Nerd'
SITEURL = 'https://mothsart.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

DISPLAY_PAGES_ON_MENU = False

TEMPLATE_PAGES = {
    '../labo/base.html': 'labo/base.html'
}

FRONTEND_PATH = os.path.join(os.path.dirname(__file__), 'labo/frontend')
for folder, subFolders, files in os.walk(FRONTEND_PATH, followlinks=True):
    if '.git' in subFolders:
        subFolders.remove('.git')
    for file in files:
        path = os.path.join(folder, file)
        TEMPLATE_PAGES["../" + path] = path

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'static'
]

EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
}

PLUGIN_PATHS = [
    'pelican-plugins',
    'personnal-plugins'
]

PLUGINS = [
    'sitemap', 'filetime_from_git',  #'i18n_subsites',
    'liquid_tags.video',
    'i18n', 'ace_editor',
    'tipue_search', 'tag_cloud' #, 'disqus_static'
]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

THEME = "themes/lab"
DIRECT_TEMPLATES = ((
    'index', 'tags', 'categories',
    'archives', 'search', '404'
))

CSS_THEMES = [
    {
        "name": "Thème classique (orange)",
        "path": "theme/css/orange.css",
        "default": True
    },
    {
        "name": "Thème océan (bleu)",
        "path": "theme/css/ocean.css"
    }
]

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/mothsART'),
    ('linkedin', 'https://www.linkedin.com/in/jérémie-ferry-0268a789'),
)

DEFAULT_PAGINATION = 10

DEFAULT_METADATA = {
    'status': 'draft'
}

# TAGS
TAG_CLOUD_STEPS = 1
TAG_CLOUD_MAX_ITEMS = 30
TAG_CLOUD_SORTING = 'size'
TAG_CLOUD_BADGE = True

# i18n
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
I18N_GETTEXT_LOCALEDIR = 'themes/lab/translations'
DEFAULT_LANG = 'fr'

# Ace Editor
ACE_EDITOR_PLUGIN = {
    'ACE_EDITOR_SCROLL_TOP_MARGIN': 150,
    'ACE_EDITOR_MAXLINES': 200
}

MD_EXTENSIONS = [
    'codehilite(css_class=highlight, linenums=False, use_pygments=False)',
    'extra'
]
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

#ISSO_SITEURL = 'http://localhost:9999'

DISQUS_SITENAME = 'http-mothsart-github-io'


# CACHE_CONTENT = True
# LOAD_CONTENT_CACHE = True
