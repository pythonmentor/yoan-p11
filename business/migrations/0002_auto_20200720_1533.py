# Generated by Django 3.0.7 on 2020-07-20 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category_name'], 'verbose_name': 'Catégorie'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['product_name'], 'verbose_name': 'Produit'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='url_category',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.URLField(null=True, verbose_name="Url de l'image du produit"),
        ),
        migrations.AddField(
            model_name='product',
            name='product_url',
            field=models.URLField(null=True, unique=True, verbose_name='Url du produit'),
        ),
        migrations.AlterField(
            model_name='product',
            name='nutriscore',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
