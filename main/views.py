from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
import os
from .forms import FileUpload
import datetime

class HomePage(View):
    def get(self,request,*args,**kwargs):
        return render(request,'main/Home.html')


    def post(self,request,*args,**kwargs):
        files = request.FILES.getlist('files')
        if len(files) > 0:
            path = os.path.join(os.environ["HOMEPATH"], "Desktop", 'transfer')
            if not os.path.exists(path): os.mkdir(path)
            path = os.path.join(path, str(datetime.datetime.now()).replace(':', '-'))
            os.mkdir(path)
            for file in files:
                with open(os.path.join(path,file.name),'wb+') as f:
                    f.write(file.read())
        else:
            return render(request, 'main/Home.html')


        return HttpResponse('Sucess')