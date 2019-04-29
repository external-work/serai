from django.db import models

class Clients(models.Model):
	first_name = models.CharField(max_length=250)
	last_name = models.CharField(max_length=250)
	user_name = models.CharField(max_length=250)
	contact = models.CharField(max_length=250)
	password = models.CharField(max_length=250)
	company = models.CharField(max_length=250, default='Unknown')


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
	