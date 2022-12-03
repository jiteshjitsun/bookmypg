from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

# Create your views here.


# def all_rooms(request):
#     page = request.GET.get("page", 1)
    # if page == "":
    #     page = 1
    # else:
    #     page = int(page)
    # page_size = 10
    # limit = page_size * page
    # offset = limit - page_size
    # all_rooms = models.Room.objects.all()[offset:limit]
    # page_count = ceil(models.Room.objects.count() / page_size)
    # return render(request, "rooms/home.html", context={
        # "rooms": all_rooms,
        # "page": page,
        # "page_count": page_count,
        # "page_range": range(1, page_count),
    # })


# better way than above one by using django paginator 

def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    rooms = paginator.page(int(page))
    # print(vars(rooms))
    return render(
        request,
        "rooms/home.html",
        {
            "page": rooms,
        },
    )
