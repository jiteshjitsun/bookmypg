import datetime
from rooms import models as room_models
from . import models
from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from django.views.generic import View
from django.http import Http404
from reviews import forms as review_forms
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
        reservation = models.Reservation.objects.get_or_none(pk=pk)
        if not reservation:
            raise Http404()
        if reservation.guest != self.request.user and reservation.room.owner != self.request.user:
            raise Http404()
        
        form = review_forms.CreateReviewForm
        return render(self.request, "bookings/detail.html", {'reservation': reservation, 'form':form})


def edit_reservation(request, pk, verb):
    reservation = models.Reservation.objects.get_or_none(pk=pk)
    if not reservation or (reservation.guest != request.user and reservation.room.owner != request.user):
        raise Http404()
    if verb == "confirm":
        reservation.status = models.Reservation.STATUS_CONFIRMED
    elif verb == "cancel":
        reservation.status = models.Reservation.STATUS_CANCELLED
        models.BookedDay.objects.filter(reservation=reservation).delete()
    reservation.save()
    messages.success(request, "Reservation Update")
    return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))
