
from django.db import models

class PointLocations(models.Model):
	LocationID = models.AutoField(primary_key=True)
	PlaceName = models.CharField(max_length=200)
	Address = models.CharField(max_length=500)
	Latitude = models.CharField(max_length=50)
	Longitude = models.CharField(max_length=50)

	def __str__(self):
   		return 'PointLocation: ' + self.PlaceName

class AirQualityReadings(models.Model):
	ReadingID = models.AutoField(primary_key=True)
	DateAndTime = models.DateTimeField('date published')
	Reading = models.FloatField()
	LocationOfReading = models.ForeignKey(PointLocations, on_delete=models.CASCADE)

	def __str__(self):
   		return 'AirQualityReadings: ' + str(self.ReadingID)

	def as_json(self):
   		return dict(
   			ReadingID = self.ReadingID,
   			DateAndTime = self.DateAndTime,
   			Reading = self.Reading, 
   			LocationOfReading = self.LocationOfReading
   			)