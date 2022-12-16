from django.shortcuts import render
from django.http import HttpResponse
from .models import Skill, Subskill

# Create your views here.
def home_view(request, *args, **kwargs):
    all_skills = Skill.objects.all()
    python_skill = all_skills.filter(title='Python')
    all_subskills = Subskill.objects.all()
    python_subskills = all_subskills.filter(skill=1)
    
    return render(request, "homepage.html", {'all':all_skills, 'python_subskills':python_subskills, 'python_skill':python_skill})