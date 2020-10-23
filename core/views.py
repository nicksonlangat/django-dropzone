from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from .models import Image
# Create your views here.

class Index(TemplateView):
    template_name='index.html'

def file_upload(request):
    # print(request.FILES)
    if request.method == 'POST':
        my_file=request.FILES.get('file')
        Image.objects.create(image=my_file)
        return HttpResponse('')
    return JsonResponse({'post':'fasle'})

