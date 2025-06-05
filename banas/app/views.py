from django.shortcuts import render
from django.http import HttpResponse
from .models import Fitness, Booking
from .serializers import FitnessSerializer, BookingSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

class FitnessViewSet(viewsets.ModelViewSet):
    queryset = Fitness.objects.all()
    serializer_class = FitnessSerializer

    def get(self,request):
        fitness_classes = Fitness.objects.all()
        serializer = FitnessSerializer(fitness_classes, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = FitnessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
