from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def split(string, sep):
    """Return the string split by sep.

    Example usage: {{ value|split:"/" }}
    """
    return [int(i) for i in string.split(sep)]


@register.simple_tag
def exist_in_trip(place, trip):
    return place.userplace_set.filter(trip=trip).exists()

#
# @register.inclusion_tag('results.html')
# def show_places(places):
#