from django.urls import path
from .views import MusicianListCreateView, MusicianDetailView

urlpatterns = [
    path('musicians/', MusicianListCreateView.as_view(), name='musician-list-create'),
    path('musicians/<int:pk>/', MusicianDetailView.as_view(), name='musician-detail'),
]
