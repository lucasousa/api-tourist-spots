from django.db import models

class Attraction(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    businnes_hours = models.TextField()
    minimum_age = models.IntegerField()
    image = models.ImageField(upload_to='attractions', blank=True, null=True)

    def __str__(self):
        return self.name