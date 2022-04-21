from django.db import models
from recipes.models import Recipe

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=20)
    recipes = models.ManyToManyField("recipes.Recipe", related_name="tags")

    def __str__(self):
        return str(self.name) + " " + str(self.recipes)
