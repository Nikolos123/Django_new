# Generated by Django 3.1.7 on 2021-04-20 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_product_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]