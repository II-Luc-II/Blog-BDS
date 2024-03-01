from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from Blog.forms.ContactForm import ContactForm
from Blog.forms.PostForm import PostForm
from Blog.models import Post
from django.contrib import messages
import os


def index(request):
    title = "Bonjour et bienvenue !"
    posts_list = Post.objects.all()

    paginator = Paginator(posts_list, 8)
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except:
        posts = paginator.page(1)

    return render(request, "blog/index.html", {
        "title": title,
        "posts": posts,
    })


def single_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/single_post.html", {"post": post})


def contact(request):
    if request.method == "POST":
        # traitement des données
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully")
            return redirect('contact')

    else:
        form = ContactForm()

    return render(request, "blog/contact.html", {'form': form})


@login_required
def dashboard_post(request):
    posts_list = Post.objects.filter(author=request.user)

    paginator = Paginator(posts_list, 8)
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except:
        posts = paginator.page(1)
    return render(request, 'blog/dashboard/post_index.html', {"posts": posts})


@login_required
def dashboard_posts_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/dashboard/post_view.html", {"post": post})


@login_required
def dashboard_posts_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        if request.POST.get('_method') == 'PUT':
            form = PostForm(request.POST, request.FILES, instance=post)
            if post.image:
                image_path = post.image.path
                if os.path.exists(image_path):
                    os.remove(image_path)
            if form.is_valid():
                form.save()
                messages.success(request, "Post has been updated !")
                return redirect('dashboard_post')
        else:
            form = PostForm(instance=post)
    else:
        form = PostForm(instance=post)

    return render(request, "blog/dashboard/post_new.html", {'form': form, 'post': post})


@login_required
def dashboard_posts_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES,)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post has been saved successfully !")
            return redirect('dashboard_post')
    else:
        form = PostForm()

    return render(request, "blog/dashboard/post_new.html", {'form': form})


@login_required
def dashboard_post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post.author != request.user:
        messages.error(request, "Vous n'êtes pas autorisé à supprimer ce message !")
        return redirect('dashboard_post')

    if request.method == "POST":
        if request.POST.get('_method') == 'DELETE':
            if post.image:
                image_path = post.image.path
                if os.path.exists(image_path):
                    os.remove(image_path)
            post.delete()
            messages.success(request, "Post has been deleted !")
    return redirect("dashboard_post")
