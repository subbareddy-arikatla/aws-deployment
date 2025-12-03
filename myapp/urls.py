from django.urls import path
from .views import MusicianCreateView

urlpatterns = [
    path('musicians/create/', MusicianCreateView.as_view(), name='musician-create'),
]
