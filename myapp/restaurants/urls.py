from django.urls import path, include

from . import views

app_name = "restaurants"
urlpatterns = [
    path("reservations/", views.IndexView.as_view(), name="IndexView"),
    path("reservations/<int:reservation_id>/", views.detail, name="detail"),
    path("reservation/", views.reservation, name="reservation"),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
