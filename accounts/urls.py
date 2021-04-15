from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView
from django.contrib.auth import views as auth_views

urlpatterns=[
     #path('', include('django.contrib.auth.urls')),
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout"),
   

    path('password_reset',PasswordResetView.as_view(),name="password_reset"),
    path('password_reset/done',PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>',PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password_reset/complete/',PasswordResetCompleteView.as_view(),name="password_reset_complete"),

]
