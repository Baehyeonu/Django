from django.db import models

# 제목
# 본문
# 작성자
# 작성일
# 수정일
# 카테고리

class Blog(models.Model):
    CATEGORY_CHOICES =(
        ('free', '자유'),
        ('travel', '여행'),
        ('cat', '고양이'),
        ('dog', '강아지'),
    )

    catergory = models.CharField('카테고리', max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField('제목', max_length=100)
    content = models.TextField('본문')
    
    created_at = models.DateTimeField('작성일자', auto_now_add=True)
    updated_at = models.DateTimeField('수정일자', auto_now=True)

    def __str__(self):
        return f'[{self.get_catergory_display()}] {self.title[:10]}'
# f'[{self.get_catergory_display()}] => 카테고리초이스중 free 가 아닌 자유를 출력하게 만든다
# {self.title[:10]}' => 제목의 글자를 제한한다.
    class Meta:
        verbose_name = '블로그'
        verbose_name_plural = '블로그 목록'

