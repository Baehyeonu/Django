from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView
from member.forms import SignupForm

#User = get_user_model()
from django.contrib.auth import get_user_model

#이메일
from django.core.signing import TimestampSigner, SignatureExpired
from django.core import signing
from utils.email import send_email

User = get_user_model()

class SignupView(FormView):
    template_name = "auth/signup.html"
    form_class = SignupForm
    # success_url = reverse_lazy('signup_done')

    def form_valid(self, form):
        user = form.save()
        #이메일 발송
        signer = TimestampSigner()
        signed_user_email = signer.sign(user.email)
        signer_dump = signing.dumps(signed_user_email)

        # decoded_user_email = signing.loads(signer_dump)
        
        # email = signer.unsign(decoded_user_email, max_age=60 *30)
        url = f'{self.request.scheme}://{self.request.META["HTTP_HOST"]}/verify/?code={signer_dump}'
        print(url)

        subject = '[Pystgram]이메일 인증을 완료해주세요'
        message = f'다음 링크를 클릭해 주세요 <br><a href="{url}">{url}</a>'

        send_email(subject, message, user.email)

        return render(
            self.request,
            template_name='auth/signup_done.html',
            context={'user': user}
        )
    
def verify_email(request):
    code = request.GET.get('code', '')

    signer = TimestampSigner()
    try:
        decoded_user_email = signing.loads(code)
        email = signer.unsign(decoded_user_email, max_age=60 * 30)
    except (TypeError, SignatureExpired):
        return render(request, 'auth/not_verified.html')
    
    user = get_object_or_404(User, email=email, is_active=False)
    user.is_active = True
    user.save()
    return render(request, 'auth/email_verified_done.html', {'user': user})