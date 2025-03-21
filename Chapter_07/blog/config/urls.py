"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect, render
from member import views as member_views
from django.views.generic import TemplateView, RedirectView
from django.views import View

from blog import views
from blog import cb_viesw
# class AboutView(TemplateView):
#     template_name = 'about.html'

# class TestView(View):
#     def get(self, request):
#         return render(request, 'test_get.html')
#     def post(self, request):
#         return render(request, 'test_post.html')
        



urlpatterns = [
    path("admin/", admin.site.urls),

    path('', include('blog.urls')),
    path('fb/', include('blog.fbv_urls')),

    #auth
    path('accounts/', include("django.contrib.auth.urls")),
    path('signup/', member_views.sign_up, name = 'signup' ),
    path('login/', member_views.login, name='login'),

    # #about 페이지
    # path('about/', AboutView.as_view(), name = 'about'),
    # path('redirect/', RedirectView.as_view(pattern_name='about'), name = 'redirect'),
    # path('redirect2/', lambda req: redirect('about')) 사용할수 있지만 위 코드가 더 기능이 많다
    # path('test/', TestView.as_view(),name = 'test')
    
    #summernote
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
