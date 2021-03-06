# Generated by Django 3.1.7 on 2021-04-06 10:08

from django.db import migrations, models
import player.utils


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_song_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song',
            field=models.FileField(upload_to='song/song', validators=[player.utils.check_format]),
        ),
    ]
