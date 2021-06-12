from django.db import models
from attraction.models import Attraction
from comments.models import Comment
from evaluations.models import Evaluation
from address.models import Address

class TouristSpot(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    aproved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction)
    comments = models.ManyToManyField(Comment)
    evaluation = models.ManyToManyField(Evaluation)
    address = models.ForeignKey(Address,on_delete=models.CASCADE, null=True, blank=True) #delete address when delete the tourist spot
    image = models.ImageField(upload_to='touristspots', blank=True, null=True)

    def __str__(self):
        return self.name
