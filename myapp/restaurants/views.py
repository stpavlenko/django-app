from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template import loader
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import Reservation
from .forms import ReservationForm


class IndexView(generic.ListView):
    template_name = ("restaurants/index.html")
    context_object_name = "latest_reservation_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Reservation.objects.order_by("-date")[:5]


def detail(request, reservation_id):
    try:
        reservation = Reservation.objects.get(pk=reservation_id)
    except Reservation.DoesNotExist:
        raise Http404("Reservation does not exist")
    return render(request, "restaurants/detail.html", {"reservation": reservation})


@login_required
def reservation(request):
    form = ReservationForm(request.POST)
    if form.is_valid():
        reservation = form.save(commit=False)
        reservation.user = request.user
        reservation.save()
    return render(request, 'restaurants/reservation.html', {'form': form})
