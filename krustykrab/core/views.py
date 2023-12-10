from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, ReviewForm
from .models import Review, Category, MenuItem

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = SignUpForm()
    context ={'form':form}
    return render(request, 'core/signup.html', context)


def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnot exists')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password incorrect')
    return render(request, 'core/login.html')

@login_required(login_url='login')
def logoutView(request):
    logout(request)
    return redirect('about')


def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('review')
        else:
            form = ReviewForm()

    reviews = Review.objects.all()
    context = {'reviews':reviews}
    return render(request, 'core/reviews.html',context)

def menu(request):
    # q = request.GET('q') if request.GET.get('q') != None else ''
    q=request.GET.get('q','')
    menus = MenuItem.objects.filter(category__name__icontains=q)
    categories = Category.objects.all()
    context = {'categories':categories, 'menus':menus}
    return render(request, 'core/menu.html',context)

@login_required(login_url='login')
def account(request):
    return render(request, 'core/account.html')

@login_required(login_url='login')
def edit_account(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.save()
        return redirect('account')
    return render(request, 'core/edit-account.html')
