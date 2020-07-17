from django.urls import path
from . import views

# Add URLConf
urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('signup/', views.signup_request, name='signup'),
    path('logout/', views.logout_request, name='logout'),
]
