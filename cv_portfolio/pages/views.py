from django.shortcuts import render
from django.http import HttpResponse
from .models import Skill

# Create your views here.
def home_view(request, *args, **kwargs):
    all_skills = Skill.objects.all
    return render(request, "homepage.html", {'all':all_skills})