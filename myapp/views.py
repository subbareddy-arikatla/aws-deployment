
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Musician
from .serializers import MusicianSerializer

class MusicianCreateView(APIView):
    
    def post(self, request):
        serializer = MusicianSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()   # creates new Musician in DB
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
