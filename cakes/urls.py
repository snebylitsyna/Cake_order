from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='main'),
    path('client_main/', views.client_main, name='client_main'),
    # path('add_new/', views.add_new, name='add_new'),
    # path('good_info/<int:pk>/', views.good_info, name='good_info'),
    # # path('good_update/<int:pk>/', views.update, name='update'),
    # path('delete/<int:pk>/', views.delete, name='delete'),
    path('admin_edit/', views.admin_edit, name='admin_edit'),
    path('admin_edit/cities', views.CityListView.as_view(), name='city_list'),
    path('admin_edit/city/create', views.CityCreateView.as_view(), name='city_create'),
    path('admin_edit/shops', views.ShopListView.as_view(), name='shop_list'),
    path('admin_edit/shop/create', views.ShopCreateView.as_view(), name='shop_create'),
    path('admin_edit/shop/update/<int:pk>/', views.ShopUpdateView.as_view(), name='shop_update'),
    path('admin_edit/shop/conf_del_shop/<int:pk>/', views.conf_del_shop, name='conf_del_shop'),
    path('admin_edit/shop/delete/<int:pk>/', views.ShopDeleteView.as_view(), name='shop_delete'),
    path('admin_edit/goods', views.GoodListView.as_view(), name='good_list'),
    path('admin_edit/good/create', views.GoodCreateView.as_view(), name='good_create'),
    path('admin_edit/good/update/<int:pk>/', views.GoodUpdateView.as_view(), name='good_update'),
    path('admin_edit/good/conf_del_good/<int:pk>/', views.conf_del_good, name='conf_del_good'),
    path('admin_edit/good/delete/<int:pk>/', views.GoodDeleteView.as_view(), name='good_delete'),
    path('admin_edit/manufacturers', views.ManufacturerListView.as_view(), name='manufacturer_list'),
    path('admin_edit/manufacturer/create', views.ManufacturerCreateView.as_view(), name='manufacturer_create'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('cake_create/', views.cake_create, name='cake_create'),
    # path('order_create/', views.order_create, name='order_create'),
    path('cakes/', views.cakes, name='cakes')
]