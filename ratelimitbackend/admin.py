# Allow transitive imports, e.g.
# `from ratelimitbackend import admin; admin.ModelAdmin`
from django.contrib.admin import *  # noqa
from django.contrib.admin import site as django_site

from .apps import site


for model, admin in django_site._registry.items():
    site.register(model, admin.__class__)
