# from math import ceil
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import Http404
# from django.core.paginator import Paginator, EmptyPage
from . import models
from django.views.generic import ListView

# Create your views here.

# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     if page == "":
#       page = 1
#     else:
#       page = int(page)
#     page_size = 10
#     limit = page_size * page
#     offset = limit - page_size
#     all_rooms = models.Room.objects.all()[offset:limit]
#     page_count = ceil(models.Room.objects.count() / page_size)
#     return render(request, "rooms/home.html", context={
#       "rooms": all_rooms,
#       "page": page,
#       "page_count": page_count,
#       "page_range": range(1, page_count),
#     })


# better way than above one by using django paginator 

# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)
#     try:
#         rooms = paginator.page(int(page))
#         return render(
#             request,
#             "rooms/home.html",
#             {
#                 "page": rooms,
#             },
#         )
#     except EmptyPage:
#         rooms = paginator.page(1)
#         return redirect("/")


class HomeView(ListView):

    """ HomeView definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/details.html", {
            "room": room,
        })
    except models.Room.DoesNotExist:
        raise Http404