"""django_course URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home.index, name='home'),
    path('categories/', views.categories.index, name='categories_index'),
    path('categories/create', views.categories.create, name='categories_create'),
    path('categories/store', views.categories.store, name='categories_store'),
    path('categories/edit/<int:id>', views.categories.edit, name='categories_edit'),
    path('categories/delete/<int:id>', views.categories.delete, name='categories_delete'),

    path('products/', views.products.index, name='products_index'),
    path('products/create', views.products.create, name='products_create'),
    path('products/store', views.products.store, name='products_store'),
    path('products/edit/<int:id>', views.products.edit, name='products_edit'),
    path('products/delete/<int:id>', views.products.delete, name='products_delete'),
]