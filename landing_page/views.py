from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from . import views
from .models import *
from django.urls import reverse
# Create your views here.

# Create your views here.

def error_404_view(request,exception):
	return render(request, 'landing_page/404.html')
def index(request):
    context = {}
    return render(request, "landing_page/index.html", context )


def about(request):
    context = {}
    return render(request, "landing_page/about.html", context )


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			data = Contact()
			data.name = form.cleaned_data['name']
			data.email = form.cleaned_data['email']
			data.phone = form.cleaned_data['phone']
			data.subject = form.cleaned_data['subject']
			data.message = form.cleaned_data['message']
			data.ip = request.META.get('REMOTE_ADDR')
			data.save()
			messages.success(request, "Your message has been delivered")
			return HttpResponseRedirect(reverse("contact"))

	form = ContactForm
	
	context = {'form':form}
	return render(request,  "landing_page/contact.html", context)

def primary(request):
	context = {}
	return render(request, "landing_page/primary.html", context)

def secondary(request):
	context = {}
	return render(request, "landing_page/secondary.html", context)

def gallery(request):
	context = {}
	return render(request, "landing_page/gallery.html", context)

def admission(request):
	context = {}
	return render(request, "landing_page/admission.html", context)

def facility(request):
	context = {}
	return render(request, "landing_page/facility.html", context)