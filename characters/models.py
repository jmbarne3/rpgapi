from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
