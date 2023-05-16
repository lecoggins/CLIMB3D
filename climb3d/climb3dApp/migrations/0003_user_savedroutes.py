# Generated by Django 4.1.7 on 2023-05-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climb3dApp', '0002_user_savedcrags'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='savedRoutes',
            field=models.ManyToManyField(blank=True, related_name='saved_routes', to='climb3dApp.route'),
        ),
    ]
