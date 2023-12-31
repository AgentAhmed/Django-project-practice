"""wscubetech URL Configuration

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
from django.urls import path
from wscubetech import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage,name="home"),    # we are keeping homepage url blank, now it will open direct
    path('about-us/', views.aboutUs,name="about"),
    path('contact/',views.contactUs,name="contact"),
    path('gallery/',views.gallery,name="gallery"),
    path('services/',views.services,name="services"),
    path('course/', views.courses),
    # # path('course/<str:courseid>', views.coursesDetails),  # for string value
    # # path('course/<int:courseid>', views.coursesDetails)   # for integer value
    # #path('course/<slug:courseid>', views.coursesDetails)    # for slug value   
    path('course/<courseid>', views.coursesDetails)   # if exact type is unknown, then just pass parameter,now you can enter values in any type

]
