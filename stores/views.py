from django.db.models import query
from django.shortcuts import render
from rest_framework import generics
from rest_framework.utils import model_meta
from .serializers import PizzeriaListSerializer, PizzeriaDetailSerializer
from .models import Pizzeria


class PizzeriaListAPIView(generics.ListAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaListSerializer


class PizzeriaRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer


class PizzeriaCreateAPIView(generics.CreateAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer


class PizzeriaRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer


class PizzeriaDeleteAPIView(generics.DestroyAPIView):
    lookup_field = "id"
    queryset = Pizzeria.objects.all()
