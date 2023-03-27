from rest_framework import serializers

from .models import Anemone, Color, Coral, Fish, Habitat, Shark, Species


class HabitatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitat
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class SpeciesSerializer(serializers.ModelSerializer):
    habitats = HabitatSerializer(many=True)
    colors = ColorSerializer(many=True)

    class Meta:
        model = Species
        fields = '__all__'


class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = '__all__'


class SharkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shark
        fields = '__all__'


class AnemoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anemone
        fields = '__all__'


class CoralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coral
        fields = '__all__'
