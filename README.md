# django-googl

Django short url on goo.gl

http://pypi.python.org/pypi/django-googl


# Installation

    pip install django-googl


# Usage

Add **googl** to your *INSTALLED_APPS*

Load **googl** in your template:

    {% load googl %}

And use **googl** filter:

    {{ "http://google.com"|googl }}