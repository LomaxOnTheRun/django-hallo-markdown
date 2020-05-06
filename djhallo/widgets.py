#!/usr/bin/env python
# -*- coding: utf-8
from __future__ import print_function

from django import forms
from django.conf import settings
from django.forms.utils import flatatt
from django.utils.html import escape
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

# Try the Python 3 import but default to the Python 2 one
try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text


class HalloInput(forms.Textarea):

    def render(self, name, value, attrs=None):
        value = value or ''
        final_attrs = self.build_attrs(attrs, name=name)
        html = [
            '<div class="hallo-block"><article class="edit"></article><textarea%s>%s</textarea></div>' % \
            (flatatt(final_attrs), force_text(escape(value)))
        ]
        return mark_safe('\n'.join(html))

    @property
    def media(self):
        return forms.Media(css= {'screen': [settings.STATIC_URL + "djhallo/hallo.css"]},
            js=(
                '//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js',
                '//ajax.googleapis.com/ajax/libs/jqueryui/1.8.18/jquery-ui.min.js',
                settings.STATIC_URL + "djhallo/jquery-init.js",
                settings.STATIC_URL + "djhallo/showdown.js",
                settings.STATIC_URL + "djhallo/to-markdown.js",
                settings.STATIC_URL + "djhallo/hallo.js",
                settings.STATIC_URL + "djhallo/djhallo.js"))
