from django.urls import path,include
import django.contrib.auth.urls
from . import views
from django.contrib.auth import views as auth_views
app_name = 'shop'
urlpatterns = [
        path('index/', views.index, name='index'),
        path('', views.products.product_list, name='product_list'),
        path ('accounts/',include('django.contrib.auth.urls')),
        path ('accounts/login/',auth_views.LoginView.as_view(template_name='shop/login.html')),
        path ('accounts/logout/',auth_views.LogoutView.as_view(template_name='shop/logout.html')),
        path('signup/',views.signup, name='signup'),
        path('product_detail/<int:product_id>/', views.products.product_detail, name= 'product_detail'),
        path('basket_add/<int:product_id>/', views.basket_add, name ='basket_add'),
        path('basket_remove/<int:product_id>/', views.basket_remove, name ='basket_remove'),
        path('basket/',views.basket, name ='basket'),
        path('search/',views.search, name= 'search'),
    ]