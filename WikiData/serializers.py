from rest_framework import serializers
import json
from .models import *



class MovieInstanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieInstance
        fields = ('movie','imdb_id','title','date')