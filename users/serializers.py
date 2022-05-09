from rest_framework import serializers

from place.models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)
    city = CitySerializer()

    class Meta:
        model = Place
        fields = ['id', 'title', 'city', 'image']
