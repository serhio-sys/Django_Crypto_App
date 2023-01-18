from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views import View
from django.views.generic import CreateView
from .models import Coin
from .forms import RegisterForm
import requests
from django.shortcuts import get_object_or_404
from django_celery_beat.models import CrontabSchedule,PeriodicTask,IntervalSchedule,ClockedSchedule
import datetime
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator

def generate(fr,to,req):
    for item in fr:
        nw = {}
        nw['pk']=item.pk
        nw['name']=item.name
        nw['symb']=item.symb
        nw['price']=item.price
        nw['img']=item.img
        nw['rank']=item.rank
        nw['market_up']=item.market_up
        if item.fav.filter(pk=req.user.pk).exists():
            nw['is_fav'] = True
        else:
            nw['is_fav'] = False
        nw['minfor24']=item.minfor24
        nw['maxfor24']=item.maxfor24 
        nw['to_up']=item.to_up
        to.append(nw)

class CoinsView(View):
    def get(self,request,*args, **kwargs):
        data = Coin.objects.order_by('id')
        nm = []
        if request.user.is_authenticated:
            generate(fr=data, to=nm,req=request)
        else:
            nm = data
        pag = Paginator(nm, 50)
        page_num = request.GET.get("page")
        page_obj = pag.get_page(page_num)
        return render(request=request, template_name='home.html',context={'data':page_obj,'name':"BIRZHA"})

@login_required
def fav_coin(request,pk):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        favorite = get_object_or_404(Coin,pk=pk)
        if favorite.fav.filter(pk=request.user.pk).exists():
            favorite.fav.remove(request.user)
        else:
            favorite.fav.add(request.user)
        return JsonResponse({},status=200)
    return redirect("home")

@login_required
def logout_user(request):
    logout(request)
    return redirect('log')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    extra_context = {"text":"Login"}
    template_name = 'log.html' 

class RegistrationView(CreateView):
    form_class = RegisterForm
    template_name = 'log.html'
    extra_context = {"text":"Register"}
    success_url = reverse_lazy('log')

@login_required
def profile(request):
    data = request.user.fav.all()
    return render(request=request, template_name="profile.html",context={'data':data})
            

def search(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        coins = Coin.objects.filter(name__icontains=request.POST['coin'])
        if len(coins)>0 and len(request.POST['coin']):
            data = []
            for i in coins:
                item = {
                    'id':i.pk,
                    'img':i.img,
                    'name':i.name,
                    'sym':i.symb
                }
                data.append(item)
        else:
            data="No coins found ..."
        return JsonResponse({"data":data},status=200)
    return JsonResponse({},status=200)