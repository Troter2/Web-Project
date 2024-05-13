"""
URL configuration for Web-Project project.

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
from django.urls import path, include

from accounts.views import admin_redirect, view_profile
from movies.views import homepage
from series.views import get_popular_series, serie_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin-redirect/', admin_redirect, name='admin_redirect'),
    path('', homepage, name='home'),
    path('reviews/', include('reviews.urls')),
    path('series/', get_popular_series, name='series'),
    path('serie-detail/<int:serie_id>/', serie_details, name='serie_details'),

]
