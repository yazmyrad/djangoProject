from django.urls import path
from .views import profile_view
app_name = "register"
urlpatterns = [
    path('profile/<str:username>', profile_view, name='profile')
]