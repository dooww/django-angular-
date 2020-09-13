from django.db import models
from djchoices import ChoiceItem, DjangoChoices
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

class Strings(DjangoChoices):
    one = ChoiceItem('confirmed', 'refused','waiting')


class Condidat(models.Model):

	first_name = models.CharField(max_length=30)
	field = models.CharField(max_length=10, choices=Strings.choices,  default='waiting')
	last_name = models.CharField(max_length=30)
	birthday=models.DateField(null = True)
	phone_numbr=models.CharField(max_length=12,null = True)
	e_mail=models.CharField(max_length=300,default='')
	message=models.TextField(null = True)
	availablity=models.BooleanField(default=True)
	expirience_years_nbr=models.IntegerField(null=True)
	cv=models.FileField(null = True)
	confirmation = models.CharField(max_length=1 ,default='e')#, choices=STATUS)
	def send_email(self):
		subject="validation"
		message="your application have been stored in our database"
		from_email="mzahhd@gmail.com"
		try:
			send_mail(subject,message,from_email,[self.e_mail])
		except BadHeaderError:
			return HttpResponse('Invalid header found.')

	def __str__(self):
		return str(self.first_name)


			# send_mail('validation', 'your application have been stored in our database','hediimzah@gmail.com','mzahhd@gmail.com' , fail_silently = False)

	# def __init__(self,first_name,last_name,birthday,phone_numbr,e_mail,message,availablity,expirience_years_nbr,cv,confirmation):
