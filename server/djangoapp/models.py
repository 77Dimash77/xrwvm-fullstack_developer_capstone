from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='')
    description = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30, default='')
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('TRUCK', 'Truck'),
    ]
    type = models.CharField(null=False, max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        null=False,
        default=2023,
        validators=[MaxValueValidator(2023), MinValueValidator(2015)]
    )
    dealer_id = models.IntegerField(null=True)

    def __str__(self):
        return self.name
