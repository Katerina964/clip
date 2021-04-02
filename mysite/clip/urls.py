from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import HomePageView
from . import views


app_name = 'clip'
urlpatterns = [

    path('', HomePageView.as_view(), name='all'),
    path('crab/', views.category_crab, name='category_crab'),
    path('clip/<int:pk>/', views.detail, name='detail'),
    path('spring/', views.category_spring, name='category_spring'),
    path('cart', views.cart, name='cart'),
    path('in_cart', views.in_cart, name='in_cart'),
    path('manage_cart', views.manage_cart, name='manage_cart'),
    path('order', views.order, name='order'),
    path('emty_order', views.emty_order, name='emty_order'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
