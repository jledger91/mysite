from django.contrib.admin import site

from .film import *
from .review import *

site.site_header = 'MySite administration'
site.site_title = 'MySite admin'
