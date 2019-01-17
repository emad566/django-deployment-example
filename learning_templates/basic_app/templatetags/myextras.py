from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This cut out all values of arg from a string value
    """
    return value.replace(arg,'')

# register.filter('cut', cut)