# Generated by Django 3.0.6 on 2020-06-07 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20200607_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='id_crew_member_1',
            field=models.ForeignKey(blank=True, default=' ', on_delete=django.db.models.deletion.CASCADE, related_name='crew_member_1', to='app.crew_member'),
        ),
    ]
