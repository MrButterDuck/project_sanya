from .models import *
from django.forms import *

class SearchForm(Form):
    CHOICES_S = [('M','Мужской'),('F','Женский')]
    CHOICES_A = [('min','Минимальная - Сидячая работа и нет физических нагрузок'),('low','Низкая - Редкие, нерегулярные тренировки, активность в быту'),('average','Средняя - Тренировки 3-5 раз в неделю'),('high','Высокая - Тренировки 6-7 раз в неделю'),('max','Очень Высокая - Больше 6 тренировок в неделю и физическая работа')]
    sex = ChoiceField(choices=CHOICES_S, widget=RadioSelect)
    age = IntegerField(widget=TextInput(attrs={'placeholder': 'Ваш возраст'}))
    height = IntegerField(widget=TextInput(attrs={'placeholder': 'Ваш рост'}))
    weight = IntegerField(widget=TextInput(attrs={'placeholder': 'Ваш вес'}))
    activity = ChoiceField(choices=CHOICES_A, widget=RadioSelect)