# Generated by Django 3.2.8 on 2022-03-18 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graphql_api', '0002_actor_movies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='movies',
            new_name='title',
        ),
    ]
