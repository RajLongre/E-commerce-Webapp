# Generated by Django 4.1.7 on 2023-05-06 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0008_costumerdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShirtOnetoOne',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='myshirt', serialize=False, to='estore.mensshits')),
                ('page_name', models.CharField(max_length=70)),
                ('image1', models.ImageField(upload_to='menss')),
                ('image2', models.ImageField(upload_to='menss')),
            ],
        ),
    ]