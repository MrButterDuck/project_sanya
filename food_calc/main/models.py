from django.db import models

class Product(models.Model):
    product_name = models.CharField('Название продукта', max_length=100)
    kkal = models.IntegerField('Ккал')
    proteins  = models.IntegerField('Белки')
    fats  = models.IntegerField('Жиры')
    carbohydrates = models.IntegerField('Углеводы')

    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Recipe(models.Model):
    title = models.CharField('Название блюда', max_length=100)
    cooking_time = models.IntegerField('Время пригтовления')
    cooking_path = models.TextField('Описание приготовления')
    img_url = models.CharField('Ссылка картинки', max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

class ProductWeight(models.Model):
    product_id = models.ForeignKey(Product,  on_delete = models.CASCADE)
    recipe_id = models.ForeignKey(Recipe,  on_delete = models.CASCADE)
    product_weight = models.IntegerField('Вес продукта')

    def __str__(self):
        str_name = str(self.product_weight)
        return str_name
    
    class Meta:
        verbose_name = 'Вес продукта'
        verbose_name_plural = 'Вес продуктов'