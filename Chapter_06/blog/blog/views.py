from django.shortcuts import render
from blog.models import Blog
from django.shortcuts import get_object_or_404
from blog.forms import BlogForm
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.views.decorators.http import require_http_methods


def blog_list(request): # 뷰는 기본적으로 request를 받는다.
    blogs = Blog.objects.all().order_by('-created_at') # 전체 가져오는것 .all()

    q = request.GET.get('q')
    if q:
        blogs = blogs.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q)  
        )
        # blogs = blogs.filter(title__icontains=q)

    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    page_object= paginator.get_page(page)

    template_name = 'blog_list.html'
    context = {
        # 'blogs': blogs,
        'object_list': page_object.object_list,
        'page_obj': page_object,
    }
    response = render(request, template_name , context)

    return response

def blog_detail(request, pk):
    # blog = Blog.objects.get(pk=pk) => 없는 pk 가 들어오면 오류
    blog = get_object_or_404(Blog, pk=pk)
    context = {
        'blog': blog
    }
    template_name = 'blog_detail.html'
    return render(request, template_name , context)

@login_required() #settings.py 에 LOGIN_URL = '/accounts/login/'
def blog_create(request):
    
    form = BlogForm(request.POST or None)
    if form.is_valid():
        blog = form.save(commit=False)
        blog.author = request.user
        blog.save()
        return redirect(reverse('fb:detail',kwargs={'pk': blog.pk}))
    
    # if not request.user.is_authenticated:
    #     return redirect(reverse('login'))
    # if request.method == 'POST':
    #     form = BlogForm(request.POST)
    #     if form.is_valid():
    #         blog = form.save()
    #         return redirect(reverse('blog_detail',{'pk': blog.pk}))
    #     else:
    #         form = BlogForm()
    temlpate_name = 'blog_form.html'
    context = {'form':form}
    return render(request,temlpate_name,context)

@login_required()
def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk, author=request.user)

    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        blog = form.save()
        return redirect(reverse('fb:detail',kwargs={'pk': blog.pk}))

    template_name = 'blog_form.html'
    context = {
        'form': form,  # form.instance = blog
        }
    return render(request, template_name, context)
    # if request.user != blog.author:
    #     raise Http404

@login_required
@require_http_methods(['POST'])  # POST method 만 받아 올수 있다. get요청이 들어오면 오류가 나온다.
def blog_delete(request, pk):
    # if request.method != 'POST':
    #     raise Http404("Method Not Allowed")

    blog = get_object_or_404(Blog, pk=pk, author=request.user)
    blog.delete()

    return redirect(reverse('fb:list'))


