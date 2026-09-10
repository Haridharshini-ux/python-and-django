from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from blog.models import post

def index(request):
    if not request.user.is_authenticated:
        return redirect("blog:customer_login")
    posts = post.objects.all()
    return render(request, "blog/index.html", {"blog_title": "Latest posts", "posts": posts})

def customer_login(request):
    if request.user.is_authenticated:
        return redirect("blog:admin_dashboard" if request.user.is_staff else "blog:index")
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get("username", ""), password=request.POST.get("password", ""))
        if user and user.is_active and not user.is_staff:
            login(request, user)
            return redirect("blog:index")
        messages.error(request, "Enter valid customer account details.")
    return render(request, "blog/login.html", {"login_type": "Customer", "admin_login": False})

def customer_signup(request):
    if request.user.is_authenticated:
        return redirect("blog:admin_dashboard" if request.user.is_staff else "blog:index")
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Your customer account has been created. Welcome to Postboard!")
        return redirect("blog:index")
    return render(request, "blog/signup.html", {"form": form})

def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect("blog:admin_dashboard")
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get("username", ""), password=request.POST.get("password", ""))
        if user and user.is_active and user.is_staff:
            login(request, user)
            return redirect("blog:admin_dashboard")
        messages.error(request, "Enter valid administrator account details.")
    return render(request, "blog/login.html", {"login_type": "Administrator", "admin_login": True})

def sign_out(request):
    logout(request)
    return redirect("blog:customer_login")

@login_required(login_url="blog:customer_login")
def details(request, prof_id):
    selected_post = get_object_or_404(post, pk=prof_id)
    return render(request, "blog/detail.html", {"post": selected_post})

def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin, login_url="blog:admin_login")
def admin_dashboard(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()
        image_url = request.POST.get("image_url", "").strip()
        if title and content:
            post.objects.create(title=title, content=content, image_url=image_url)
            messages.success(request, "Your post has been published.")
            return redirect("blog:admin_dashboard")
        messages.error(request, "A title and post content are required.")
    return render(request, "blog/admin_dashboard.html", {"posts": post.objects.all()})
