from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from .models import Clients
import json
from .assets import skill_extract
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm

enable = False
context = {}


def logging(request):
	return render(request, 'Login/login.html')

def registering(request):
	return render(request, 'Login/register.html')

def call_chatbot(request):
	return render(request, 'Login/chatbot.html')

def call_main(request):
	context = {
		'enable' : enable,
	}
	return render(request, 'Login/main.html', context)

def place(request):
	context = {}
	with open(str(os.path.dirname(os.path.realpath(__file__))+"/assets/placed.txt")) as file:
		company_name = file.read()
		context = {
			'company_name' : company_name,
		}
	return render(request, 'Login/placement.html', context)

def upload(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()

			resume_name = str(request.FILES['document'])
			if resume_name == "":
				enable = False
				context = {
					'enable' : enable,
				}
				return render(request, 'Login/main.html', context)
			else:
				skill_extract.run(resume_name)
				command = str(os.path.dirname(os.path.realpath(__file__))+"/assets/train.py")
				command = "python3 " + command
				os.system(command)
				return place(request)
		return render(request, 'Login/model_form_upload.html', {'form': form })
		######################
		

def evaluate(request):
	if request.method == 'POST':
		form = request.POST
		count = 0
		if form.__getitem__('naidu') == "naidu":
			count += 1
		if form.__getitem__('sweden') == "sweden":
			count += 1
		if form.__getitem__('kylie') == "kylie":
			count += 1
		if form.__getitem__('pewdiepie') == "pewdiepie":
			count += 1
		if form.__getitem__('france') == "france":
			count += 1

		if count >= 3:
			enable = True
			context = {
			'enable' : enable,
			}
			return render(request, 'Login/main.html', context)
		else:
			enable = False
		context = {
			'enable' : enable,
		}
		return render(request, 'Login/main.html', context)

def execute_query(request):
	if request.method == 'POST':
		data = Clients()
		form = request.POST
		if form.__getitem__('username') == "" or form.__getitem__('password') == "":
			return render(request, 'Login/register.html')
		data.first_name = form.__getitem__('fname')
		data.last_name = form.__getitem__('lname')
		data.user_name = form.__getitem__('username')
		data.contact = form.__getitem__('Contact')
		data.password = form.__getitem__('password')
		data.save()
		return render(request, 'Login/login.html')

	if request.method == 'GET':
		all_users = Clients.objects.all()
		form = request.GET
		for user in all_users:
			if form.__getitem__('username') == user.user_name and form.__getitem__('password') == user.password:
				### go to main page
				return call_main(request)
				
		return render(request, 'Login/login.html')

		