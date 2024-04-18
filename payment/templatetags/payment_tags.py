from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='frf')
@stringfilter
def frf(value):
    return value[17:]

@register.filter(name='frf24')
@stringfilter
def frf(value):
    return value[24:]

@register.filter(name='frf27')
@stringfilter
def frf(value):
    return value[27:]

@register.filter(name='frf020')
@stringfilter
def frf(value):
    return value[:20]

@register.filter(name='frf025')
@stringfilter
def frf(value):
    return value[:25]

@register.filter(name='frf0130')
@stringfilter
def frf(value):
    return value[:130]

@register.filter(name='frf0100')
@stringfilter
def frf(value):
    return value[:100]

@register.filter(name='tshk')
@stringfilter
def frf(value):
    return value.replace(',', '.')

@register.filter(name='summ')
@stringfilter
def summ(value):
    total = 0
    for a in value.split():
        total += float(a)
    return total