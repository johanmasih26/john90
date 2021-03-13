from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import ImageForm
from .models import photo


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = photo.objects.all()    
    return render(request,'index.html',{'form':form,'img':img})        