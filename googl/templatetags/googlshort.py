#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from googl.short import GooglUrlShort



register = template.Library()

@register.filter
def googlshort(url):

    return GooglUrlShort(url).short(False)
