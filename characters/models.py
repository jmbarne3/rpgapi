import math

from django.db import models

from .utils import clamp

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    experience_points = models.IntegerField(null=False, blank=False, default=0)
    level = models.IntegerField(null=False, blank=False, default=1, editable=False)

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
