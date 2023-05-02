from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from WikiData.views import MovieInstanceView

router = routers.DefaultRouter()
router.register(r'movies', MovieInstanceView, 'Movies')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.urls))),
] 
