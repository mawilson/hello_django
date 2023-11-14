# Generated by Django 4.2.5 on 2023-11-14 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survive', '0005_survivor_winner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survivor',
            old_name='fanFavorite',
            new_name='fan_favorite',
        ),
        migrations.RenameField(
            model_name='survivor',
            old_name='juryNumber',
            new_name='jury_number',
        ),
        migrations.RemoveField(
            model_name='rubric',
            name='fanFavorite',
        ),
        migrations.RemoveField(
            model_name='rubric',
            name='idolsWinner',
        ),
        migrations.RemoveField(
            model_name='rubric',
            name='juryNumber',
        ),
        migrations.AddField(
            model_name='rubric',
            name='fan_favorite',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='rubric',
            name='finalist',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='rubric',
            name='idols',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='rubric',
            name='immunities',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='rubric',
            name='jury_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='survivor',
            name='finalist',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='survivor',
            name='immunities',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rubric',
            name='winner',
            field=models.IntegerField(default=5),
        ),
    ]