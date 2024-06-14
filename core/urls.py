from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('users/', views.user_list, name='user-list'),
    path('users/create/', views.user_create, name='user-create'),
    path('login/', views.login, name='login'),
    path('discussions/', views.discussion_list, name='discussion-list'),
    path('api/discussions/create/', views.discussion_create, name='discussion-create'),
    path('accounts/profile/', views.profile, name='profile'),
    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/users/create/', views.user_create, name='api-user-create'),

]
