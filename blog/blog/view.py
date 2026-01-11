from django.http import HttpResponse
from django.shortcuts import render 
from otzivi.forms import ReviewForm
from otzivi.models import Review
from django.shortcuts import render, redirect


MENU = {"главная":"/","о блоге":"/about","посты":"/post","отзывы":"/otzivi"}
POST = {"пост1":"/post1","пост2":"/post2","пост3":"/post3"}

def index_page(request):
    title = "Главная страница"
    context = { "menu":MENU, "title": title}
    return render(request, "index.html", context)

def about_page(request): 
    title = "О блоге"
    context = { "menu":MENU, "title": title}
    return render(request, "about_page.html", context)

def otziv_page(request): 
    title = "Оставьте, Ваш отзыв"
    context = { "menu":MENU, "title": title}
    return render(request, "otzivi.html", context)

def post_page(request):
    title = "Посты"
    context = { "menu":MENU, "title": title}
    return render(request, "post_page.html", context)

def post1_page(request):
    title = "Пост1"
    context = { "menu":MENU, "title": title}
    return render(request, "post_1.html", context) 

def post2_page(request):
    title = "Пост2"
    context = { "menu":MENU, "title": title}
    return render(request, "post_2.html", context)

def post3_page(request):
    title = "Пост3"
    context = { "menu":MENU, "title": title}
    return render(request, "post_3.html", context)

def logo_image(request):
    with open('static/img/1.png', 'rb') as f:
        return HttpResponse(f.read(), content_type='image/png')
    
def otziv_page(request):
    title = "Оставьте ваш отзыв"
    
    reviews = Review.objects.filter(show_on_site=True)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('otziv_page')
    else:
        form = ReviewForm()
    
    context = {
        "menu": MENU,
        "title": title,
        "form": form,
        "reviews": reviews 
    }
    return render(request, "otzivi.html", context)