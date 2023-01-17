from django.contrib import admin
from django.urls import path
from CryptoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.CoinsView.as_view(),name='home'),
    path('find/',views.search,name="search"),
    path('add_tofav/<pk>/<wr>/',views.fav_coin,name='folow'),
    path('login/',views.LoginUser.as_view(),name='log'),
    path('register/',views.RegistrationView.as_view(),name="reg"),
    path('logout/',views.logout_user,name="logout"),
    path('profile/',views.profile,name="prof"),
]
