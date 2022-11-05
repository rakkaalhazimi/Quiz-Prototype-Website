from django.contrib.auth import views as auth_views
from django.urls import path, include

from .views import LoginView, RegisterView, LogoutView

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("register", RegisterView.as_view(), name="register"),
    path("logout", LogoutView.as_view(), name="logout"),
    
    path(
        'password_reset', 
        auth_views.PasswordResetView.as_view(template_name="password_reset.html"), 
        name="password_reset"
    ),
    path(
        'accounts/password_reset/done', 
        auth_views.PasswordResetDoneView.as_view(), 
        name="password_reset_done"
    ),
    path(
        'accounts/reset/<uidb64>/<token>', 
        auth_views.PasswordResetConfirmView.as_view(), 
        name="password_reset_confirm"
    ),
    path(
        'accounts/reset/done', 
        auth_views.PasswordResetCompleteView.as_view(), 
        name="password_reset_complete"),
]