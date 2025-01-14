from django.db import models
from user_app.models import Client
from result_app.models import Result

class Favorites(models.Model):
    user = models.OneToOneField(Client, on_delete=models.CASCADE)

class Favorites_result(models.Model):
    favorites = models.ForeignKey(Favorites, related_name='favorite_result_set', on_delete=models.CASCADE)
    result = models.ForeignKey(Result, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.result.name}'