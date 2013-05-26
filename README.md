# django-googl
[![PyPi version](https://pypip.in/v/django-googl/badge.png)](https://crate.io/packages/django-googl/)
[![PyPi downloads](https://pypip.in/d/django-googl/badge.png)](https://crate.io/packages/django-googl/)

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

Use **googl** in backend:

    from googl.short import GooglUrlShort
    
    GooglUrlShort("http://avelino.us/").short()
