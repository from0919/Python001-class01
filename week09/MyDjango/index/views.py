from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse

###  从models取数据传给template  ###
from .models import Name
def index(request):
    # return HttpResponse("Hello Django!")
    return render(request,'index.html')
from .form import LoginForm
from django.contrib.auth import authenticate, login
def login2(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data 
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                # 登陆用户
                login(request, user)  
                # return HttpResponse('登录成功')
                return redirect('/')
                # return render(request,'result.html')
                # return index(request)
            else:
                return HttpResponse('用户密码错误')
    # GET
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'form2.html', {'form': login_form})