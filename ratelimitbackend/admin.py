# Allow transitive imports, e.g.
# `from ratelimitbackend import admin; admin.ModelAdmin`
from django.contrib.admin import *  # noqa

from .apps import site
