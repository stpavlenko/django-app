from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)

app_name = "restaurants"
urlpatterns = [
    path("reservations/", views.IndexView.as_view(), name="IndexView"),
    path("reservations/<int:reservation_id>/", views.detail, name="detail"),
    path("reservation/", views.reservation, name="reservation"),
    path('', include('router.urls')),
    # path('your-models/', views.RestaurantListCreateView.as_view(), name='your-models-list-create'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
