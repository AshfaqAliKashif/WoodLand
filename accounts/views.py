from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def service(request):
    return render(request, 'service.html')
def gallery(request):
    return render(request, 'gallery.html')
def contact(request):
    return render(request, 'contact.html')
def booking(request):
    return render(request, 'booking.html')
def testimonial(request):
    return render(request, 'testimonial.html')
def financing(request):
    return render(request, 'financing.html')