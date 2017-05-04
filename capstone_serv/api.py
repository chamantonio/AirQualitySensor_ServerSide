
from io import BytesIO
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
import os
from shutil import which
import subprocess
import uuid


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from airqsapp.models import PointLocations, AirQualityReadings
import json

@api_view(['POST'])
def InsertReadings(request, multiple=False):

    if request.method == 'POST':
        data = request.data
        print ("TESTING IF RETRIEVED", data)
        insert_data = AirQualityReadings(DateAndTime = data["DateAndTime"], Reading = data["Reading"], LocationOfReading = PointLocations.objects.get(LocationID = data["LocationOfReading"]))
        insert_data.save()
        _response  = "Done inserting "+ str(data)
        return Response(_response)


@api_view(['GET'])
def GetAllReadings(request, multiple=False):
	if request.method == 'GET':
		_response = AirQualityReadings.objects.all()#.as_json()
		"""print (type(_response))
		for readings in _response:
			print (readings.Reading)
		_response_list = list(_response)
		print (_response_list[0].Reading)"""
		#return Response("testing get")
		#return Response(json.dumps(_response_list), content_type="application/json")
		return JsonResponse(serializers.serialize('json',_response), safe=False)

@api_view(['GET'])
def GetAllPointLocations(request, multiple=False):
	if request.method == 'GET':
		_response = PointLocations.objects.all()#.as_json()
		"""print (type(_response))
		for readings in _response:
			print (readings.Reading)
		_response_list = list(_response)
		print (_response_list[0].Reading)"""
		#return Response("testing get")
		#return Response(json.dumps(_response_list), content_type="application/json")
		return JsonResponse(serializers.serialize('json',_response), safe=False)