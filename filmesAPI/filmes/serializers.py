from rest_framework import serializers
from filmes.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie   # point to the Movie model
        fields = [      # indicate which fields inside Movie model
            'title',
            'yearRelease',
            'genre',
            'budgetCost',
            'countryOrigin',
            'description'
        ]
