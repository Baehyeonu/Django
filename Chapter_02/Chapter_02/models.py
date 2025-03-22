from django.db import models

# Model = DB의 테이블
# Field = DB의 컬럼

# 북마크
# 이름 => VARCHAR
# URL 주소 => VARCHAR

class Bookmark(models.Model):
    name = models.CharField('이름', max_length=100)
    url = models.URLField('URL')
    created_at = models.DateTimeField('생성일시',auto_now_add=True)
    updated_at = models.DateTimeField('수정일시',auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '북마크'
        verbose_name_plural = '북마크 목록'

# makemigrations => migration.py 파일을 생성
# 실제 DB에 영향 X => 실제 DB에 넣기 위한 정의를 하는 파일을 생성

# migrate => migrations/ 폴더 안에 있는 migration 파일들을 실제 DB에 적용을 합니다.

#makemigrations => 깃의 커밋 => github  적용 X(커밋 이력만 남음) => DB에 적용 X, 적용할 파일 생성
#migrate => 깃의 push => githun에 적용 O() => DB에 적용 O, migration 파일을 가지고 적용

