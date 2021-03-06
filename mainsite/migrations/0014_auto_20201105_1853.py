# Generated by Django 2.2.13 on 2020-11-05 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0013_sphere_of_life_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sphere_of_life',
            name='career',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='Учеба\\Карьера'),
        ),
        migrations.AlterField(
            model_name='sphere_of_life',
            name='health',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='Здоровье'),
        ),
        migrations.AlterField(
            model_name='sphere_of_life',
            name='inside_world',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='Внутренний мир'),
        ),
        migrations.AlterField(
            model_name='sphere_of_life',
            name='relationships',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='Отношения'),
        ),
    ]
