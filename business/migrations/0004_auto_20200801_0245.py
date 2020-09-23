# Generated by Django 3.0.7 on 2020-08-01 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_auto_20200720_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='category',
            name='url_category',
            field=models.URLField(unique=True, verbose_name='Url de la categorie'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
