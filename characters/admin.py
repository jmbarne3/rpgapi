from django.contrib import admin
from .models import Character


# Register your models here.
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass
