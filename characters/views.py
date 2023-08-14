from rest_framework import generics
from .models import (
    Character,
    Job,
    Weapon,
    Armor
)

from .serializers import (
    CharacterSerializer,
    JobSerializer,
    SimpleWeaponSerializer,
    WeaponSerializer,
    SimpleArmorSerializer,
    ArmorSerializer
)

# Create your views here.
class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetailView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    lookup_field = 'id'
    serializer_class = JobSerializer

class WeaponListView(generics.ListAPIView):
    queryset = Weapon.objects.all()
    serializer_class = SimpleWeaponSerializer

class WeaponDetailView(generics.RetrieveAPIView):
    queryset = Weapon.objects.all()
    lookup_field = 'id'
    serializer_class = WeaponSerializer

class ArmorListView(generics.ListAPIView):
    queryset = Armor.objects.all()
    serializer_class = SimpleArmorSerializer

class ArmorDetailView(generics.RetrieveAPIView):
    queryset = Armor.objects.all()
    lookup_field = 'id'
    serializer_class = ArmorSerializer

class CharacterListView(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class CharacterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    lookup_field = 'id'
    serializer_class = CharacterSerializer
