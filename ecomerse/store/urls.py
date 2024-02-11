from django.contrib import admin
from django.urls import path
from .import views

app_name='store'

urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('login/',views.logine,name="login"),
    path('logout/',views.logoute,name="logout"),
    path('single_buy/',views.single_product,name="single_buy"),
    path('about/',views.about_us,name="about"),
    path('contact/',views.contact_us,name="contact"),
    path('', views.product_list, name='product_list'),
	path('cart/', views.view_cart, name='view_cart'),
	path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
	path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('forgot/',views.forgot_password,name="forgot"),
]
