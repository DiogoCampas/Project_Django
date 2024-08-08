
from django.urls import path
from .views import home, feed, squad, add_player

urlpatterns = [
     path('', home, name='home'),  # For function-based view
     path('feed/', feed, name='feed'),
     path('squad/', squad, name='squad'),
     path('add_player/', add_player, name='add_player')
]