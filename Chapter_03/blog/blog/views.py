from django.shortcuts import render
from blog.models import Blog
from django.shortcuts import get_object_or_404

def blog_list(request): # 뷰는 기본적으로 request를 받는다.
    blogs = Blog.objects.all() # 전체 가져오는것 .all()
    visits = int(request.COOKIES.get('visits', 0)) + 1

    request.session['count'] = request.session.get('count', 0) + 1

    template_name = 'blog_list.html'
    context = {
        'blogs': blogs,
        'count': request.session['count'],
    }
    response = render(request, template_name , context)
    response.set_cookie('visits', visits)

    return response

def blog_detail(request, pk):
    # blog = Blog.objects.get(pk=pk) => 없는 pk 가 들어오면 오류
    blog = get_object_or_404(Blog, pk=pk)
    context = {
        'blog': blog
    }
    template_name = 'blog_detail.html'
    return render(request, template_name , context)