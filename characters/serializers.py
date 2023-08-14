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
            'id',
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
            'id',
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


class CharacterSerializer(serializers.ModelSerializer):
    job = SimpleJobSerializer(many=False, read_only=True)
    stats = serializers.SerializerMethodField()
    weapon = SimpleWeaponSerializer(read_only=True)
    head = SimpleArmorSerializer(read_only=True)
    body = SimpleArmorSerializer(read_only=True)
    hands = SimpleArmorSerializer(read_only=True)
    feet = SimpleArmorSerializer(read_only=True)

    class Meta:
        model = Character
        fields = [
            'id',
            'job',
            'name',
            'description',
            'stats',
            'weapon',
            'head',
            'body',
            'hands',
            'feet',
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