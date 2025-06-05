from rest_framework import serializers
from .models import *

class FitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fitness
        fields = ['id', 'name', 'date', 'instructor', 'available_slots']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'client_name', 'client_email']