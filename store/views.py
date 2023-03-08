from django.shortcuts import render

#Creating the views for different pages.
def home(request):
    return render(request, 'home.html')

def productPage(request):
    return render(request, 'product.html')
# Create your views here.
