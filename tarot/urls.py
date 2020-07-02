"""tarot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include('app.game_date.urls')),
    path('api/', include('app.game_name.urls')),
    path('api/', include('app.game_tarot.urls')),
    path('api/', include('app.options.urls')),
    # path('', include(router.urls)),
    path('api/auth/', include('rest_auth.urls')),
    path('api/access/', include('rest_framework.urls')),
]
