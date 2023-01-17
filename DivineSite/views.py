from django.shortcuts import render
from .forms import ImageForm

# Create your views here.
def soon(request):
    return render(request, 'soon.html')

def image_upload_view(request):
    if(request.method == 'POST'):
        form = ImageForm(request.POST, request.FILES)
        if(form.is_valid):
            form.save()
            img_obj = form.instance
            return render(request,'imageUpload.html',{'form':form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'imageUpload.html', {'form':form})