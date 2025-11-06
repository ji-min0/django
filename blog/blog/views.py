from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect, reverse


from blog.models import Blog
from blog.forms import BlogForm
from django.views.decorators.http import require_http_methods


@login_required
def blog_create(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        blog = form.save(commit=False)
        blog.author = request.user
        blog.save()
        return redirect(reverse('blog_detail', kwargs={'pk': blog.pk}))

    return render(request, 'blog_create.html', {'form': form})

@login_required()
def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk, author=request.user)

    form = BlogForm(request.POST or None, instance=blog) # instance로 기초데이터 세팅
    if form.is_valid():
        blog = form.save()
        return redirect(reverse('blog_detail', kwargs={'pk': blog.pk}))

    context = {'blog': blog,
               'form' : form,
               }

    return render(request, 'blog_update.html', context)

@login_required()
@require_http_methods(['POST'])
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk, author=request.user)
    blog.delete()
    return redirect('blog_list')


def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    # visits = int(request.COOKIES.get('visits', 0)) + 1

    # request.session['count'] = request.session.get('count', 0) + 1

    q = request.GET.get('q')
    if q:
        blogs = blogs.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q)
        )

    paginator = Paginator(blogs, 10)

    page = request.GET.get('page')
    page_object = paginator.get_page(page)

    context = {
        'page_object': page_object,
        # 'blogs': blogs,
        # 'count': request.session['count'],
    }

    response = render(request, 'blog_list.html', context)
    # response.set_cookie('visits', visits)

    return response

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    return render(request, 'blog_detail.html', {'blog': blog})