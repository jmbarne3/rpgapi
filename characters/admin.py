from django.contrib import admin
from .models import (
    Character,
    Job,
    WeaponType,
    Weapon,
    ArmorType,
    Armor
)

# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass

@admin.register(WeaponType)
class WeaponTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    pass

@admin.register(ArmorType)
class ArmorTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Armor)
class ArmorAdmin(admin.ModelAdmin):
    pass

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass
