import os
from django.shortcuts import render
from .vari import calcVegIndex
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.colors
import skimage
import numpy as np 
matplotlib.style.use('ggplot')
np.random.seed(1)
#from .vari import calcVegIndex
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(request):
    return render(request , 'index.html')

def upload(request):
    if request.method=='POST':
        myfile = request.FILES['img']
        algorithm=request.POST['algorithm']
        extension = myfile.name.split('.')[1]
        photo_path = 'static/img/' 
        if os.path.exists(photo_path + 'test.png'):
            os.remove(photo_path+'test.png')
        elif os.path.exists(photo_path + 'test.jpg'):
            os.remove(photo_path+'test.jpg')
        elif os.path.exists(photo_path + 'test.jpeg'):
            os.remove(photo_path+'test.jpeg')
        fs = FileSystemStorage()
        fs.save(photo_path+'test.'+ extension, myfile)
        if algorithm=='rndvi':       
            myfilenir = request.FILES['nir']
            if os.path.exists(photo_path + 'nir.png'):
                os.remove(photo_path + 'nir.png')
            elif os.path.exists(photo_path + 'nir.jpg'):
                os.remove(photo_path + 'nir.jpg')
            elif os.path.exists(photo_path + 'nir.jpeg'):
                os.remove(photo_path + 'nir.jpeg')
            fs1 = FileSystemStorage()
            fs1.save(photo_path + 'nir.' + extension, myfilenir)
        if algorithm=='fndvi':
            dense,sparse,barren=calcVegIndex(photo_path+'test.'+extension,0,extension,photo_path,1)
        else:
            dense,sparse,barren=calcVegIndex(photo_path+'test.'+extension,photo_path+'nir.'+extension,extension,photo_path,2)
      
        inputimg='img/test.'+extension
        outputimg='img/result.'+extension
        #plotimg='img/plot.png'
        return render(request , 'output.html',{'outputimg':outputimg,'inputimg':inputimg,'dense':dense,'sparse':sparse,'barren':barren})