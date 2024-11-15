from django.shortcuts import render,get_object_or_404, redirect
from .models import Category,Guide
from django.contrib.auth import login,authenticate,logout
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm 

def home_page(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request,"./home.html",context)

def categories_page(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request,"./categories.html",context)


def guides_page(request):

    guides = Guide.objects.all()

    context = {
        'guides': guides,
    }

    return render(request,"./guides.html",context)


def guide_detail_page(request,pk):
    guide = get_object_or_404(Guide,pk=pk)
    context = {
        'guide': guide
    }
    return render(request,"./guide-detail.html",context)


def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login_page')
    else:
        form = NewUserForm()
    context = {
        'form': form
    }
    return render(request,"./sign-up.html",context)

def login_page(request):



    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home_page')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form
    }
    return render(request,"./login.html",context)


def logout_action(request):
    logout(request)
    return redirect('home_page')

def mashiny_page(request):
    cars = [
        {
            'name': 'Mercedes-Benz E 320',
            'price': '4 800 000 ₸',
            'year': 2003,
            'engine': '3.2 л',
            'fuel': 'бензин',
            'color': 'белый',
            'added_date': '02 октября',
            'image': 'images/gen1200 1.jpg',
        },
        {
            'name': 'Mitsubishi Galant',
            'price': '2 500 000 ₸',
            'year': 1998,
            'engine': '2.5 л',
            'fuel': 'бензин',
            'color': 'белый',
            'added_date': '03 октября',
            'image': 'images/mitsi.jpg',
        },
        {
            'name': 'BMW M4 G82',
            'price': '54 600 000 ₸',
            'year': 2020,
            'engine': '5.5 л',
            'fuel': 'бензин',
            'color': 'сталь',
            'added_date': '05 октября',
            'image': 'images/bmw.png',
        },
    ]
    return render(request, 'mashiny.html', {'cars': cars})


def car_detail(request, car_id):
    car_data = {
        1: {'name': 'Mercedes-Benz E 320', 'price': '4 800 000 ₸', 'year': '2003'},
        2: {'name': 'BMW 525', 'price': '5 300 000 ₸', 'year': '2007'},
        3: {'name': 'Mercedes-Benz CLS 63 AMG', 'price': '80 000 000 ₸', 'year': '2016'},
    }

    car = car_data.get(car_id, None)
    if car is None:
        return render(request, '404.html')

    return render(request, 'car_detail.html', {'car': car})


def ads_list(request):
    return render(request, 'ads_list.html')