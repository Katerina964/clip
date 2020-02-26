from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from .models import Hairclip
from django.views.generic import ListView
from PIL import Image


def category_crab(request):
    crab_list = Hairclip.objects.filter(category='краб')
    context = {'crab_list': crab_list}

    return render(request, 'clip/category_crab.html', context)



class HomePageView(ListView):
    model = Hairclip
    template_name = 'clip/all.html'
    paginate_by = 4

def detail(request, pk):
    hairclip = get_object_or_404(Hairclip, pk=pk)
    if hairclip:
        pass

    return render(request, 'clip/detail.html', {'hairclip': hairclip})


def category_spring(request):
    spring_list = Hairclip.objects.filter(category='пружинки')
    context = {'spring_list': spring_list}
    paginate_by = 2

    return render(request, 'clip/spring_list.html', context)






