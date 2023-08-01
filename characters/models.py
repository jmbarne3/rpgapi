import math

from django.db import models

from .utils import clamp

# Create your models here.
class Job(models.Model):

    class GrowthRate(float, models.Choices):
        A = 2.0, 'A'
        B = 1.8, 'B'
        C = 1.6, 'C'
        D = 1.4, 'D'
        E = 1.2, 'E'
        F = 1.0, 'F'

    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    strength_mod = models.FloatField(null=False, blank=False, choices=GrowthRate.choices)
    dexterity_mod = models.FloatField(null=False, blank=False, choices=GrowthRate.choices)
    vitality_mod = models.FloatField(null=False, blank=False, choices=GrowthRate.choices)
    agility_mod = models.FloatField(null=False, blank=False, choices=GrowthRate.choices)
    intelligence_mod = models.FloatField(null=False, blank=False, choices=GrowthRate.choices)
    mind_mod = models.FloatField(null=False, blank=False, choices=GrowthRate.choices)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    experience_points = models.IntegerField(null=False, blank=False, default=0)
    level = models.IntegerField(null=False, blank=False, default=1, editable=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.level = self.get_level_from_xp(self.experience_points)
        super().save(*args, **kwargs)

    def get_level_from_xp(self, xp: int) -> int:
        level = math.floor(
            (self.experience_points / 50) ** (1 / 1.6)
        ) + 1
        return clamp(level, 1, 99)
