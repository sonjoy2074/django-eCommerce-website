from django.urls import path
from App_Payment import views

app_name = 'App_Payment'

urlpatterns = [ 
 path('checkout/', views.checkout, name='checkout'),
 path('payment/', views.payment, name='payment'),
 path('status/', views.complete, name='complete'),
 path('purchase/<val_id>/<tran_id>', views.purchase, name='purchase'),
 path('order_view/', views.order_view, name='order'),
]