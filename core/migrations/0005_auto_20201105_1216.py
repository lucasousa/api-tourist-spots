# Generated by Django 3.1.3 on 2020-11-05 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0001_initial'),
        ('address', '0001_initial'),
        ('comments', '0001_initial'),
        ('evaluations', '0001_initial'),
        ('core', '0004_auto_20201105_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='touristspot',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='address.address'),
        ),
        migrations.AddField(
            model_name='touristspot',
            name='attractions',
            field=models.ManyToManyField(to='attraction.Attraction'),
        ),
        migrations.AddField(
            model_name='touristspot',
            name='comments',
            field=models.ManyToManyField(to='comments.Comment'),
        ),
        migrations.AddField(
            model_name='touristspot',
            name='evaluation',
            field=models.ManyToManyField(to='evaluations.Evaluation'),
        ),
    ]
