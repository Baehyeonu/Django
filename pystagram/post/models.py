from django.contrib.auth import get_user_model
from django.db import models


from utils.models import TimestampModel

User = get_user_model()


class Post(TimestampModel):
    content = models.TextField('본문')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.user}] post'

    class Meta:
        verbose_name = '포스트'
        verbose_name_plural = '포스트 목록'


class PostImage(TimestampModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images') # 해당 이미지를 소유한 포스트를 나타내는 외래 키 필드로, Post 모델과 관계를 맺습니다.
    image = models.ImageField('이미지', upload_to='post/%Y/%m/%d')

    def __str__(self):
        return f'{self.post} image'

    class Meta:
        verbose_name = '이미지'
        verbose_name_plural = '이미지 목록'