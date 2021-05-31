from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
	path('primary/', views.primary, name='primary'),
	path('secondary/', views.secondary, name='secondary'),
	path('gallery/', views.gallery, name='gallery'),
	path('admission/', views.admission, name='admission'),
	path('facility/', views.facility, name='facility'),
]