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

TEMPLATE_PAGES = {
    '../labo/frontend/ripple_onclick/animate.css': 'labo/frontend/ripple_onclick/animate.css',
    '../labo/frontend/ripple_onclick/script.js': 'labo/frontend/ripple_onclick/script.js',
    '../labo/frontend/ripple_onclick/index.html': 'labo/frontend/ripple_onclick/index.html',

    '../labo/frontend/vanilla/benchmark.js': 'labo/frontend/vanilla/benchmark.js',
    '../labo/frontend/vanilla/script.js': 'labo/frontend/vanilla/script.js',
    '../labo/frontend/vanilla/index.html': 'labo/frontend/vanilla/index.html',

    '../labo/frontend/dragndrop/script.js': 'labo/frontend/dragndrop/script.js',
    '../labo/frontend/dragndrop/index.html': 'labo/frontend/dragndrop/index.html',

    '../labo/frontend/menu_dragndrop/script.js': 'labo/frontend/menu_dragndrop/script.js',
    '../labo/frontend/menu_dragndrop/index.html': 'labo/frontend/menu_dragndrop/index.html',

    '../labo/frontend/modernizr/is.js': 'labo/frontend/modernizr/is.js',
    '../labo/frontend/modernizr/modernizr-custom.js': 'labo/frontend/modernizr/modernizr-custom.js',
    '../labo/frontend/modernizr/duckTypingBrowserDetection.js': 'labo/frontend/modernizr/duckTypingBrowserDetection.js',
    '../labo/frontend/modernizr/pluginDetect.js': 'labo/frontend/modernizr/pluginDetect.js',
    '../labo/frontend/modernizr/script.js': 'labo/frontend/modernizr/script.js',
    '../labo/frontend/modernizr/index.html': 'labo/frontend/modernizr/index.html',

    '../labo/base.html': 'labo/base.html'
}

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
DIRECT_TEMPLATES = ((
    'index', 'tags', 'categories',
    'archives', 'search', '404'
))

CSS_THEMES = [
    {
        "name": "Thème classique (orange)",
        "path": "static/css/themes/classic.css",
        "default": True
    },
    {
        "name": "Thème océan (bleu)",
        "path": "static/css/themes/ocean.css"
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

# CACHE_CONTENT = True
# LOAD_CONTENT_CACHE = True
