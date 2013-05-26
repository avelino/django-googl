#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, urllib2, json
from django.core.validators import URLValidator, ValidationError


class GooglUrlShort(object):
    api_url = "https://www.googleapis.com/urlshortener/v1/url"

    def __init__(self, url):
        self.url = url
        if isinstance(url, unicode):
            self.url = url.encode('utf-8')

        url_validator = URLValidator()
        try:
            url_validator(self.url)
        except ValidationError:
            return u""


    def short(self, all_response = False):
        header = { "Content-Type": "application/json" }
        params = { "longUrl": self.url }

        try:
            response = urllib2.urlopen(urllib2.Request(
                self.api_url, json.dumps(params), header))
        except urllib2.URLError, urllib2.HTTPError:
            return u""

        json_data = response.read()

        if not all_response:
            data = json.loads(json_data)
            if 'id' in data:
                return json.loads(json_data)['id']
            return u""
        return json_data

    def expend(self, all_response = False):
        json_data = urllib.urlopen(u"https://www.googleapis.com/urlshortener"
                                   "/v1/url?shortUrl=%s" % self.url).read()

        if not all_response:
            return json.loads(
                json_data)['longUrl'] if "longUrl" in json_data else ""
        return json_data
