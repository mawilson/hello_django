# Generated by Django 4.2.5 on 2023-11-14 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survive', '0006_rename_fanfavorite_survivor_fan_favorite_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='rubric',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='survive.season', verbose_name='the season a team belongs to'),
        ),
        migrations.AddField(
            model_name='survivor',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='survive.season', verbose_name='the season a team belongs to'),
        ),
        migrations.AddField(
            model_name='team',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='survive.season', verbose_name='the season a team belongs to'),
        ),
    ]