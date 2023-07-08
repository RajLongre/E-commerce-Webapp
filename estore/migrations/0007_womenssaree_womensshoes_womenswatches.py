# Generated by Django 4.1.7 on 2023-04-24 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0006_womensjackets'),
    ]

    operations = [
        migrations.CreateModel(
            name='WomensSaree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='WomensSaree')),
                ('price', models.FloatField()),
                ('available', models.IntegerField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WomensShoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='WomensShoes')),
                ('price', models.FloatField()),
                ('available', models.IntegerField()),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WomensWatches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='WomensWatches')),
                ('price', models.FloatField()),
                ('available', models.IntegerField()),
                ('desc', models.TextField()),
            ],
        ),
    ]