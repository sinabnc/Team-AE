from django.shortcuts import render
from .models import Blog
# Create your views here.
def index(request):
    return render(request,"web/index.html")


def about(request):
    return render(request,"web/about.html")


def contact(request):
    return render(request,"web/contact.html")


def service(request):
    return render(request,"web/services.html")


def blog(request):
    blogs = Blog.objects.all()
    context = {"is_blog": True,
               "blogs": blogs}
    return render(request, "web/blog.html", context)


def blog_detail(request,slug):
    blog = Blog.objects.get(slug=slug)
    other_blogs = Blog.objects.all().exclude(slug=slug)
    context = {"is_blog": True,
               "blog": blog,
               "other_blogs": other_blogs}
    
    return render(request, "web/blog-details.html", context)


def service_detail(request):
    return render(request,"web/page-service-details.html")


def service_detail2(request):
    return render(request,"web/service-details-2.html")


def service_detail3(request):
    return render(request,"web/service-details-3.html")


def service_detail4(request):
    return render(request,"web/service-details-4.html")


def service_detail5(request):
    return render(request,"web/service-details-5.html")


def service_detail6(request):
    return render(request,"web/service-details-6.html")

