# Generated by Django 4.0.3 on 2022-07-18 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ean_code', models.FloatField()),
                ('product_id', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=200)),
                ('product_description', models.CharField(max_length=400)),
                ('product_price', models.FloatField()),
                ('product_image', models.CharField(max_length=400)),
                ('product_weight', models.CharField(max_length=200)),
                ('product_height', models.CharField(max_length=200)),
                ('product_length', models.CharField(max_length=200)),
                ('product_width', models.CharField(max_length=200)),
                ('product_url', models.CharField(max_length=400)),
                ('unit_type', models.CharField(max_length=64, null=True)),
            ],
        ),
    ]
