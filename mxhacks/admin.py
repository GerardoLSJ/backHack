from django.contrib import admin
from .models import(Tags, Procedure, Law, City, Country)

admin.site.register(Tags)
admin.site.register(Procedure)
admin.site.register(Law)
admin.site.register(Country)
admin.site.register(City)