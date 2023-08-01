from django.urls import path

from .views import (
    CharacterListView,
    CharacterDetailView,
    JobListView,
    JobDetailView
)

urlpatterns = [
    path(r'jobs/<id>/',
        JobDetailView.as_view(),
        name='api.characters.jobs.detail'
    ),
    path(r'jobs/',
        JobListView.as_view(),
        name='api.characters.jobs.list'
    ),
    path(r'<id>/',
        CharacterDetailView.as_view(),
        name='api.characters.detail'
    ),
    path(r'',
        CharacterListView.as_view(),
        name='api.characters.list'
    ),
]
