from django.db import models


class Product(models.Model):
    """
    Product of categories : name, nutriscore, image...
    """
    product_name = models.CharField(max_length=300, unique=True)
    nutriscore = models.CharField(max_length=1, null=False)
    image_url = models.URLField(
        verbose_name="Url de l'image du produit",
        null=True)
    product_url = models.URLField(
        verbose_name="Url du produit",
        unique=True,
        null=False,
        default="aucune url trouvé")
    fat = models.IntegerField()
    saturated_fat = models.IntegerField()
    sugars = models.IntegerField()
    salt = models.IntegerField()
    # openfoodfacts_link = models.CharField(max_length=100)
    # TODO dans openfoodfacts on trouve ces informations à ce chemin
    # nutriments.get('salt'), nutriments.get('sugars') etc...

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Produit"
        ordering = ['product_name']


class Category(models.Model):
    """
    Category of product : name, url_category
    """
    category_name = models.CharField(max_length=300)
    products = models.ManyToManyField(Product, related_name='categories')
    url_category = models.URLField(
        verbose_name="Url de la categorie",
        unique=True,
        null=False)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Catégorie"
        ordering = ['category_name']
