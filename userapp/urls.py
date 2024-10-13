from django.urls import path
from .views import Login_view, home_view
urlpatterns = [
    path('login/', Login_view, name='login'),
    path('home/', home_view, name='home'),
]