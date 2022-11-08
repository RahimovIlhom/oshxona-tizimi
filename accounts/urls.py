from django.urls import path
from .views import ChangeUserView, CreateUserView, AdminUserChangeView, all_users_view

urlpatterns = [
    path('editing/<int:pk>/', ChangeUserView.as_view(), name='editing'),
    path('admin/edit/<int:pk>', AdminUserChangeView.as_view(), name='admin_edit'),
    path('adduser/', CreateUserView.as_view(), name='adduser'),
    path('admin/users/', all_users_view, name='users'),
]