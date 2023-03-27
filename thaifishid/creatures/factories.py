import factory

from .models import Anemone, Color, Coral, Fish, Habitat, Shark, Species


class HabitatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Habitat

    name = factory.Faker('word')
    description = factory.Faker('sentence')
    habitat_type = factory.Faker('word')


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Color

    name = factory.Faker('color_name')


class SpeciesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Species
        abstract = True

    name = factory.Faker('word')
    scientific_name = factory.Faker('sentence')
    markings = factory.Faker('word')
    size = factory.Faker('word')
    shape = factory.Faker('word')
    behavior = factory.Faker('word')
    image = factory.django.ImageField()
    description = factory.Faker('text')

    habitats = factory.RelatedFactory(HabitatFactory)
    colors = factory.RelatedFactory(ColorFactory)


class FishFactory(SpeciesFactory):
    class Meta:
        model = Fish

    behavior = factory.Faker('word')
    type = factory.Faker('word')


class SharkFactory(SpeciesFactory):
    class Meta:
        model = Shark

    behavior = factory.Faker('word')
    type = factory.Faker('word')


class AnemoneFactory(SpeciesFactory):
    class Meta:
        model = Anemone

    behavior = factory.Faker('word')
    type = factory.Faker('word')


class CoralFactory(SpeciesFactory):
    class Meta:
        model = Coral

    texture = factory.Faker('word')
    type = factory.Faker('word')
