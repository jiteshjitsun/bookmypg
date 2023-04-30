import datetime
from rooms import models as room_models
from . import models
from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from django.views.generic import View
from django.http import Http404
# Create your views here.


class CreateError(Exception):
    pass


def create(request, room, year, month, day):
    try:
        date_obj = datetime.datetime(year, month, day)
        room = room_models.Room.objects.get(pk=room)
        models.BookedDay.objects.get(day=date_obj, reservation__room=room)
        raise CreateError()
    except (room_models.Room.DoesNotExist, CreateError):
        messages.error(request, "Can't Book that")
        return redirect(reverse("core:home"))
    except models.BookedDay.DoesNotExist:
        reservation = models.Reservation.objects.create(
            guest=request.user,
            room=room,
            check_in=date_obj,
            check_out=date_obj + datetime.timedelta(days=1)
        )
        return redirect(reverse("reservations:detail", kwargs={'pk': reservation.pk}))


class ReservationDetailView(View):

    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        resevation = models.Reservation.objects.get_or_none(pk=pk)
        if not resevation:
            raise Http404()
        if resevation.guest != self.request.user and resevation.room.owner != self.request.user:
            raise Http404()
        return render(self.request, "bookings/detail.html", {'reservation': resevation})
