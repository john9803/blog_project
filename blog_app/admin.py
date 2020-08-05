from django.contrib import admin
from .models import BlogApp
# Register your models here.
# from 을 사용할때는 파일이 같은 폴더에 위치한다면 .앞에 디렉토리를 따로 적어주지 않고 사용해도 같은 폴더라는 내용이므로 참고하자!

admin.site.register(BlogApp)

