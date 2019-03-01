"""datax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.conf.urls import url
from django_registration.backends.activation.views import RegistrationView
from assignment.forms import RegistrationFormUniqueEmailWithCaptcha

from assignment.views import index, about, search, account

urlpatterns = [
    path('', index, name="assignment_home"),
    path('admin/', admin.site.urls),
    path(r'accounts/register/',
        RegistrationView.as_view(
            form_class=RegistrationFormUniqueEmailWithCaptcha
        ),
        name='django_registration_register',
    ),
    path(r'accounts/', include('django_registration.backends.activation.urls')),
    path(r'accounts/', include('django.contrib.auth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('about/', about, name="assignment_about"),
    path('search/', search, name="assignment_search"),
    path('my_account', account, name="assignment_account"),
    path('', include('social_django.urls', namespace='social')),
]
