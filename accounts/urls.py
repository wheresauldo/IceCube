from django.urls import path, include
# looks in any folder at this level views.py
from . import views
# create Login
from django.contrib.auth.views import LoginView, PasswordChangeView





# document all urls that will be handled by the accounts app


urlpatterns = [
    # path('takes account then the rest of it'), views_in_this_app.view for this url
    path('', views.home),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', LoginView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('register/', views.register, name="register"),
    path('profile/', views.view_profile, name="accounts/profile"),
    path('profile/edit', views.edit_profile, name="accounts/edit_profile"),
    #path('change-password/', PasswordChangeView.as_view()),
]