from django.urls import path
from .views import index, productos, signup_view, login_view, logout_view, profile_view, update_profile_view


urlpatterns = [
    path('', index, name='index'),
    path('productos/', productos, name='products'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('update-profile/', update_profile_view, name='update_profile')
]
