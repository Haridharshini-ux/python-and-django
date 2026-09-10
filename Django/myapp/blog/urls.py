from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.customer_login, name="customer_login"),
    path("signup/", views.customer_signup, name="customer_signup"),
    path("admin-login/", views.admin_login, name="admin_login"),
    path("logout/", views.sign_out, name="logout"),
    path("posts/<int:prof_id>/", views.details, name="post_detail"),
    path("manage-posts/", views.admin_dashboard, name="admin_dashboard"),
]
