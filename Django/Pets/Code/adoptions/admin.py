from django.contrib import admin
from .models import Pet
# Register your models here.

#Decorator.
#Pet model is registered, So that it can be visited.

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):

	#List display in a table.
	#What attributes will be shown in the table
	list_display = ['name','species','breed','age','sex'] #This is how you display pet object in the web

