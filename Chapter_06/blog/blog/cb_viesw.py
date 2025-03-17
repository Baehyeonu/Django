from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from blog.models import Blog
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy

class BloglistView(ListView):
    # model = Blog
    # queryset = Blog.objects.all().order_by('-created_at')
    queryset = Blog.objects.all()
    template_name = 'blog_list.html'     
    paginate_by = 10
    ordering = ('-created_at',)
    def get_queryset(self):
        queryset = super().get_queryset()
        q= self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(content__icontains=q)
            )
        return queryset
    
class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    # pk_url_kwarg = 'id' => pk가 id 값일대 사용

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(id__lte=50)
    
    # def get_object(selg, queryset=None):
    # object = super().get_object()
    # return object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'blog_form.html'
    fields = ('catergory','title', 'content')
    # success_url = reverse_lazy('cd_blog_list') 정적인 페이지로 갈때는 함수 success보다 이 코드

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_title'] = '작성'
        context['btn_name'] = '생성'
        return context
    
class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model = Blog
    template_name = 'blog_form.html'
    fields = ('catergory','title', 'content')
    
    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)

    #     if self.object.author != self.request.user:
    #         raise Http404
    #     return self.object

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            return queryset
        return queryset.filter(author=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_title'] = '수정'
        context['btn_name'] = '수정'
        return context


    # def get_success_url(self):
    #     return reverse_lazy('cd_blog_detail', kwargs={'pk': self.object.pk})

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            queryset = queryset.filter(author=self.request.user)
        return queryset
    
    def get_success_url(self):
        return reverse_lazy('blog:list')