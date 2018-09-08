from django.contrib import admin
from .models import(Tags, Procedure, Law,City,Country)
from rest_framework import serializers

class TagsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tags
		fields = ('__all__')

class ProcedureSerializer(serializers.ModelSerializer):
	class Meta:
		model = Procedure
		fields = ('__all__')

class LawSerializer(serializers.ModelSerializer):
	class Meta:
		model = Law
		fields = ('__all__')

class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model = City
		fields = ('__all__')

class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = ('__all__')