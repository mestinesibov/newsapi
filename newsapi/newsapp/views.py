from django.shortcuts import render
from rest_framework import generics, permissions

from .models import News
from .serializers import NewsSerializers

# Create your views here.

class NewsList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny,]
    queryset = News.objects.all()
    serializer_class = NewsSerializers

