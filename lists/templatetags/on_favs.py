from django import template
from lists import models as list_models

register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, room):
    user = context.request.user
    the_list = list_models.List.objects.get(user=user, name="My Favourite Rooms")
    print(the_list)
    # return list_models.List.objects
    
    return room in the_list.rooms.all()
