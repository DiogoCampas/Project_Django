# Generated by Django 5.0.2 on 2024-08-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_alter_player_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='coach',
        ),
        migrations.AddField(
            model_name='team',
            name='district',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
