from django.contrib import admin
from .models import(Tags, Procedure, Law,City,Country)
from rest_framework import serializers

from rest_framework.fields import ListField

class StringArrayField(ListField):
    """
    String representation of an array field.
    """
    def to_representation(self, obj):
    	obj = super().to_representation( obj)
    	return ",".join([str(element) for element in obj])

    def to_internal_value(self, data):
    	data = data.split(",")  # convert string to list
    	return super().to_internal_value(data)

class TagsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tags
		fields = ('__all__')

class ProcedureSerializer(serializers.ModelSerializer):
	class Meta:
		model = Procedure
		fields = ('__all__')

class LawSerializer(serializers.ModelSerializer):
	bullets = StringArrayField()
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