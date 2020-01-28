from django.urls import path, re_path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',login_required(views.hello_world), name='list_products'),
    re_path(r'^product/(?P<pk>[0-9]+)/$',login_required(views.product_detail), name='product_detail'),
    re_path(r'^product/new',login_required(views.new_product), name='new_product'),
]