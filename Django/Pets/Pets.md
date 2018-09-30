

<hr style="border: 5px solid#FF000F;" />

# Other Reference Sheet
## Install
```shell
python -m pip install django==1.11.7
```

## Start A Project
```shell
django-admin.py startproject wisdompets
```

## Run App
```shell
python3 manage.py startapp adoptions
```

## Files in an app
| File          | Role          | 
| ------------- |:-------------:| 
| apps.py      | Config | 
| models.py      | Data Layer | 
| admin.py      | Administrative Interface | 
| urls.py      | URL Routing | 
| views.py      | Control Layer |
| tests.py      | Tests the app | 
| migrations/     | Hold migration files| 


## Django Design Pattern
MVC:
Model: models.py -> data
Controller: views.py --> logic
View: *.html -> presentation
*	URL Patterns (adoptions/urls.py) -> Decide which view to pass 
*	Views (adoptions/views.py) -> HTTP Response, query database
*	Models (adoptions/models.py) -> database spec


## Models
*	Data layer of an app
*	Define DB structure
*	enables query

## Example:
```python
from django.db import models

class Item(models.Model):
	title = models.CharField(max_length=200) #Field name title, type char
	description = models.TextField() #Field name description, type text.
	amount = models.InterField() #Field name amount, type int.
```

## Field Attributes:
*	max_length
*	null
*	blank
*	default
*	choices

## Why migration.
*	When new model is created, migration creates tables.
*	Adding a field/ Removing a field / Changing a field
## Command for migration 
First register your app in "INSTALLED_APPS" under setting.py.
```shell
python manage.py makemigrations
python manage.py migrate
```
### makemigrations
*	Generate migration files
*	Query current model field and determine what changes are needed.
*	Migrations are named with numbers
### migrate
*	Runs all migrations that haven't been run yet.

## Models Created.
*	APP_NAME_Pet
*	APP_NAME_Vaccine
*	APP_NAME_Pet_vaccinations. Notice here a separate file is created.

## Load CSV Data
Python will call hanlde method
```shell
python3 manage.py load_pet_data
```

## Add Admin
In admin.py. register ModelAdmin
Also, run the following to create super user:
```shell
python3 manage.py createsuperuser
```
Then visit http://127.0.0.1:8000/admin/

## Python interactive shell
```shell
python3 manage.py shell
```
```python
from adoptions.models import Pet #Read a table
pets = Pet.objects.all() #Read an object (record)
pet = pets[0]
pet.name #get name
pet.id # From 1.
pet = Pet.objects.get(id=1) #Get first pet
pet.vaccinations.all() #Return all vaccinations
```

## Regular Expressions
Also see pythex.com, and regular expression coureses.

| Regular          | String that matches      | 
| ------------- |:-------------:| 
| ducky     | ducky, Match exactly ducky | 
| \d      | 1, Match a single digit| 
| \d+      | 123, Match multiple digits | 
| ^admin/      | admin/invertory, Match any string starting with admin/ | 
| suffix$     | anything ends wtih suffix |
| ^$      | Empty string | 

## URL Pattern Example
```python
# Try match one by one
urlpatterns = [
    url(r'^admin/', admin.site.urls), #Navigate to admin
    url(r'^$', views.home, name="home"), # Navigate to home if no parameter
    url(r'^adoptions/(\d+)/',views.pet_detail, name="pet_detail") #In parenthesis, parse as a group, and pass numbers as parameters
]

```

## Template Syntax
```html
{{ variable}}
{% tag %}
{{variable|filter}}
```

```html
<h3>{{pet.name}}</h3>
{% for pet in pets %}
	<li>{{pet.name}}</li>
{% endfor %}

## Result:
<li>Pepe<li>
<li>Scooter</li>

<h3>{{pet.name|capfirst}}</h3>
<a href="{% url 'pet_detail' pet.id %}"> <!--Create url to pet_detail, whose Name defined in urls.py with name="", and para pet.id-->
<!-- Result: /adoption/3-->
```

## Virtualenv
```shell
pip install virtualenv

#To set up virtualenv for that project
cd my_project
virtualenv venv --system-site-packages #create isolated env, this does not need super access, also extends global lib
#When this is active, everything goes into this directory, no sudo needed.

#This creates a venv folder in the current folder.
#To activate
source venv/bin/activate
#To deactivate 
source venv/bin/deactivate
```
