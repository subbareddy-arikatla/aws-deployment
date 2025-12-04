
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Musician
from .serializers import MusicianSerializer

class MusicianListCreateView(APIView):
    
    def get(self, request):
        musicians = Musician.objects.all()
        serializer = MusicianSerializer(musicians, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MusicianSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()   # creates new Musician in DB
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MusicianDetailView(APIView):

    def get_object(self, pk):
        try:
            return Musician.objects.get(pk=pk)
        except Musician.DoesNotExist:
            return None

    def get(self, request, pk):
        musician = self.get_object(pk)
        if not musician:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MusicianSerializer(musician)
        return Response(serializer.data)

    def put(self, request, pk):
        musician = self.get_object(pk)
        if not musician:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MusicianSerializer(musician, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        musician = self.get_object(pk)
        if not musician:
            return Response(status=status.HTTP_404_NOT_FOUND)
        musician.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
