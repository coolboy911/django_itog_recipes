# Generated by Django 5.0.4 on 2024-04-19 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='recipes/'),
        ),
    ]