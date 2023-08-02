"""
URL configuration for potfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from mypro import views
app_name = 'mypro'
urlpatterns = [
    path('home', views.home, name='home'),
    path('index', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),

    ###for user registratio, sign-in sign-out
    path('info', views.info, name = 'info'),
    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login_reg'),
    path('logout', views.logoutuser, name = 'logout'),
    
    ###for product

    path('product', views.product, name='product'),
    path('products', views.products, name='products'),
    path('order/<int:id>', views.order, name='order'),
    path('kart', views.kart  , name='kart '),
   

]

