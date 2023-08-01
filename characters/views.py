from rest_framework import generics
from .models import Character, Job
from .serializers import CharacterSerializer, JobSerializer

# Create your views here.
class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetailView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    lookup_field = 'id'
    serializer_class = JobSerializer

class CharacterListView(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class CharacterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    lookup_field = 'id'
    serializer_class = CharacterSerializer
