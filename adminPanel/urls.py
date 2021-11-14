from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('<int:id>', views.displayProduct, name='home'),
    path('panel', views.adminPanel, name='home'),
    path('adminView', views.adminView, name='adminView'),
    path('products', views.productsDetail, name='adminView'),
    path('getProducts', views.returnProductsToAdmin, name='productsToAdmin'),
    path('productEdit', views.editProduct, name='edit'),
    path('addProduct', views.addProduct, name='edit'),
    path('Register', views.registerUser, name='registration'),
    path('registerUser', views.addUser, name='userRegistration'),
    path('Users', views.adminUser, name='users'),
    path('getUsers', views.returnUsers , name='users'),
    path('editUser', views.editUser , name='userEdit'),
    path('updateUser', views.updateUser, name='updateUser'),
    path('authenticate', views.allowUser, name='allowUser'),
    path('addOrder', views.addOrder, name='addOrder'),
    path('checkUser', views.checkIfAuthenticated, name='checkUser'),
    path('checkout', views.checkout, name='checkout'),
    path('winner', views.winner, name='winner'),
    path('bidWinners', views.returnWinners, name='returnWinners'),
    path('returnBidProducts', views.returnBidProducts, name='returnBidProducts'),

    
]
    

  
