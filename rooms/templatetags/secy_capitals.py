from django import template

register = template.Library()


@register.filter()
def secy_capitals(value):
    print(value)
    return value.capitalize()
