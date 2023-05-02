from django.db import models

class MovieInstance(models.Model):
    movie = models.URLField()
    imdb_id = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    date = models.DateField()

    class Meta:
        unique_together = (
            'imdb_id','title','date',
        )