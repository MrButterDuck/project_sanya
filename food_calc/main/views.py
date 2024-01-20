from django.shortcuts import render, redirect
from .models import *
from math import *
from .forms import *


def index(request):
    recipes = Recipe.objects.all()
    result = []
    for rec in recipes:
        weight = 0
        kkal = 0
        P = 0
        F = 0
        C = 0
        prod_list = ''
        products = ProductWeight.objects.filter(recipe_id = rec.id)
        for prod in products:
            weight += prod.product_weight
            prod_obj = Product.objects.get(product_name = prod.product_id)
            kkal += prod_obj.kkal
            P += prod_obj.proteins
            F += prod_obj.fats
            C += prod_obj.carbohydrates
            prod_list += prod_obj.product_name + ", "
        result.append({'id': rec.id,'title': rec.title, 'time': rec.cooking_time, 'img': rec.img_url, 'kkal': round(kkal / weight * 100, 2), 'proteing': P, 'fat': F, 'carb': C, 'products': prod_list[:-2]})
    return render(request, 'main/result.html', {'recipes': result, 'title':'Все рецепты'})

def reg(request):
    return render(request, 'main/reg.html')

def auth(request):
    return render(request, 'main/auth.html')

def recipe(request, recipe_id):
    recipe = Recipe.objects.get(id = recipe_id)
    result = {}
    all_weight = 0
    kkal = 0
    P = 0
    F = 0
    C = 0
    prod_list = []
    products = ProductWeight.objects.filter(recipe_id = recipe.id)
    for prod in products:
        all_weight += prod.product_weight
        prod_obj = Product.objects.get(product_name = prod.product_id)
        kkal += prod_obj.kkal
        P += prod_obj.proteins
        F += prod_obj.fats
        C += prod_obj.carbohydrates
        prod_list.append({'product': prod_obj, 'weight': prod.product_weight})
    if P != 0:    
        P_ = round((kkal / all_weight * 100)/((P / all_weight * 100) / 4))
    else:
        P_ = 0
    if F != 0:  
        F_ = round((kkal / all_weight * 100)/((P / all_weight * 100) / 9))
    else:
        F_ = 0
    if C != 0:  
        C_ = round((kkal / all_weight * 100)/((P / all_weight * 100) / 4))
    else:
        C_ = 0
    result = {'recipe': recipe, 'products': prod_list, 'all_weight': all_weight, 'kkal': kkal, 'prot': P, 'fat': F, 'carb': C, 'kkal100': round(kkal / all_weight * 100), 'prot100': round(P / all_weight * 100), 'fat100': round(F / all_weight * 100), 'carb100': round(C / all_weight * 100),'prot_': P_, 'fat_': F_, 'carb_': C_}
    return render(request, 'main/menu_item.html', context = result)
     
def search(request):
    error = ''
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            factor = 0
            if (form.cleaned_data.get('sex') == 'M'):
                normal_weigth = (form.cleaned_data.get('height') - 110)
            else:
                normal_weigth = (form.cleaned_data.get('height') - 100)
            if(form.cleaned_data.get('age') >= 20 and form.cleaned_data.get('age') <= 30):
                normal_weigth -= normal_weigth * 0.11
            elif(form.cleaned_data.get('age') >= 50):
                normal_weigth += normal_weigth * 0.06

            if(form.cleaned_data.get('activity') == 'min'):
                factor = -10
            elif(form.cleaned_data.get('activity') == 'low'):
                factor = -5
            elif(form.cleaned_data.get('activity') == 'high'):
                factor = 5
            elif(form.cleaned_data.get('activity') == 'max'):
                factor = 10

            recipes = Recipe.objects.all()
            result = []
            title = ''
            for rec in recipes:
                weight = 0
                kkal = 0
                P = 0
                F = 0
                C = 0
                prod_list = ''
                products = ProductWeight.objects.filter(recipe_id = rec.id)
                for prod in products:
                    weight += prod.product_weight
                    prod_obj = Product.objects.get(product_name = prod.product_id)
                    kkal += prod_obj.kkal
                    P += prod_obj.proteins
                    F += prod_obj.fats
                    C += prod_obj.carbohydrates
                    prod_list += prod_obj.product_name + ", "
                if(abs(normal_weigth - form.cleaned_data.get('weight')) <= 10 and (kkal >= 400 and kkal <= 600)):
                    title = 'Рецепты для поддержания веса'
                    result.append({'id': rec.id,'title': rec.title, 'time': rec.cooking_time, 'img': rec.img_url, 'kkal': round(kkal / weight * 100, 2), 'proteing': P, 'fat': F, 'carb': C, 'products': prod_list[:-2]})
                elif(normal_weigth - form.cleaned_data.get('weight') < (0 + factor) and (kkal <= 400)):
                    title = 'Рецепты для похудения'
                    result.append({'id': rec.id,'title': rec.title, 'time': rec.cooking_time, 'img': rec.img_url, 'kkal': round(kkal / weight * 100, 2), 'proteing': P, 'fat': F, 'carb': C, 'products': prod_list[:-2]})
                elif(normal_weigth - form.cleaned_data.get('weight') > (0 - factor) and (kkal >= 600)):
                    title = 'Рецепты для набора веса'
                    result.append({'id': rec.id,'title': rec.title, 'time': rec.cooking_time, 'img': rec.img_url, 'kkal': round(kkal / weight * 100, 2), 'proteing': P, 'fat': F, 'carb': C, 'products': prod_list[:-2]})
            
            return render(request , 'main/result.html', {'recipes': result, 'title':title})
        else:
            error = 'Что-то пошло не так'


    form = SearchForm()
    return render(request, 'main/search.html', {'form': form, 'error': error})  