from django.shortcuts import render

# Create your views here.

def Home_Page(request):
    return render(request, 'home/home.html')
def About_Page(request):
    return render(request, 'home/about.html')
