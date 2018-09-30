from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Pet


# Create your views here.
def home(request):

	pets = Pet.objects.all()
	#Use a template. Template define in adoptions
	return render(request, 'home.html', {'pets':pets}) #pets are Parameters for the html to use


	#Returns a http
	#return HttpResponse('<p>Home View</p>')

def pet_detail(request, pet_id):
	try:
		pet = Pet.objects.get(id = pet_id)
	except:
		raise Http404("Pet not Found")

	return render(request, 'pet_detail.html', {'pet':pet}) #pet are Parameters for the html to use


	#return HttpResponse('<p>pet_detail view with id {}</p>'.format(pet_id))
