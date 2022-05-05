"""lab3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import RegistrUserView, send_friend_request, accept_friend_request, delete_friend, check_profile, ImageUploadView


urlpatterns = [
    path('registr/', RegistrUserView.as_view()),
    path('profile/', check_profile),
    path('profile/<int:id>', check_profile),
    path('profile/<pk>/submit', ImageUploadView.as_view()),
    path('profile/send_friend_request/<int:id>', send_friend_request),
    path('profile/accept_friend_request/<int:id>', accept_friend_request),
    path('profile/delete_friend/<int:id>', delete_friend),

]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


