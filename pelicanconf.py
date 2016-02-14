#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'Jérémie Ferry'
SITENAME = 'Le Labo Du Nerd'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = False

# TEMPLATE_PAGES = {
#     '../labo/base.html': 'labo/base.html'
# }

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'content/images',
    'static/robots.txt'
]

EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
}

PLUGIN_PATHS = ['pelican-plugins', 'personnal-plugins']

PLUGINS = [
    'assets', 'sitemap', 'gravatar',  #'i18n_subsites',
    'i18n', 'ace_editor',
    'tipue_search', "tag_cloud"  #, 'disqus_static'
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
    # 'ACE_EDITOR_THEME': 'pastel_on_dark',
    'ACE_EDITOR_SCROLL_TOP_MARGIN': 150,
    'ACE_EDITOR_MAXLINES': 200
}

# # Code highlighting
# PYGMENTS_STYLE = 'emacs'
MD_EXTENSIONS = [
    'codehilite(css_class=highlight, linenums=False, use_pygments=False)',
    'extra'
]
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DISQUS_SITENAME = 'lelabodunerd'
DISQUS_CATEGORY_ID = "3506724"  # Dev

DISQUS_SECRET_KEY = 'Iq1skapIEykejHa4FwVcbomNJOKkm4CoUhTHXwiKrnNrWFDMRYvo6VUcbS5c5ode'
DISQUS_PUBLIC_KEY = 'YbVM9ctM6uTgnAAWrezSFa1rwCiRhhNjjaPwBI9dmgcHJVYCmbw3PpwNgHcLdGzN'
