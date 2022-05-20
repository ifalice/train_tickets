from django import template

register = template.Library()

@register.filter(name='range_filter')
def range_filter(value:int):
    return range(value)

@register.filter(name = 'type_element')
def type_element(value):
    return type(value)

@register.filter(name = 'isinstance_class_list')
def isinstance_class_list(value):
    return isinstance(value, list)

@register.filter(name = 'zip')
def zip_lists(first, second):
    return zip(first, second)