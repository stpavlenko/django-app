from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'reservations', views.ReservationViewSet)

app_name = "restaurants"
urlpatterns = [
    path("reservations/", views.IndexView.as_view(), name="IndexView"),
    path("reservations/<int:reservation_id>/", views.detail, name="detail"),
    path("reservation/", views.reservation, name="reservation"),
    path('api/', include(router.urls)),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
