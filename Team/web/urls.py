
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("service/",views.service,name="service"),
    path("blog/",views.blog,name="blog"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("service_detail/",views.service_detail,name="service_detail"),
    path("service_detail2/",views.service_detail2,name="service_detail2"),
    path("service_detail3/",views.service_detail3,name="service_detail3"),
    path("service_detail4/",views.service_detail4,name="service_detail4"),
    path("service_detail5/",views.service_detail5,name="service_detail5"),
    path("service_detail6/",views.service_detail6,name="service_detail6"),
]
