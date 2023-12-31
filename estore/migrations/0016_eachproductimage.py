# Generated by Django 4.1.7 on 2023-05-08 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0015_rename_cat_allproduct_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='EachProductImage',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='allproduct', serialize=False, to='estore.allproduct')),
                ('image1', models.ImageField(upload_to='allproduct')),
                ('image2', models.ImageField(upload_to='allproduct')),
            ],
        ),
    ]
