from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template import loader
from django.views import generic
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Q

from .models import Reservation, Restaurant
from .forms import ReservationForm
from .serializers import RestaurantSerializer, ReservationSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.filter(Q(address='Москва'))
    serializer_class = RestaurantSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
    @action(methods=['GET'], detail=False)
    def filter_by_moscow(self, request):
        queryset = self.get_queryset().filter(table__restaurant__address='Москва')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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
