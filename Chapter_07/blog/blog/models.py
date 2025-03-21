from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from utils.models import TimestampModel

User = get_user_model()


class Blog(TimestampModel):
    CATEGORY_CHOICES =(
        ('free', '자유'),
        ('travel', '여행'),
        ('cat', '고양이'),
        ('dog', '강아지'),
    )

    catergory = models.CharField('카테고리', max_length=20, choices=CATEGORY_CHOICES, default='free')
    title = models.CharField('제목', max_length=100)
    content = models.TextField('본문')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #models.CASCADE :  같이 삭제
    #models.PROTECT : 삭제가 불가능함(유저를 삭제하려고할때 블로그가 있으면 유저 삭제가 불가능)
    #mdels.SET_NULL : NULL값을 넣습니다. 유저 삭제 시 블로그의 author가 이 null이 됨, NULL=True

    def __str__(self):
        return f'[{self.get_catergory_display()}] {self.title[:10]}'
    
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'blog_pk': self.pk})
    
# f'[{self.get_catergory_display()}] => 카테고리초이스중 free 가 아닌 자유를 출력하게 만든다
# {self.title[:10]}' => 제목의 글자를 제한한다.
    class Meta:
        verbose_name = '블로그'
        verbose_name_plural = '블로그 목록'

# 제목
# 본문
# 작성자
# 작성일
# 수정일
# 카테고리

class Comment(TimestampModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.CharField('본문', max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.blog.title} 댓글'
    class Meta:
        verbose_name='댓글'
        verbose_name_plural='댓글 목록'
        ordering = ('-created_at',)
    #블로그 정보, 댓글 내용, 작성자, 작성일자, 수정일자