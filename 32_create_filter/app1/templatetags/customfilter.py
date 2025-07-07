from django import template
register=template.Library()



def tomorrow(value,arg):
    return value.replace(arg,'Tomorrow')

register.filter('Tomorrow',tomorrow)