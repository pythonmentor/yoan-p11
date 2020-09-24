# Generated by Django 3.0.7 on 2020-07-19 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("product_name", models.CharField(max_length=100)),
                ("nutriscore", models.CharField(max_length=100)),
                ("image", models.CharField(max_length=150)),
                ("fat", models.IntegerField()),
                ("saturated_fat", models.IntegerField()),
                ("sugars", models.IntegerField()),
                ("salt", models.IntegerField()),
                ("openfoodfacts_link", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_name", models.CharField(max_length=100)),
                (
                    "products",
                    models.ManyToManyField(
                        related_name="categories", to="business.Product"
                    ),
                ),
            ],
        ),
    ]
