from django.shortcuts import render
from rest_framework import generics
from .models import Stock
from .serializers import StockSerializer

class StockListCreate(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
