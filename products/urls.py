from django.urls import path
from .views import (professions_page,
                    cashier_view,
                    accountant_view,
                    categories_view,
                    CategoryCreateView,
                    CategoryUpdateView,
                    CategoryDeleteView,
                    products_view,
                    ProductCreateView,
                    )

urlpatterns = [
    path('', professions_page, name='profession'),
    path('cashier/', cashier_view, name='cashier'),
    path('accountant/', accountant_view, name='admin_page'),
    path('accountant/categories/', categories_view, name='categories'),
    path('accountant/categories/add/', CategoryCreateView.as_view(), name='create_category'),
    path('accountant/categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='update_category'),
    path('accountant/categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),
    path('accountant/products/', products_view, name='products'),
    path('accountant/products/add/', ProductCreateView.as_view(), name='add_product'),
]