from django.shortcuts import render, get_object_or_404 , redirect
from .models import BlogApp
# Create your views here.

def home(request):
    blogs = BlogApp.objects #쿼리셋
    return render(request, 'home.html', {"blogs" : blogs})
    
def detail(request,blog_id):
    details = get_object_or_404(BlogApp, pk = blog_id)
    return render(request, 'detail.html', {'details' : details})

def new(request):
    return render(request,'new.html', {'new' : new})

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    # title의 내용을 가져다 주는 역할을 하는 라인   
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    # 블로그를 작성한 시간대를 알려주는 라인
    blog.save()
    # 작성한 내용을 데이터베이스에 저장하라@!@

    return redirect('/blog/'+str(blog_id))
    # 특정 내-외부 url에 연결시켜주는 기능을 하는 함수이다.