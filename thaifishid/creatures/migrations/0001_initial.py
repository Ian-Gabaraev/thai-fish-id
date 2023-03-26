# Generated by Django 4.1.7 on 2023-03-26 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Habitat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('habitat_type', models.CharField(choices=[('coral_reef', 'Coral Reef'), ('mangrove', 'Mangrove'), ('estuary', 'Estuary'), ('river', 'River'), ('lake', 'Lake'), ('pond', 'Pond')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('scientific_name', models.CharField(max_length=100, null=True)),
                ('markings', models.CharField(choices=[('black_spots', 'Spots'), ('black_blotches', 'Blotches'), ('stripes', 'Stripes'), ('bands', 'Bands')], max_length=100, null=True)),
                ('size', models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], max_length=100, null=True)),
                ('shape', models.CharField(choices=[('rounded', 'Rounded'), ('elongated', 'Elongated'), ('flat', 'Flat')], max_length=100, null=True)),
                ('image', models.ImageField(null=True, upload_to='species_images/')),
                ('behavior', models.CharField(choices=[('passive', 'Passive'), ('aggressive', 'Aggressive'), ('semi-aggressive', 'Semi-Aggressive')], max_length=100, null=True)),
                ('type', models.CharField(max_length=100)),
                ('colors', models.ManyToManyField(blank=True, to='creatures.color')),
                ('habitats', models.ManyToManyField(blank=True, to='creatures.habitat')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('scientific_name', models.CharField(max_length=100, null=True)),
                ('markings', models.CharField(choices=[('black_spots', 'Spots'), ('black_blotches', 'Blotches'), ('stripes', 'Stripes'), ('bands', 'Bands')], max_length=100, null=True)),
                ('size', models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], max_length=100, null=True)),
                ('shape', models.CharField(choices=[('rounded', 'Rounded'), ('elongated', 'Elongated'), ('flat', 'Flat')], max_length=100, null=True)),
                ('image', models.ImageField(null=True, upload_to='species_images/')),
                ('behavior', models.CharField(choices=[('passive', 'Passive'), ('aggressive', 'Aggressive'), ('semi-aggressive', 'Semi-Aggressive')], max_length=100, null=True)),
                ('type', models.CharField(max_length=100)),
                ('colors', models.ManyToManyField(blank=True, to='creatures.color')),
                ('habitats', models.ManyToManyField(blank=True, to='creatures.habitat')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Coral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('scientific_name', models.CharField(max_length=100, null=True)),
                ('markings', models.CharField(choices=[('black_spots', 'Spots'), ('black_blotches', 'Blotches'), ('stripes', 'Stripes'), ('bands', 'Bands')], max_length=100, null=True)),
                ('size', models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], max_length=100, null=True)),
                ('shape', models.CharField(choices=[('rounded', 'Rounded'), ('elongated', 'Elongated'), ('flat', 'Flat')], max_length=100, null=True)),
                ('behavior', models.CharField(choices=[('passive', 'Passive'), ('aggressive', 'Aggressive'), ('semi-aggressive', 'Semi-Aggressive')], max_length=100, null=True)),
                ('image', models.ImageField(null=True, upload_to='species_images/')),
                ('texture', models.CharField(choices=[('smooth', 'Smooth'), ('rough', 'Rough'), ('bumpy', 'Bumpy')], max_length=100, null=True)),
                ('type', models.CharField(max_length=100)),
                ('colors', models.ManyToManyField(blank=True, to='creatures.color')),
                ('habitats', models.ManyToManyField(blank=True, to='creatures.habitat')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Anemone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('scientific_name', models.CharField(max_length=100, null=True)),
                ('markings', models.CharField(choices=[('black_spots', 'Spots'), ('black_blotches', 'Blotches'), ('stripes', 'Stripes'), ('bands', 'Bands')], max_length=100, null=True)),
                ('size', models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], max_length=100, null=True)),
                ('shape', models.CharField(choices=[('rounded', 'Rounded'), ('elongated', 'Elongated'), ('flat', 'Flat')], max_length=100, null=True)),
                ('image', models.ImageField(null=True, upload_to='species_images/')),
                ('behavior', models.CharField(choices=[('passive', 'Passive'), ('aggressive', 'Aggressive'), ('semi-aggressive', 'Semi-Aggressive')], max_length=100, null=True)),
                ('type', models.CharField(max_length=100)),
                ('colors', models.ManyToManyField(blank=True, to='creatures.color')),
                ('habitats', models.ManyToManyField(blank=True, to='creatures.habitat')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
