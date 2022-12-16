from django.shortcuts import render
from django.http import HttpResponse
from .models import Skill, Subskill

# Create your views here.
def home_view(request, *args, **kwargs):
    all_skills = Skill.objects.all()
    python_skill = all_skills.filter(title='Python')
    webdev_skill = all_skills.filter(title='Web Development')
    all_subskills = Subskill.objects.all()
    python_subskills = all_subskills.filter(skill=1)
    webdev_subskills = all_subskills.filter(skill=2)
    sql_skill = all_skills.filter(title='SQL')
    sql_subskills = all_subskills.filter(skill=3)
    devops_skill = all_skills.filter(title='DevOps')
    devops_subskills = all_subskills.filter(skill=5)
    
    return render(request, "homepage.html", {'all':all_skills, 'python_subskills':python_subskills, 'python_skill':python_skill, 'webdev_subskills':webdev_subskills, 
    'webdev_skill':webdev_skill, 'sql_subskills':sql_subskills, 'sql_skill':sql_skill, 'devops_subskills':devops_subskills, 'devops_skill':devops_skill})