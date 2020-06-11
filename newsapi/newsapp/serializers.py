from rest_framework import serializers
from .models import Category, News


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'category',
            'description',
            'image',
        )
        model = News



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'description',
        )
        model = Category




