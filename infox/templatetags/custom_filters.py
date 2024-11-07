from django import template

register = template.Library()

@register.filter
def add_delay(value, increment):
    return "{:.1f}s".format(float(value) + float(increment) * 0.1)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
