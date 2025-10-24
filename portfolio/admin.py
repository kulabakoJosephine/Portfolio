
# Register your models here.
from django.contrib import admin
from .models import HomeContent, About, Service, Skill, Project, ContactMessage

admin.site.register(HomeContent)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(ContactMessage)
