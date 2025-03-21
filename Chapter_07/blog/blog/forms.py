from django import forms
from blog.models import Blog, Comment
from django_summernote.widgets import SummernoteWidget

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('catergory', 'title', 'content')
        widgets = {
            'content': SummernoteWidget()
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', ) # 넣은 모델에서 어떤 필드를 수정할지 정하는 필드
        widgets = { #안넣으면 기본값, 실제 화면에 어떻게 그려질지 나타냄
            'content': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'content':'댓글'
        }