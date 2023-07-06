from django.urls import path

from .views import CharacterListView, CharacterDetailView

urlpatterns = [
    path(r'',
        CharacterListView.as_view(),
        name='api.characters.list'
    ),
    path(r'<id>/',
         CharacterDetailView.as_view(),
         name='api.characters.detail'
      ),
]
