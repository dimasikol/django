from django.shortcuts import render
from django.views import generic
from ..models import user
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
class LkView(generic.View):
    def get(self,request,**kwargs):
        users = user.Users.objects.all()
        context = {'user': users,2:3}
        return render(request, "bShop/personal_account/lk.html",context=context)


class Login(generic.View):
    def get(self,request):
        return render(request,'bShop/personal_account/login.html')
    def post(self,request):
        user_name = request.POST['username']
        password = request.POST['password']
        user = login(request,username=user_name,password=password)
        if user is not None:
            login(request,user)
            context=user.Users.objects.get(pk=user.pk)
            return render(request,'bShop/personal_account/lk.html',context=context)
        return render(request,'bShop/personal_account/login.html')


class Register(generic.View):
    def get(self,request):
        return render(request,'bShop/personal_account/registration.html')
    def post(self,request):
        if request.method=='POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password,username=username)
            user.save()
            #context = user.Users.objects.get(pk=user.pk)
            return render(request, 'bShop/personal_account/lk.html')# context=context)

class ForgetPassword(generic.View):
    pass
class RecoveryPassword(generic.View):
    pass