"""
URL configuration for djangoProject2 project.

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
from .views import say_hello
from .views.say_hello import say_hello_with_name
# from .views.say_hello import say_hello
# we need to write in above format if we remove the line from __init__.py from views folder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', say_hello),
    path('say_hello/<name>', say_hello_with_name),
]
