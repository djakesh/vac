from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from vac.forms import PostCreateForm
from vac.models import Category, Post


def main_page(request):
    categories = Category.objects.all()
    posts = Post.objects.filter()
    context = {
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'vac/index.html', context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return redirect('main_page')
    form = PostCreateForm()
    context = {
        'form': form
    }
    return render(request, 'vac/create_job.html', context)


def post_detail(request, pk):
    post = Post.objects.filter(id=pk).first()

    not_anonymous = not (isinstance(request.user, AnonymousUser))
    if not_anonymous and request.user == post.author:
        pass
    else:
        post.seen_amount += 1
        post.save()

    if request.user == post.author:
        author = True
    context = {
        'post': post,
        'author': author,
    }
    return render(request, 'vac/post_detail.html', context)



@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'vac/index.html',
                  context={'posts': page_obj})


def category_posts(request, pk):
    category = Category.objects.filter(id=pk).first()
    posts = Post.objects.filter(category=category, published=True)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'vac/category_vac.html',
                  context={'category': category, 'posts': page_obj})


def search(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(title__icontains=query)
    return render(request,'vac/index.html',
                  context={'posts': posts})


def post_delete(request, pk):
    post = Post.objects.filter(id=pk).first()
    post.delete()
    return redirect('my_posts')

