# Generated by Django 4.2.5 on 2024-04-21 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survive', '0037_alter_season_rubric'),
    ]

    operations = [
        migrations.AddField(
            model_name='rubric',
            name='confessionals',
            field=models.IntegerField(default=2, verbose_name='The points awarded to the survivor who featured in the most confessionals.'),
        ),
        migrations.AddField(
            model_name='rubric',
            name='confessionals_tie_split',
            field=models.BooleanField(default=True, verbose_name='Whether ties in most confessionals split points. True means points are split, False means each survivor is rewarded the maximum value'),
        ),
    ]
