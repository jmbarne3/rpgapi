from django.urls import path

from .views import (
    CharacterListView,
    CharacterDetailView,
    JobListView,
    JobDetailView,
    WeaponListView,
    WeaponDetailView,
    ArmorListView,
    ArmorDetailView
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
    path(r'weapons/<id>/',
        WeaponDetailView.as_view(),
        name='api.characters.weapons.detail'
    ),
    path(r'weapons/',
        WeaponListView.as_view(),
        name='api.characters.weapons.list'
    ),
    path(r'armor/<id>/',
        ArmorDetailView.as_view(),
        name='api.characters.armor.detail'
    ),
    path(r'armor/',
        ArmorListView.as_view(),
        name='api.characters.armor.list'
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
