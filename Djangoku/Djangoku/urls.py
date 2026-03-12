"""
URL configuration for Djangoku project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from django.urls import include, path
from django.conf import settings
from Djangoku.views import home_view, item_detail_view, create_item_view, AboutView


urlpatterns = [
   path('home/', home_view, name='home'),
    path('item/<int:pk>/', item_detail_view, name='item-detail'),
    path('item/new/', create_item_view, name='item-create'),
    path('about/', AboutView.as_view(), name='about'),
]

if settings.DEBUG:
    # Include django_browser_reload URLs only in DEBUG mode
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
