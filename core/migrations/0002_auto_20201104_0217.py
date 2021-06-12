# Generated by Django 3.1.3 on 2020-11-04 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0001_initial'),
        ('address', '0001_initial'),
        ('comments', '0001_initial'),
        ('evaluations', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='touristspot',
            name='teste',
        ),
        migrations.AddField(
            model_name='touristspot',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='address.address'),
            preserve_default=False,
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
