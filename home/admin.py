from django.contrib import admin
from .models import PersonalInformation, Project, TechStack, Testimony, Inquiry

admin.site.register(PersonalInformation)
admin.site.register(Project)
admin.site.register(TechStack)
admin.site.register(Testimony)
admin.site.register(Inquiry)