#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, urllib2, json



class GooglUrlShort(object):
    api_url = "https://www.googleapis.com/urlshortener/v1/url"

    def __init__(self, url):
        self.url = url

    def short(self, all_response = False):
        header = { "Content-Type": "application/json" }
        params = { "longUrl": self.url }

        try:
            response = urllib2.urlopen(urllib2.Request(self.api_url, json.dumps(params), header))
        except urllib2.HTTPError, e:
            if e.code:
                response = e.fp

        json_data = response.read()

        if all_response is True:
            return json_data
        else:
            data = json.loads(json_data)
            if 'id' in data:
                return json.loads(json_data)['id']
            return ""

    def expend(self, all_response = False):
        json_data = urllib.urlopen("https://www.googleapis.com/urlshortener/v1/url?shortUrl=%s" % self.url).read()

        if all_response == True:
            return json_data
        else:
            return json.loads(json_data)['longUrl'] if "longUrl" in json_data else ""
