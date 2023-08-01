from django.contrib import admin
from .models import Character, Job


# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass
