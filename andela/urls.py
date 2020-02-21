"""andela URL Configuration

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

from rest_framework.urlpatterns import format_suffix_patterns

import eng.views
# router = DefaultRouter()
# router.register(r'engs', eng.views.Index, basename='user')

engurls = [
    path('eng/', eng.views.CreateEngView.as_view()),
    path('eng/<int:pk>/', eng.views.GetEngView.as_view()),
    path('partner/', eng.views.CreatePartnerView.as_view()),
    path('partner/<int:pk>/', eng.views.GetPartnerView.as_view())

]

urlpatterns = format_suffix_patterns(engurls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urlpatterns))
]
