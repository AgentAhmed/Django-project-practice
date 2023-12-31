"""IIP URL Configuration

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
from IIP import views  # type: ignore
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/',views.aboutUs,name="about"),
    path('',views.homePage,name="home"),  # we are keeping it blank so that homePage open directly
    path('gallery/',views.gallery,name="gallery"),
    path('course/',views.course),
    path('contact-us/',views.contactUs,name="contact"),
    path('services/',views.service,name="service"),
    path('userform/',views.userForm,name="userform"),
    path('submitform/',views.submitform,name="submitform"),
    path('calculator/',views.calculator),
    path('evenodd/',views.evenodd),
    path('marks/',views.marks),
    path("newsdetails/<newsid>",views.newsDetails),
    path("saveenquiry/",views.saveEnquiry,name="saveenquiry"),
    # path('course/<int:courseid>', views.courseDetails),  # for integer value int
    # path('course/<str:courseid>', views.courseDetails),   # for string value str
    # path('course/<slug:courseid>', views.courseDetails),  # for slug values eg. @, abc-def etc
    path('course/<courseid>', views.courseDetails), # this will print all type  
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
