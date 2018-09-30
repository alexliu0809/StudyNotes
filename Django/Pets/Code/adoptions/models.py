from django.db import models

class Pet(models.Model):
	SEX_CHOICES = [("M","Male"),("F","Female")]
	name = models.CharField(max_length = 100)
	submitter = models.CharField(max_length = 100)
	species = models.CharField(max_length = 30)
	breed = models.CharField(max_length = 30, blank = True)
	description = models.TextField() #No length limit
	sex = models.CharField(choices=SEX_CHOICES, max_length = 1, blank = True) #Just one sex
	submission_date = models.DateTimeField()
	age = models.IntegerField(null = True) #if blank = 0, it's not distinguishable

	#Seperate table is created for this
	vaccinations = models.ManyToManyField('Vaccine',blank = True) # Some pets have 0 vac

class Vaccine(models.Model):
	name = models.CharField(max_length = 50) #Many to Many relationship.

	def __str__(self):
		return self.name #How this object is shown when called. -- Not listed in the talbe
