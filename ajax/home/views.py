from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Datas
def index(request):
    return render(request,'index.html')
@csrf_exempt
def citystate(request):
    state=request.POST['state']
    data=Datas.objects.filter(state=state).all()
    #data=Datas.objects.all()
    return render(request,'show.html',{'data':data})
