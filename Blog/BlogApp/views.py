from django.shortcuts import render 
from django.http import HttpResponse
from .models import Article
from django.db.models import Q
# Create your views here.

def recipes(request):
    search_query = request.GET.get('search', '').strip()
    
    if search_query:
        keywords = search_query.split()
        
        query = Q()
        for keyword in keywords:
            query |= (
                Q(title__icontains=keyword) |
                Q(text__icontains=keyword) |
                Q(key_words__icontains=keyword)
            )
        
        recipes = Article.objects.filter(query).distinct().order_by('-add_time')
    else:
        recipes = Article.objects.all().order_by('-add_time')
    
    context = {
        'recipes': recipes,
        'search_query': search_query,
    }

    return render(request, "blog/Recipes.html", context)

def aboutme(request):
    return render(request,"blog/AboutMe.html")

def recipie(request,id):
    recipe = Article.objects.get(id=id)
    return render(request,"blog/Recipie.html",{"recipe":recipe})