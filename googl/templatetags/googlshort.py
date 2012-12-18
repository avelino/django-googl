#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from django.core.cache import cache
from googl.short import GooglUrlShort

import uuid



register = template.Library()

@register.filter
def googlshort(url):

    uid = uuid.uuid3(uuid.NAMESPACE_DNS, url)

    cache_url = cache.get('googlshort_%s' % uid)
    if cache_url:
        return cache_url

    cache_url = GooglUrlShort(url).short(False)
    cache.set('googlshort_%s' % uid, cache_url)

    return cache_url
