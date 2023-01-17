from django import template

register = template.Library()

@register.filter
def filter_event(events, weekday):
    filtered = events.filter(start_time)