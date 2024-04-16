from django.db import models


class Flight(models.Model):
    gen = [("WOMEN", "women"), ("MEN", "men"), ("BOY", "boy"), ("GIRL", "girl")]
    candidate_name = models.CharField(max_length=20)
    mobile_no = models.IntegerField()
    gender = models.CharField(max_length=20, choices=gen)
    place = models.CharField(max_length=20)
    seat_no = models.CharField(max_length=10)
    fight_time = models.TimeField()
