from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    proj = Project.objects.all()
    return render(request, 'projects.html', {'projects': proj})

from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Message sent successfully!"
            return render(request, 'contact.html', {'form': ContactForm(), 'message': message})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
