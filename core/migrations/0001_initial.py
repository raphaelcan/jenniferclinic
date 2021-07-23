# Generated by Django 3.2.5 on 2021-07-22 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZoomMeeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_id', models.IntegerField(unique=True)),
                ('nb_of_participants', models.IntegerField(default=0)),
            ],
        ),
    ]
