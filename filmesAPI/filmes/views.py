from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

from .serializers import MovieSerializer
from .models import Movie

# Create your views here.
@api_view(['GET', 'POST'])
def films_list(request):
    if request.method == 'GET':
        movie = Movie.objects.all()     # get all the movies
        serializer = MovieSerializer(movie, many=True)  # serializer them
        return JsonResponse({"movies": serializer.data})    # return the Json
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():   # check if the data is valid
            print(f"is Valid, POST, from films_list!")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def films_detail(request, id):
    try:
        serializerMovie = Movie.objects.get(pk=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerializer(serializerMovie)   # pas the movie from models as a serializer format
        return Response(serializer.data)    # return it
    elif request.method == 'PUT':
        serializer = MovieSerializer(serializerMovie, data=request.data)
        if serializer.is_valid():   # check if it's a valid form
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializerMovie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

