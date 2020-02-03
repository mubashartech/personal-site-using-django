from django.shortcuts import render
from .models import Contact
# Create your views here.
def contact_View(request):
    if request.method=='POST':
        name_g = request.POST.get('name')
        email_g = request.POST.get('email')
        subject_g = request.POST.get('subject')
        message_g = request.POST.get('message')
        c = Contact(name = name_g, email= email_g, subject=subject_g, message = message_g)
        c.save()
        return render(request, 'contact/contact.html')
    else:
        return render(request, 'contact/contact.html')
