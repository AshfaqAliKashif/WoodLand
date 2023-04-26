from django.urls import path
from accounts.views import home_page, about, service, gallery, contact, booking, testimonial
urlpatterns = [
    path('',home_page, name='index'),
    path('about/',about, name='about'),
    path('services/',service, name='service'),
    path('gallery/',gallery, name='gallery'),
    path('contact/',contact, name='contact'),
    path('booking/',booking, name='booking'),
    path('testimonial/',testimonial, name='testimonial'),
]