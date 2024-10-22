from django.shortcuts import render
from django.views import View
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import random
from django.core.mail import send_mail
from renter.models import *
# Create your views here.

class home(View):
    def  get(self,request):
        un=request.session.get('username')
        if un:
            UO=User.objects.get(username=un)
            brands=Brand.objects.all()
            bikes=Bike.objects.all()
            d={'bikes':bikes,'brands':brands,'UO':UO}
            return render(request,'customer/home.html',d)
        return render(request,'customer/home.html')


class register(View):
    def get(self,request):
        ECFO=CustomerForm()
        EPFO=CustomerProfileForm()
        d={'ECFO':ECFO,'EPFO':EPFO}
        return render(request,'customer/register.html',d)
    def post(self,request):
        if request.FILES:
            CFDO=CustomerForm(request.POST)
            CPFDO=CustomerProfileForm(request.POST,request.FILES)
            if CFDO.is_valid() and CPFDO.is_valid():
                pw=CFDO.cleaned_data.get('password')
                MCFDO=CFDO.save(commit=False)
                MCFDO.set_password(pw)
                MCFDO.save()
                MCPFDO=CPFDO.save(commit=False)
                MCPFDO.username=MCFDO
                MCPFDO.save()
                return HttpResponseRedirect(reverse('customer_login'))
        return HttpResponse('invalid data')
        
class customer_login(View):
    def get(self,request) :
        return render(request,'customer/login.html')   

    def post(self,request):
        un=request.POST.get('un')    
        pw=request.POST.get('pw')  
        AUO=authenticate(username=un,password=pw)
        if AUO:
            login(request,AUO)
            request.session['username']=un
            return  HttpResponseRedirect(reverse('home'))
        return HttpResponse('authenticated user not found')
    

class customer_logout(View):
    #  def get(self,request):
    #        logout(request)
    #        return HttpResponseRedirect(reverse('home')) 
    def get(self,request):
          un=request.session.get('username')
          if un:
               logout(request)
               return HttpResponseRedirect(reverse('home')) 
          return HttpResponse('plaease login') 

    
class customer_profile(View):
    # def get(self,request):
    #     un=request.session.get('username')
    #     UO=User.objects.get(username=un)
    #     PO=CustomerProfile.objects.get(username=UO)
    #     d={'PO':PO,'UO':UO}
    #     return render(request,'customer/profile.html',d)
    def get(self,request):
        un=request.session.get('username')
        if un:
             UO=User.objects.get(username=un)
             PO=CustomerProfile.objects.get(username=UO)
             d={'PO':PO,'UO':UO}
             return render(request,'customer/profile.html',d)
        return HttpResponse('please login')
    
class forget_password(View): 
    def get(self,request):
        return render(request,'customer/forget_password.html')
    def post(self,request):
        un=request.POST.get('un')
        UO=User.objects.get(username=un)
        otp=random.randint(1000,9999)
        request.session['username']=un
        request.session['otp']=otp
        if UO:
            email=UO.email
            mesaage=f'your otp is {{otp}}'
            # send_mail(
            #     'your otp',
            #     mesaage,
            #     'kumarmanoj8260910@gmail.com',
            #     [email],
            #     fail_silently=False
            # )
            print(otp)
            return HttpResponseRedirect(reverse('otp'))
        return    HttpResponse('username not found') 
    
class otp(View):
    def get(self,request):
        return render(request,'customer/otp.html')
    def post(self,request):
        uotp=request.POST.get('uotp')
        sotp=request.session.get('otp')
        print(uotp)
        print(type(uotp))
        if uotp == str(sotp) :
            return HttpResponseRedirect(reverse('new_password'))
        return HttpResponse('invalid otp')
    
class new_password(View):
    def get(self,request):
         un=request.session.get('username')
         UO=User.objects.get(username=un)
         d={'UO':UO}
         return render(request,'customer/new_password.html',d) 
    def post(self,request):
        npw=request.POST.get('npw')   
        cpw=request.POST.get('cpw')   
        if npw == cpw :
            un=request.session.get('username')
            UO=User.objects.get(username=un)
            if UO:
              UO.set_password(cpw)
              UO.save()
              return HttpResponseRedirect(reverse('customer_login'))
            return HttpResponse('session expired')            
        return HttpResponse('password doesnot match')
    
class change_password(View):
    def get(self,request):
        un=request.session.get('username')
        UO=User.objects.get(username=un)
        d={'UO':UO}
        return render(request,'customer/change_password.html',d) 
    def post(self,request):
        un=request.session.get('username')
        UO=User.objects.get(username=un)
        email=UO.email
        otp=random.randint(1000,9999)
        request.session['otp']=otp
        print(email)
        print(otp)
        return HttpResponseRedirect(reverse('otp'))





   

    







       


    
            