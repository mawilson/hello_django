# Generated by Django 4.2.5 on 2024-03-14 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survive', '0029_alter_survivor_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survivor',
            name='season',
            field=models.ManyToManyField(blank=True, default=None, to='survive.season', verbose_name='a season a Survivor belongs to'),
        ),
        migrations.AlterField(
            model_name='survivor',
            name='team',
            field=models.ManyToManyField(blank=True, default=None, to='survive.team', verbose_name='a team that recruited this survivor'),
        ),
    ]
