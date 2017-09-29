#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'PythonBrasil'
SITENAME = u'PythonBrasil 13'
SITEURL = 'http://2017.pythonbrasil.org.br'
SITE_DESCRIPTION = (
    "13ª Conferência Brasileira da Comunidade Python. São seis dias de "
    "atividades! Palestras de 6 a 8 de Outubro. Tutoriais e sprints de "
    "9 a 11 de Outubro."
)

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'
THEME = "./theme"

DEFAULT_LANG = u'pt'

# URL mapping
ARTICLE_URL = 'noticias/{slug}'
ARTICLE_SAVE_AS = 'noticias/{slug}/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

CATEGORIES_URL = 'noticias/categorias'
CATEGORIES_SAVE_AS = 'noticias/categorias/index.html'
CATEGORY_URL = 'noticias/categorias/{slug}'
CATEGORY_SAVE_AS = 'noticias/categorias/{slug}/index.html'

TAG_URL = 'noticias/tags/{slug}'
TAG_SAVE_AS = 'noticias/tags/{slug}/index.html'
TAGS_URL = 'noticias/tags'
TAGS_SAVE_AS = 'noticias/tags/index.html'

AUTHOR_URL = 'noticias/autores/{slug}'
AUTHOR_SAVE_AS = 'noticias/autores/{slug}/index.html'
AUTHORS_URL = 'noticias/autores'
AUTHORS_SAVE_AS = 'noticias/autores/index.html'

INDEX_SAVE_AS = "noticias/index.html"

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None

STATIC_PATHS = ['images', 'extra/CNAME', 'programacao.pdf']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Plugins
PLUGIN_PATHS = ['./.plugins']
PLUGINS = [
        'better_figures_and_images',
        'sitemap',
        'i18n_subsites',
        ]

RESPONSIVE_IMAGES = True
PYGMENTS_STYLE= "perldoc"
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'indexes': 0.2,
        'pages': 0.7
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    },
}

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
