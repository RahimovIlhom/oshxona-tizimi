from django.urls import path
from .views import (professions_page,
                    cashier_view,
                    add_to_card,
                    remove_from_card,
                    products_ordered,
                    UpdatePartialPaymentView,
                    order_completed,
                    chef_view,
                    accountant_view,
                    accountant_view1,
                    accountant_view2,
                    categories_view,
                    CategoryCreateView,
                    CategoryUpdateView,
                    CategoryDeleteView,
                    products_view,
                    ProductCreateView,
                    ProductUpdateView,
                    ProductDeleteView,
                    )

urlpatterns = [
    path('', professions_page, name='profession'),
    path('cashier/', cashier_view, name='cashier'),
    path('add_to_card/<int:id>/', add_to_card, name='add_to_card'),
    path('remove_from_card/<int:id>/', remove_from_card, name='remove_from_card'),
    path('products_ordered/<ref_code>/', products_ordered, name='products_ordered'),
    path('partial_payment/<int:pk>/', UpdatePartialPaymentView.as_view(), name='partial_payment'),
    path('chef/', chef_view, name='chef'),
    path('chef/order_complete/<ref_code>', order_completed, name='order_completed'),
    path('accountant/day/', accountant_view, name='admin_page'),
    path('accountant/week/', accountant_view1, name='admin_page1'),
    path('accountant/month/', accountant_view2, name='admin_page2'),
    path('accountant/categories/', categories_view, name='categories'),
    path('accountant/categories/add/', CategoryCreateView.as_view(), name='create_category'),
    path('accountant/categories/update/<int:pk>/', CategoryUpdateView.as_view(), name='update_category'),
    path('accountant/categories/delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),
    path('accountant/products/', products_view, name='products'),
    path('accountant/products/add/', ProductCreateView.as_view(), name='add_product'),
    path('accountant/products/update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('accountant/products/delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]