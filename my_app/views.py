# Create your views here.
from django.shortcuts import render_to_response

def index(request):
	return render_to_response('index.html')

def home(request):
	return render_to_response('home.html')

def help(request):
	return render_to_response('help.html')

def about(request):
	return render_to_response('about.html')

def contact(request):
	return render_to_response('contact.html')
  
def signup(request):
	return render_to_response('signup.html')