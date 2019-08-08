import os
from django.shortcuts import render
from .vari import vari
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    return render(request , 'index.html')

def upload(request):
    if request.method == 'POST' and request.FILES['img']:
        myfile = request.FILES['img']
        extension = myfile.name.split('.')[1]
        photo_path = 'static/img/' 
        if os.path.exists(photo_path + 'test.png'):
            os.remove(photo_path+'test.png')
        elif os.path.exists(photo_path + 'test.jpg'):
            os.remove(photo_path+'test.jpg')
        elif os.path.exists(photo_path + 'test.jpeg'):
            os.remove(photo_path+'test.jpeg')
        fs = FileSystemStorage()
        filename = fs.save(photo_path+'test.'+ extension, myfile)
    #main code
    vari(photo_path+'test.'+extension,extension,photo_path)
    inputimg='img/test.'+extension
    outputimg='img/result.'+extension
    return render(request , 'output.html',{'outputimg':outputimg,'inputimg':inputimg})