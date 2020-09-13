from django.db import models
from django import forms


# Create your models here.

    # STATUS = (
	# 	('c', 'confirmer'),
	# 	('e', 'en cours'),
	# 	('r', 'rejeter'),
	#)
class Condidat(models.Model):


    # status = models.CharField(max_length=1, choices=STATUS)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	birthday=models.DateField(null = True)
	phone_numbr=models.CharField(max_length=12,null = True)
	e_mail=models.CharField(max_length=300,default='')
	message=models.TextField(null = True)
	availablity=models.BooleanField(default=True)
	expirience_years_nbr=models.IntegerField(null=True)
	cv=models.FileField(null = True)


	def __str__(self):
		return str(self.first_name);
