from django.db import models

from .constants import (BEHAVIOR_CHOICES, MARKINGS_CHOICES, SHAPE_CHOICES,
                        SIZE_CHOICES, HABITAT_CHOICES)


def get_species_image_path(instance, filename):

    return 'species_images/{}/{}/{}'.format(
        instance.__class__.__name__.lower(),
        instance.type.lower(), filename
    )


class Habitat(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    habitat_type = models.CharField(max_length=100, choices=HABITAT_CHOICES)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Species(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100, null=True)
    habitats = models.ManyToManyField(Habitat, blank=True)
    colors = models.ManyToManyField(Color, blank=True)
    markings = models.CharField(max_length=100, choices=MARKINGS_CHOICES, null=True)
    size = models.CharField(max_length=100, choices=SIZE_CHOICES, null=True)
    shape = models.CharField(max_length=100, choices=SHAPE_CHOICES, null=True)
    behavior = models.CharField(max_length=100, choices=BEHAVIOR_CHOICES, null=True)
    image = models.ImageField(upload_to='species_images/', null=True, blank=True)
    description = models.TextField(null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Fish(Species):
    behavior = models.CharField(max_length=100, choices=BEHAVIOR_CHOICES, null=True)
    type = models.CharField(max_length=100)


class Shark(Species):
    behavior = models.CharField(max_length=100, choices=BEHAVIOR_CHOICES, null=True)
    type = models.CharField(max_length=100)


class Anemone(Species):
    behavior = models.CharField(max_length=100, choices=BEHAVIOR_CHOICES, null=True)
    type = models.CharField(max_length=100)


class Coral(Species):
    TEXTURE_CHOICES = (
        ('smooth', 'Smooth'),
        ('rough', 'Rough'),
        ('bumpy', 'Bumpy'),
    )
    texture = models.CharField(max_length=100, choices=TEXTURE_CHOICES, null=True)
    type = models.CharField(max_length=100)
