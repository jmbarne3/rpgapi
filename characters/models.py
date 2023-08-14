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


class Equipment(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    magic_mod = models.IntegerField(null=False, blank=False, default=0)
    accuracy_mod = models.IntegerField(null=False, blank=False, default=0)
    evasion_mod = models.IntegerField(null=False, blank=False, default=0)
    speed_mod = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.name

    class Meta:
        abstract=True


class WeaponType(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    jobs_can_equip = models.ManyToManyField(Job)

    def __str__(self):
        return self.name


class Weapon(Equipment):
    attack = models.IntegerField(null=False, blank=False, default=0)
    weapon_type = models.ForeignKey(WeaponType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ArmorType(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    jobs_can_equip = models.ManyToManyField(Job)

    def __str__(self):
        return self.name
    

class Armor(Equipment):

    class ArmorSlot(models.TextChoices):
        HEAD = 'Head'
        BODY = 'Body'
        HANDS = 'Hands'
        FEET = 'Feet'

    defense = models.IntegerField(null=False, blank=False, default=0)
    armor_slot = models.CharField(max_length=5, null=False, blank=False, choices=ArmorSlot.choices)
    armor_type = models.ForeignKey(ArmorType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Character(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    experience_points = models.IntegerField(null=False, blank=False, default=0)
    level = models.IntegerField(null=False, blank=False, default=1, editable=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    # Equipment
    weapon = models.ForeignKey(Weapon, null=True, blank=True, on_delete=models.SET_NULL, related_name='characters_weapon_equipped')
    head = models.ForeignKey(Armor, null=True, blank=True, on_delete=models.SET_NULL, related_name='characters_head_equipped')
    hands = models.ForeignKey(Armor, null=True, blank=True, on_delete=models.SET_NULL, related_name='characters_hands_equipped')
    body = models.ForeignKey(Armor, null=True, blank=True, on_delete=models.SET_NULL, related_name='characters_body_equipped')
    feet = models.ForeignKey(Armor, null=True, blank=True, on_delete=models.SET_NULL, related_name='characters_feet_equipped')

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
    
    def calculate_stat(self, growth_rate) -> int:
        return math.floor(
            (5 * growth_rate) + (self.level * growth_rate)
        )

    @property
    def armor(self):
        return [
            self.head,
            self.body,
            self.hands,
            self.feet
        ]
    
    @property
    def equipment(self):
        return [self.weapon] + self.armor
    
    @property
    def strength(self):
        return self.calculate_stat(self.job.strength_mod)
    
    @property
    def dexterity(self):
        return self.calculate_stat(self.job.dexterity_mod)
    
    @property
    def agility(self):
        return self.calculate_stat(self.job.agility_mod)
    
    @property
    def vitality(self):
        return self.calculate_stat(self.job.vitality_mod)
    
    @property
    def intelligence(self):
        return self.calculate_stat(self.job.intelligence_mod)
    
    @property
    def mind(self):
        return self.calculate_stat(self.job.mind_mod)

    @property
    def attack(self):
        retval = math.floor(5 + (self.strength * self.level / 4))
        retval += self.weapon.attack if self.weapon is not None else 0
        return retval

    @property
    def defense(self):
        retval = math.floor(5 + (self.vitality * self.level / 4))
        retval += sum([x.defense for x in self.armor if x is not None])
        return retval

    @property
    def magic(self):
        retval = math.floor(
            2.5 + (self.intelligence * self.level / 8) + \
            2.5 + (self.mind * self.level / 8)
        )
        retval += sum([x.magic_mod for x in self.equipment if x is not None])
        return retval

    @property
    def accuracy(self):
        retval = math.floor(5 + (self.dexterity * self.level / 3))
        retval += sum([x.accuracy_mod for x in self.equipment if x is not None])
        return retval

    @property
    def evasion(self):
        retval = math.floor(5 + (self.agility * self.level / 3))
        retval += sum([x.evasion_mod for x in self.equipment if x is not None])
        return retval

    @property
    def speed(self):
        retval = math.floor(5 + (self.agility * self.level / 3))
        retval += sum([x.speed_mod for x in self.equipment if x is not None])
        return retval
