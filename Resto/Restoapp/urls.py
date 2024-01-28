from django.urls import path,include
from Restoapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path("",views.home),
    path("register",views.register),
    path("login",views.user_login),
    path("logout",views.user_logout),
    path("catfilter/<cv>",views.catfilter),
    # path("sort/<sv>",views.sort),
    path("range",views.range),
    path("detail/<pid>",views.product_detail),
    path("addtocart/<pid>",views.addtocart),
    path("cart",views.cart),
    path("remove/<cid>",views.removecart),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path('placeorder',views.placeorder),
    path('makepayment',views.makepayment),
    path('contact',views.contact),
    path('about',views.about_us),
    path('forgetpass',views.forget_password),


]


if settings.DEBUG:
   urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)