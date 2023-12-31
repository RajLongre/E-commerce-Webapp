# Generated by Django 4.1.7 on 2023-05-07 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0010_tshirtonetoone'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='allproduct')),
                ('price', models.FloatField()),
                ('available', models.IntegerField()),
                ('desc', models.TextField()),
            ],
        ),
    ]
