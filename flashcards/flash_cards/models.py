from django.db import models

# Create your models here.


class Card(models.Model):
    word = models.CharField(max_length=50, default=None)
    definition = models.CharField(max_length=500, default=None)
    collection = models.ForeignKey('flash_cards.Collection', default=None, null=True, on_delete=models.CASCADE)


class Collection(models.Model):
    title = models.CharField(max_length=50)




