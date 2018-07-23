from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
	return render(request, 'login/index.html')

def register(request):
	# add function to search database if 
	errors = User.objects.registration_validator(request.POST)
	if len(errors):
		for key, value in errors.items():
			messages.error(request, value)
		print(errors)
		return redirect('/')
	else:
		User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
		user = User.objects.filter(email = request.POST['email'])
		request.session['user_id'] = user.values()[0]['id']
		request.session['user_first_name'] = user.values()[0]['first_name']
		request.session['user_last_name'] = user.values()[0]['last_name']
		request.session['user_email'] = user.values()[0]['email']
		return redirect('/success')

def login(request):
	if request.method == 'POST':
		errors = User.objects.login_validator(request.POST)
		if len(errors):
			for key, value in errors.items():
				messages.error(request, value)
			print(errors)
			return redirect('/')
		else:
			user = User.objects.filter(email = request.POST['email'])
			request.session['user_id'] = user.values()[0]['id']
			request.session['user_first_name'] = user.values()[0]['first_name']
			request.session['user_last_name'] = user.values()[0]['last_name']
			request.session['user_email'] = user.values()[0]['email']
			print(request.session.values())
			return redirect('/success')

def success(request):
	if 'user_id' in request.session:
		return render(request, 'login/success.html')
	else:
		return redirect('/')