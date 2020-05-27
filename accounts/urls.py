from django.urls import path, include
# looks in any folder at this level views.py
from . import views

#trying from different tutorial
from django.contrib.auth import views as auth_views
# create Login
from django.contrib.auth.views import (
        LoginView, LogoutView, PasswordChangeView, PasswordResetView,
        PasswordResetConfirmView, PasswordResetDoneView,
        PasswordResetCompleteView
)





# document all urls that will be handled by the accounts app


urlpatterns = [
    # path('takes account then the rest of it'), views_in_this_app.view for this url
    path('', views.home),

    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logged_out/', LogoutView.as_view(template_name='accounts/logged_out.html'), name="logged_out"),

    path('register/', views.register, name="register"),

    path('profile/', views.view_profile, name="accounts/profile"),
    path('profile/edit', views.edit_profile, name="accounts/edit_profile"),

    path('change_password/', views.change_password, name='change_password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html'), name='password_reset'),

    # in password reset confirm, token is generated
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'), name='password_reset_done'),

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),


    ]