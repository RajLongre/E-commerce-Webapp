from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name="base"),
    path('signup',views.sign_up,name="signup"),
    path('signin',views.sign_in,name="signin"),
    path('logout',views.log_out,name="logout"),
    path('mens-tshirts',views.tshirts,name="tshirts"),
    path('mens-shirts',views.shirts,name="shirts"),
    path('womens-jackets',views.womens_jackets,name="womens-jackets"),
    path('womens-saree',views.womens_saree,name="womens-saree"),
    path('KidsToy',views.KidsToy,name="KidsToy"),
    path('buy-product/<int:id>',views.buy_product,name="buy-product"),
    path('search',views.search,name='search'),
    path('cart<int:id>',views.cart,name='cart'),
    path('buynow<int:id>',views.buynow,name='buynow'),
    path('showcart',views.showcart,name='showcart'),
    path('orderplaced',views.orderplaced,name='orderplaced'),
    path('profile',views.profile,name='profile'),
    path('address',views.address,name='address'),
    path('checkout',views.checkout,name='checkout'),
    path('order',views.order,name='order'),
    
    
    

]