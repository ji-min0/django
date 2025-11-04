from django.db import models

# Model = DB 테이블
# Field = DB 칼럼

class Bookmark(models.Model):
    name = models.CharField('이름', max_length=100)
    url = models.URLField('URL')
    created_at = models.DateTimeField('생성일시', auto_now_add=True)
    updated_at = models.DateTimeField('수정일시', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '북마크'
        verbose_name_plural = '북마크 목록'


# makemigrations => migration.py를 만듦. ( = git commit 느낌 )
# 실제 db에는 영향 없으나 db에 넣기 위한 정의를 하는 파일 생성

# migrate => migrations/ 폴더 안에 있는 migration 파일을 실제 db에 적용. ( = git push 느낌 )
