"""
URL configuration for twitch_modular_plugin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include
from roulette.views import RouletteGetView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('roulette/', RouletteGetView.as_view(), name='roulette_get'),
    path('roulette/<int:num_characters>', RouletteGetView.as_view(), name='roulette_get_num_characters'),
    path('<game>/roulette/', RouletteGetView.as_view(), name='roulette_get'),
    path('<game>/roulette/<int:num_characters>', RouletteGetView.as_view(), name='roulette_get_num_characters')
   
]
