# Generated by Django 4.2.5 on 2023-11-17 22:24

from django.db import migrations, models
import django.db.models.deletion
import survive.models


class Migration(migrations.Migration):

    dependencies = [
        ("survive", "0009_remove_rubric_season_season_rubric"),
    ]

    operations = [
        migrations.AlterField(
            model_name="season",
            name="rubric",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.SET_DEFAULT, to="survive.rubric"
            ),
        ),
    ]
