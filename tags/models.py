from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20)
    recipes = models.ManyToManyField("recipes.Recipe", related_name="tags")

    def __str__(self):
        return str(self.name) + " plus " + str(self.recipes)


class Rating(models.Model):
    value = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ]
    )
    recipe = models.ForeignKey(
        "Recipe",
        related_name="ratings",
        on_delete=models.CASCADE,
    )
