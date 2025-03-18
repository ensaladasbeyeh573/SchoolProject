from django.shortcuts import render
from django.utils import timezone
from .models import Project

def index(request):
    projects = Project.objects.filter(published=True)
    return render(request, 'index.html', {'projects': projects})
