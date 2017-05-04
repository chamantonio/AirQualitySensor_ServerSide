from rest_framework import serializers
from airqsapp.models import PointLocations, AirQualityReadings

class PointLocationsSerializer(serializers.Serializer):
	#LocationID = serializers.AutoField(required = True)
	PlaceName = serializers.CharField(required = True, allow_blank = False, max_length=200)
	Address = serializers.CharField(required = True, allow_blank = False, max_length=500)
	Latitude = serializers.CharField(required = True, allow_blank = False, max_length=50)
	Longitude = serializers.CharField(required = True, allow_blank = False, max_length=50)

	def create (self, validated_data):
		return Snippet.objects.create(**validated_data)

class AirQualityReadingsSerializer(serializers.Serializer):
	#ReadingID = serializers.AutoField(required = True)
	DateAndTime = serializers.DateTimeField(required = True)
	Reading = serializers.FloatField(required = True)
	LocationOfReading = serializers.ForeignKey(required = True)

	def create (self, validated_data):
		return Snippet.objects.create(**validated_data)