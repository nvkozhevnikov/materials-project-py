from marochnik.models import *

""" Подсчет количества материалов в категории на главной странице марочника """

def count_quantity_materils_category():
    categories = Categories.objects.all()

    for category in categories:
        quantity = Materials.objects.filter(subcategory__in=category.subcategories_set.all()).count()
        Categories.objects.filter(pk=category.pk).update(quantity_materials=quantity)

def count_quantity_materils_subcategory():
    subcategories = SubCategories.objects.all()

    for subcategory in subcategories:
        quantity = Materials.objects.filter(subcategory=subcategory).count()
        SubCategories.objects.filter(pk=subcategory.pk).update(quantity_materials=quantity)