from django.contrib import admin
from .models import Skill, Contact, Subskill

# Register your models here.
admin.site.register(Contact)
admin.site.register(Skill)
admin.site.register(Subskill)