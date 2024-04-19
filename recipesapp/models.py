from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.CharField(max_length=50)
    image = models.ImageField(upload_to='recipes/', default='default.jpg')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=50)


class RecipeCategoryLink(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
