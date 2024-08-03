from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import  HttpResponse,render, redirect
from django.http import JsonResponse
from django.db.models import Q
from .forms import Messageform,Subscriberform
from .models import Blog,Service,Tag,Category,Portfolio,Partner,Testmonial,MetaInfo
from django.http import HttpResponseRedirect
from django.urls import resolve, reverse
from django.utils import translation
from django.urls.exceptions import Resolver404
from urllib.parse import urlparse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
import json 
import random
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response

def home(request):
    blogs = Blog.objects.filter(in_home=True)
    services = Service.objects.filter(in_home=True)
    portfolios = Portfolio.objects.filter(in_home=True)
    partners = Partner.objects.all()
    testmonials = Testmonial.objects.all()
    meta = MetaInfo.objects.filter(page_name="home").first()
    context = {
        'blogs':blogs,
        'services':services,
        'portfolios':portfolios,
        'partners':partners,
        'testimonials':testmonials,
        'meta':meta
    }

    return render(request,'index-4.html',context)

def about(request):
    partners = Partner.objects.all()
    meta = MetaInfo.objects.filter(page_name="about").first()
    context = {
        'meta':meta,
        'partners':partners,
    }
    return render(request,'about.html',context)

def blogs(request):
    blog_list = Blog.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()    
    recent_blogs = Blog.objects.all()[0:3]

    if request.GET.get('search'):
        search = request.GET.get('search')
        blog_list = blog_list.filter(Q(title__icontains=search) | Q(description__icontains=search))
        
    if request.GET.get('tag'):
        tag = request.GET.get('tag')
        blog_list = blog_list.filter(tag__slug=tag)
    
    if request.GET.get('category'):
        category = request.GET.get('category')
        blog_list = blog_list.filter(category__slug=category)

    paginator = Paginator(blog_list, 2)
    page = request.GET.get("page", 1)
    blogs = paginator.get_page(page)
    total_pages = [x+1 for x in range(paginator.num_pages)]
    blogs_count = Blog.objects.count()
 
    meta = MetaInfo.objects.filter(page_name="blogs").first()
    context = {
        'meta':meta,
        'categories':categories,
        'blogs':blogs,
        'total_pages':total_pages,
        'tags':tags,
        'recent_blogs':recent_blogs,
        'blogs_count':blogs_count
    }
    
    return render(request,'blog-2.html',context)

def blog(request,slug):
    blog = get_object_or_404(Blog,slug=slug)

    related_blogs = set(Blog.objects.filter(category=blog.category).exclude(id=blog.id))

    if len(related_blogs) < 3:
        tag = blog.tag.all()
        tag_related_blogs = set(Blog.objects.filter(tag__in=tag).exclude(Q(id=blog.id) | Q(id__in=[b.id for b in related_blogs])))
        related_blogs.update(tag_related_blogs)

    if len(related_blogs) < 3:
        additional_blogs = set(Blog.objects.exclude(Q(id=blog.id) | Q(id__in=[b.id for b in related_blogs])))
        additional_count = 3 - len(related_blogs)
        additional_blogs = random.sample(list(additional_blogs), min(len(additional_blogs), additional_count))
        related_blogs.update(additional_blogs)


    related_blogs = list(related_blogs)[:3]

    categories = Category.objects.all()
    tags = Tag.objects.all()

    blogs_count = Blog.objects.count()

    context = {
        'blog':blog,
        'related_blogs':related_blogs,
        'tags':tags,
        'categories':categories,
        'blogs_count':blogs_count
    }

    return render(request,'blog-details.html',context)

def services(request):
    services = Service.objects.all()
    meta = MetaInfo.objects.filter(page_name="services").first()
    context = {
        'meta':meta,
        'services':services
    }
    return render(request,'service.html',context)

def service(request,slug):
    services = Service.objects.all()[0:3]
    service = get_object_or_404(Service,slug=slug)
    context = {
        'service':service,
        'services':services
    }
    return render(request,'service-details.html',context)

def portfolios(request):
    portfolios = Portfolio.objects.all()
    meta = MetaInfo.objects.filter(page_name="portfolios").first()
    context = {
        'meta':meta,
        'portfolios':portfolios
    }
    return render(request,'case-study.html',context)

def portfolio(request,slug):
    portfolio = get_object_or_404(Portfolio,slug=slug)
    portfolios = Portfolio.objects.exclude(id=portfolio.id)[0:2]
    context = {
        'portfolio':portfolio,
        'portfolios':portfolios
    }
    return render(request,'case-study-details.html',context)

def contact(request):
    meta = MetaInfo.objects.filter(page_name="contact").first()
    context = {
        'meta':meta,
    }
    return render(request,'contact.html',context)

def message(request):
    if request.method == 'POST':
        newmessage = Messageform(request.POST)
        if newmessage.is_valid():
            newmessage.save()
            data = {'status': 'success','message': 'Məktubunuz uğurla göndərildi!'}
            return JsonResponse(data)
        else:
            print(newmessage.errors)
            return JsonResponse({'status': 'error', 'message': 'Form hataları var!', 'errors': newmessage.errors})
        
    else:
        return HttpResponse(status=405) 
    

def subscribe(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            form_data = {'email': email}
            newmessage = Subscriberform(form_data)

            if newmessage.is_valid():
                newmessage.save()
                response_data = {'status': 'success', 'message': 'Uğurlu əməliyyat!'}
                return JsonResponse(response_data)
            else:
                errors = newmessage.errors.as_json()
                return JsonResponse({'status': 'error', 'message': 'Form hataları var!', 'errors': errors})
        
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Geçersiz JSON verisi!'}, status=400)
    else:
        return HttpResponse(status=405)