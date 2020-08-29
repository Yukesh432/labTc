from django.urls import path
from . import views

urlpatterns= [
    path('', views.product, name= 'products'),
    path('product-view/', views.productview, name= 'productview'),
    # path('<int:microcontroller_id>', views.microcontrollerid, name= 'microcontrollerid'),

]
