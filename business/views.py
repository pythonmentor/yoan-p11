from django.shortcuts import (
    render,
    redirect,
    get_list_or_404,
    reverse,
    get_object_or_404,
)
from django.http import HttpResponse
from .models import Product, Category, CategoriesProducts
from django.template import RequestContext
from decimal import *
from .food import Food
from .form import SearchFoodForm

# from django.template import loader


# Create your views here.
def index(request, message=False):
    """return the home template of our app"""
    # if request.args.get('context'):
    #     context = {'success_is_ok': request.args.get('context')}
    #     return render(request, 'business/index.html', context)
    form = SearchFoodForm()
    context = {'form': form}

    if message is not False:
        context['message'] = message

    return render(request, "business/index.html", context)


# def page_not_found_view(request, exception=None):
#     """
#     display an unic page 404
#     """
#     return render(request, 'business/404.html')


def results(request):
    """return the results of substitutions product"""
    # TODO se servir du nom de l'aliment à substituer pour retrouver les
    # informations sur les autres aliments

    product_name = request.GET.get('product_name')
    print("PRODUCT NAME : ", product_name)

    if product_name:
        food = Food(product_name)
        print('food ====== ', food)
        complete_product_and_its_categories = food.search_food_and_categories_by_product_name()

        if complete_product_and_its_categories == 'product not found':
            print('product not found')
            return redirect('index', message='Aucun produit ou catégorie associée trouvé')
            # TODO : message='aucune catégories ou produit trouvé'
            # créer un message en args pour pouvoir mettre des alertes
            # aux utilisateurs ! 
        # categories = complete_product_and_its_categories.categories
        # if len(categories) > 1:

        print("complete product and its categories : ", complete_product_and_its_categories)
        list_of_foods_substitute = food.substitute_food_by_foods_with_best_nutriscore(
            complete_product_and_its_categories
        )
        print('list_of_foods_substitute : ', list_of_foods_substitute)
        if list_of_foods_substitute == 'this product have the best nutriscore':
            return redirect('index')
        context = {
            "active_results": "active",
            "food_to_substitute": product_name,
            "origin_food_nutriscore": complete_product_and_its_categories.get('product').get('nutriscore'),
            "commune_category": 'a faire',
            "url_image": complete_product_and_its_categories.get('product').get('image_url'),
            "foods_substitute": list_of_foods_substitute,
        }
        return render(request, "business/results.html", context)

    print("product_name is empty")
    return redirect("index", message="Le nom du produit ne doit pas être vide")


def detail_food(request, food):
    """display the page detail of food in params"""
    # TODO se servir de food pour retrouver les infos concernant
    # l'aliment dans la base et les rendre à l'aide du contexte
    print("FOOD : ", food)

    # food_detail = get_object_or_404(Product, product_name=food)
    food_detail = {
        "name": "nutella",
        "nutriscore": "e",
        "level_gras": "high",
        "level_sugar": "low",
        "level_sel": "moderate",
        "level_satur_gras": "high",
        "link_open_food_fact": "https://fr.openfoodfacts.org/produit/3017620421006/nutella-ferrero",
        "category": "pâte à tartiner",
        "nutri_per_100g": "de la merde",
        "url_image": '"https://static.openfoodfacts.org/images/products/301/762/042/1006/front_fr.176.400.jpg',
    }

    context = {"food_detail": food_detail}
    return render(request, "business/food.html", context)
