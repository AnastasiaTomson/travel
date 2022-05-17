from rest_framework import serializers

from place.models import *
from trip.models import UserPlace, UserTrip


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTrip
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)
    city = CitySerializer()

    class Meta:
        model = Place
        fields = ['id', 'title', 'city', 'image']


class PlaceDateSerializer(serializers.ModelSerializer):
    trip = TripSerializer()

    class Meta:
        model = UserPlace
        fields = '__all__'
