# encoding: utf-8
'''
Make reading the news more fun.
http://xkcd.com/1288/
'''
from __future__ import unicode_literals
import re
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()
d = {
    "witnesses": "these dudes I know",
    "Witnesses": "These dudes I know",
    "allegedly": "kinda probably",
    "Allegedly": "Kinda probably",
    "new study": "Tumblr post",
    "New study": "Tumblr post",
    "rebuild": "avenge",
    "Rebuild": "Avenge",
    "space": "spaace",
    "Space": "Spaace",
    "google glass": "Virtual Boy",
    "Google glass": "Virtual Boy",
    "Google Glass": "Virtual Boy",
    "Smartphone": "Pokédex",
    "smartphone": "Pokédex",
    "electric": "atomic",
    "Electric": "Atomic",
    "senator": "elf-lord",
    "Senator": "Elf-lord",
    "car": "cat",
    "Car": "Cat",
    "election": "eating contest",
    "Election": "Eating contest",
    "congressional leaders": "river spirits",
    "Congressional leaders": "River spirits",
    "homeland security": "Homestar Runner",
    "Homeland security": "Homestar Runner",
    "Homeland Security": "Homestar Runner",
    "could not be reached for comment": "is guilty and everyone knows it",
}


@register.filter(is_safe=True)
@stringfilter
def substitute(value):
    pattern = re.compile('|'.join(d.keys()))
    try:
        result = pattern.sub(lambda x: d[x.group()], value)
    except:
        result = value
    return result
