from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.


class Profile(models.Model):
    MIN_LEN_VALIDATION_MESSAGE = "The username must be a minimum of 2 chars"

    username = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        validators=[
            MinLengthValidator(limit_value=2, message=MIN_LEN_VALIDATION_MESSAGE),
        ],
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=[MinValueValidator(limit_value=18), ],
        null=False,
        blank=False,
    )

    password = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )
    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    YEAR_ERROR_MESSAGE = "Year must be between 1980 and 2049"
    SPORTS = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"
    TYPE_CHOICES = (
        (SPORTS, SPORTS),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    type = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        choices=TYPE_CHOICES,
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=[
            MinLengthValidator(limit_value=2),
        ],
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MaxValueValidator(limit_value=2049, message=YEAR_ERROR_MESSAGE),
            MinValueValidator(limit_value=1980, message=YEAR_ERROR_MESSAGE),

        ],
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(limit_value=1),
        ],
    )
