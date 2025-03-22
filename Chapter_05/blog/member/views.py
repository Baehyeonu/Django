
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import login as django_login
from django.urls import reverse
def sign_up(request):
    # username = request.POST.get('username')
    # password1 = request.POST.get('password1')
    # password2 = request.POST.get('password2')

    # print(f'username: {username}, password1: {password1}, password2: {password2}')

    #username 중복 확인 작업
    #패스워드가 맞는지, 그리고 패드워드 정책에 올바른지

    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL)
    
    # if request.method =='POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/accounts/login/')
    # else:
    #     form = UserCreationForm()

    context = {
        'form': form
    }
    template_name = 'registration/signup.html'
    return render(request, template_name, context)

def login(request):
    form = AuthenticationForm(request, request.POST or None)
    if form.is_valid():
        django_login(request, form.get_user())

        next = request.GET.get('next')
        if next:
            return redirect(next)

        return redirect(reverse('blog:list'))
    
    context = {
        'form':form
    }
    template_name = 'registration/login.html'
    return render(request, template_name, context)
