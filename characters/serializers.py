from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import (
    Character,
    Job,
    Weapon,
    Armor
)

class SimpleJobSerializer(serializers.ModelSerializer):
    detail_view = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = [
            'id',
            'name',
            'detail_view'
        ]

    def get_detail_view(self, obj):
        return reverse(
            'api.characters.jobs.detail',
            kwargs={'id': obj.id},
            request=self.context['request']
        )

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class SimpleWeaponSerializer(serializers.ModelSerializer):
    detail_view = serializers.SerializerMethodField()

    class Meta:
        model = Weapon
        fields = [
            'name',
            'detail_view'
        ]

    def get_detail_view(self, obj):
        return reverse(
            'api.characters.weapons.detail',
            kwargs={'id': obj.id},
            request=self.context['request']
        )

class WeaponSerializer(serializers.ModelSerializer):
    weapon_type = serializers.StringRelatedField(many=False)

    class Meta:
        model = Weapon
        fields = '__all__'


class SimpleArmorSerializer(serializers.ModelSerializer):
    detail_view = serializers.SerializerMethodField()

    class Meta:
        model = Armor
        fields = [
            'name',
            'detail_view'
        ]

    def get_detail_view(self, obj):
        return reverse(
            'api.characters.armor.detail',
            kwargs={'id': obj.id},
            request=self.context['request']
        )

class ArmorSerializer(serializers.ModelSerializer):
    armor_type = serializers.StringRelatedField(many=False)

    class Meta:
        model = Armor
        fields = '__all__'

class DynamicArmorSerializer(serializers.PrimaryKeyRelatedField):
    def __init__(self, armor_slot=None, **kwargs):
        self.slot = armor_slot
        super().__init__(**kwargs)

    def get_queryset(self):
        character = self.parent.instance
        queryset = Armor.objects.filter(
            armor_type__jobs_can_equip=character.job
        )

        if self.slot is not None:
            queryset = queryset.filter(armor_slot=self.slot)

        return queryset
    

class DynamicWeaponSerializer(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        character = self.parent.instance
        queryset = Weapon.objects.filter(
            weapon_type__jobs_can_equip=character.job
        )

        return queryset
    
class SimpleCharacterSerializer(serializers.ModelSerializer):
    job = serializers.PrimaryKeyRelatedField(
        queryset=Job.objects.all())
    job_details = SimpleJobSerializer(many=False, read_only=True)

    stats = serializers.SerializerMethodField()

    class Meta:
        model = Character
        fields = [
            'id',
            'job',
            'job_details',
            'name',
            'description',
            'stats',
            'experience_points',
            'level'
        ]

    def get_stats(self, obj):
        return {
            'strength': obj.strength,
            'dexterity': obj.dexterity,
            'agility': obj.agility,
            'vitality': obj.vitality,
            'intelligence': obj.intelligence,
            'mind': obj.mind,
            'attack': obj.attack,
            'defense': obj.defense,
            'magic': obj.magic,
            'accuracy': obj.accuracy,
            'evasion': obj.evasion,
            'speed': obj.speed
        }

class CharacterSerializer(serializers.ModelSerializer):
    job_details = serializers.SerializerMethodField()
    stats = serializers.SerializerMethodField()

    weapon = DynamicWeaponSerializer()
    weapon_details = serializers.SerializerMethodField()

    head = DynamicArmorSerializer(armor_slot=Armor.ArmorSlot.HEAD)
    head_details = serializers.SerializerMethodField()

    body = DynamicArmorSerializer(armor_slot=Armor.ArmorSlot.BODY)
    body_details = serializers.SerializerMethodField()

    hands = DynamicArmorSerializer(armor_slot=Armor.ArmorSlot.HANDS)
    hands_details = serializers.SerializerMethodField()

    feet = DynamicArmorSerializer(armor_slot=Armor.ArmorSlot.FEET)
    feet_details = serializers.SerializerMethodField()

    class Meta:
        model = Character
        fields = [
            'id',
            'job',
            'job_details',
            'name',
            'description',
            'stats',
            'weapon',
            'weapon_details',
            'head',
            'head_details',
            'body',
            'body_details',
            'hands',
            'hands_details',
            'feet',
            'feet_details',
            'experience_points',
            'level'
        ]

    def get_stats(self, obj):
        return {
            'strength': obj.strength,
            'dexterity': obj.dexterity,
            'agility': obj.agility,
            'vitality': obj.vitality,
            'intelligence': obj.intelligence,
            'mind': obj.mind,
            'attack': obj.attack,
            'defense': obj.defense,
            'magic': obj.magic,
            'accuracy': obj.accuracy,
            'evasion': obj.evasion,
            'speed': obj.speed
        }
    
    def get_job_details(self, obj: Character) -> dict:
        return SimpleJobSerializer(obj.job, context=self.context).data
    
    def get_weapon_details(self, obj: Character) -> dict:
        return SimpleWeaponSerializer(obj.weapon, context=self.context).data

    def get_head_details(self, obj: Character) -> dict:
        return SimpleArmorSerializer(obj.head, context=self.context).data

    def get_body_details(self, obj: Character) -> dict:
        return SimpleArmorSerializer(obj.body, context=self.context).data

    def get_hands_details(self, obj: Character) -> dict:
        return SimpleArmorSerializer(obj.hands, context=self.context).data

    def get_feet_details(self, obj: Character) -> dict:
        return SimpleArmorSerializer(obj.feet, context=self.context).data