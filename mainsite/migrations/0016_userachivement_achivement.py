# Generated by Django 2.2.13 on 2020-11-16 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0015_achivement_userachivement'),
    ]

    operations = [
        migrations.AddField(
            model_name='userachivement',
            name='achivement',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='achivement', to='mainsite.Achivement'),
        ),
    ]