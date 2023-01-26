from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('search/', views.search_view, name='search_view'),
    path('product/<int:pk>/', views.product_view, name='product_view'),
    path('comment/<int:pk>/', views.comment_add_view, name='comment_add_view'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('logout/', views.logout_view, name='logout_view'),
]
