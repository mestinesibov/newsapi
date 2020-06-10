from django.shortcuts import render
from rest_framework import generics

from .models import News
from .serializers import NewsSerializers

from django.utils.text import slugify
# Create your views here.

class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class NewsDetail(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers

