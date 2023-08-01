from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Character, Job

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

class CharacterSerializer(serializers.ModelSerializer):
    job = SimpleJobSerializer(many=False)

    class Meta:
        model = Character
        fields = '__all__'