from io import BytesIO
from pathlib import Path
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from PIL import Image
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
    image = models.ImageField('이미지', null=True, blank=True, upload_to='blog/%Y-%m-%d')
    thumbnail = models.ImageField('썸네일', null=True, blank=True, upload_to='blog/%Y-%m-%d/thumbnail')
    #ImageField, FieldField와 같지만 이미지만 업로드하게 되어있다.
    #varchar => 경로만 저장을 함

    def __str__(self):
        return f'[{self.get_catergory_display()}] {self.title[:10]}'
    
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'blog_pk': self.pk})
    
    def get_thumbnail_image_url(self):
        if self.thumbnail:
            return self.thumbnail.url
        elif self.image:
            return self.image.url
        return None

    
    def save(self, *args, **kwargs):
        if not self.image:
            return super().save(*args, **kwargs)

        image = Image.open(self.image)
        image.thumbnail((300, 300))

        image_path = Path(self.image.name) # Path 라이브러리를 사용해 이미지 경로를 가져옵니다

        thumbnail_name = image_path.stem # /blog/2024/8/13/database.png -> database
        thumbnail_extension = image_path.suffix # /blog/2024/8/13/database.png -> .png
        thumbnail_filename = f'{thumbnail_name}_thumb{thumbnail_extension}'

        if thumbnail_extension in ['.jpg', 'jpeg']:
            file_type = 'JPEG'
        elif thumbnail_extension == '.gif':
            file_type = 'GIF'
        elif thumbnail_extension == '.png':
            file_type = 'PNG'
        else:
            return super().save(*args, **kwargs)

        temp_thumb = BytesIO()
        image.save(temp_thumb, file_type)
        temp_thumb.seek(0)

        self.thumbnail.save(thumbnail_filename, temp_thumb, save=False)
        temp_thumb.close()
        return super().save(*args, **kwargs)


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