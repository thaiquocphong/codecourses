from django.shortcuts import render, redirect
from django.contrib import messages
from home.models import Article, Register

# Create your views here. 
def get_home(request):
    object_list = Article.objects.all()
    return render(request,'home.html', {'object_list': object_list})

def get_newsDetail(request, ID):
    object_item = Article.objects.get(id = ID)
    return render(request,'news_detail.html', {'object_item': object_item})

def get_about(request):
    return render(request,'about.html', {})

def get_courses(request):
    return render(request,'courses.html', {} )

def get_resources(request):
    return render(request,'resources.html', {} )

def get_team(request):
    return render(request,'team.html', {} )

def get_testimonial(request):
    return render(request,'testimonial.html', {} )

def get_contact(request):
    return render(request,'contact.html', {} )

def get_register(request):

    if request.method == "POST":
        hovaten = request.POST['hovaten']
        tenchame = request.POST['tenchame']
        diachi = request.POST['diachi']
        dienthoai = request.POST['dienthoai']
        gioitinh = request.POST['gioitinh']
        khoahoc = request.POST['khoahoc']
        thoigian = request.POST['thoigian']
        ngay = request.POST['ngay']

        register_item = Register()
        register_item.hovaten = hovaten
        register_item.tenchame = tenchame
        register_item.diachi = diachi
        register_item.dienthoai = dienthoai
        register_item.gioitinh = gioitinh
        register_item.khoahoc = khoahoc
        register_item.thoigian = thoigian
        register_item.ngay = ngay
        register_item.save()

        messages.success(request, 'Đăng ký học lập trình thử thành công!')
        return redirect('/')

    return render(request,'register.html', {})
