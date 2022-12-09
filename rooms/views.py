# from math import ceil
# from django.urls import reverse
from django.shortcuts import render, redirect
# from django.http import Http404
from django.core.paginator import Paginator, EmptyPage
from . import models, forms
from django.views.generic import ListView, DetailView, View
from django_countries import countries

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


# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/details.html", {
#             "room": room,
#         })
#     except models.Room.DoesNotExist:
#         raise Http404


class RoomDetail(DetailView):

    """ DetailView definition """

    model = models.Room


# def search(request):
#     city = request.GET.get("city", "anywhere")
#     city = str.capitalize(city)
#     country = request.GET.get("country", "IN")
#     room_type = int(request.GET.get("room_type", 3))
#     price = int(request.GET.get("price", 0))
#     person = int(request.GET.get("person", 0))
#     beds = int(request.GET.get("beds", 0))
#     baths = int(request.GET.get("baths", 0))
#     instant = request.GET.get("super_host", False)
#     super_host = request.GET.get("super_host", False)
#     s_amenities = request.GET.getlist("amenities")
#     f_facilities = request.GET.getlist("facilities")
    
#     form = {
#         "city": city,
#         "s_room_type": room_type,
#         "s_country": country,
#         "price": price,
#         "person": person,
#         "beds": beds,
#         "baths": baths,
#         "s_amenities": s_amenities,
#         "f_facilities": f_facilities,
#         "instant": instant,
#         "super_host": super_host,
#     }

#     room_types = models.RoomType.objects.all()
#     amenities = models.Amenity.objects.all()
#     facilities = models.Facility.objects.all()

#     choices = {
#         "countries": countries,
#         "room_types": room_types,
#         "amenities": amenities,
#         "facilities": facilities,
#     }

#     filter_args = {}

#     if city != "Anywhere":
#         filter_args["city__startswith"] = city

#     filter_args["country"] = country

#     if room_type != 0:
#         filter_args["room_type__pk"] = room_type

#     if price != 0:
#         filter_args["price__lte"] = price

#     if person != 0:
#         filter_args["person__gte"] = person

#     if beds != 0:
#         filter_args["beds__gte"] = beds

#     if baths != 0:
#         filter_args["baths__gte"] = baths

#     if instant is True:
#         filter_args["instant_book"] = True

#     if super_host is True:
#         filter_args["host__superhost"] = True

#     if len(s_amenities) > 0:
#         for s_amenity in s_amenities:
#             filter_args["amenities__pk"] = int(s_amenity)

#     if len(f_facilities) > 0:
#         for f_facility in f_facilities:
#             filter_args["facilities__pk"] = int(f_facility)

#     rooms = models.Room.objects.filter(**filter_args)

#     return render(request, "rooms/search.html", {
#         **form,
#         **choices,
#         "rooms": rooms,
#     })


class SearchView(View):

    def get(self, request):
        country = request.GET.get("country")

        if country:

            form = forms.SearchForm(request.GET)

            if form.is_valid():
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                superhost = form.cleaned_data.get("superhost")
                instant_book = form.cleaned_data.get("instant_book")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True
    
                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                qs = models.Room.objects.filter(**filter_args).order_by("-created")

                paginator = Paginator(qs, 10, orphans=5)

                page = request.GET.get("page", 1)

                rooms = paginator.get_page(page)

                return render(request, "rooms/search.html", {
                    "form": form,
                    "rooms": rooms
                })

        else:
            form = forms.SearchForm()

        return render(request, "rooms/search.html", {
            "form": form,
        })