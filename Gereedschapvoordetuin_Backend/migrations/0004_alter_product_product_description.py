# Generated by Django 4.0.3 on 2022-07-18 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gereedschapvoordetuin_Backend', '0003_alter_product_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.CharField(max_length=3600),
        ),
    ]
