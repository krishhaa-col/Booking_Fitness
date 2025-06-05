
from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import FitnessViewSet, BookingViewSet
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fitness/', FitnessViewSet.as_view({'get': 'list', 'post': 'create'}), name='fitness'),
    path('fitness/<int:pk>/', FitnessViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='fitness_detail'),
    path('booking/', BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking'),
    path('booking/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='booking_detail'),
]
