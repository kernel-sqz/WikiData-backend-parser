from rest_framework import viewsets
from rest_framework import pagination

from .serializers import *
from .models import *
from WikiData.hooks.GetMoviesFromDB import getMoviesFromWiki


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class MovieInstanceView(viewsets.ModelViewSet):
    serializer_class = MovieInstanceSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        update = self.request.GET.get('update')
        title = self.request.GET.get('title')
        
        if update:
            getMoviesFromWiki()
        if title:
            return MovieInstance.objects.filter(title__startswith=title)
        return MovieInstance.objects.all()
