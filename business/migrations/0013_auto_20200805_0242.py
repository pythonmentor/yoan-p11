# Generated by Django 3.0.7 on 2020-08-05 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0012_linkcategoriesproducts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LinkCategoriesProducts',
            new_name='CategoriesProducts',
        ),
        migrations.AlterModelTable(
            name='categoriesproducts',
            table='business_categories_products',
        ),
    ]