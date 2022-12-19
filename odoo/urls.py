from django.urls import path

from . import views,products,pointofsale,inventory_adjustments,order_line,paymentmethod,paymentmethodSpecific

urlpatterns = [
    path('customers/', views.index, name='index'),
    path('products/', products.index, name='products'),
    path('pos/', pointofsale.pos, name='pos'),
    path('adjustments/', inventory_adjustments.index, name='adjustments'),
    path('line/<int:id>',order_line.pos_line, name='pos_line'),
    path('paymentmethod/',paymentmethod.payment, name='payment_method'),
    path('paymentmethodspecific/<str:id>',paymentmethodSpecific.payment_item, name='payment_method'),
]