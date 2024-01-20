from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('auth', views.auth, name='auth'),
    path('reg', views.reg, name='reg'),
    path('article/<int:recipe_id>', views.recipe, name='article'),
    path('search', views.search, name='search')
]
