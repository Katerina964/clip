from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Hairclip
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.db.models import F
from django.db.models import Count
import copy
from django.http import QueryDict


def category_crab(request):
    crab_list = Hairclip.objects.filter(category='краб')
    paginator = Paginator(crab_list, 4)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj}

    return render(request, 'clip/category_crab.html', context)


class HomePageView(ListView):
    model = Hairclip
    template_name = 'clip/all.html'
    paginate_by = 4


def detail(request, pk):
    hairclip = get_object_or_404(Hairclip, pk=pk)

    return render(request, 'clip/detail.html', {'hairclip': hairclip})


def category_spring(request):
    spring_list = Hairclip.objects.filter(category='пружинки')
    paginator = Paginator(spring_list, 4)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj}

    return render(request, 'clip/spring_list.html', context)


def cart(request):

    request.session['cart'] = request.session.get('cart', {})
    cart = request.session['cart']
    cart.update()
    product = request.GET.get('product')
    if not cart.get(product):
        cart[product] = {"quantity": 1}


    return redirect("clip:all")


def in_cart(request):

    cart_list = request.session.get('cart', {})
    in_cart_list = Hairclip.objects.filter(pk__in=cart_list)
    #form = HairclipForm()
    total = 0
    for each in in_cart_list:
        each.quantity = cart_list[str(each.id)]["quantity"]
        total += cart_list[str(each.id)]["quantity"] * each.price

    paginator = Paginator(in_cart_list, 3)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {"page_obj": page_obj, "total": total}
    return render(request, 'clip/cart_list.html', context)


def manage_cart(request):

    if request.GET.get("plus"):
        pk = request.GET.get("plus")
        request.session["cart"][str(pk)]["quantity"] += 1
        request.session.modified = True

    if request.GET.get("minus"):
        pk = request.GET.get("minus")
        if request.session["cart"][str(pk)]["quantity"] > 1:
            request.session["cart"][str(pk)]["quantity"] -= 1
            request.session.modified = True
        else:
            del request.session["cart"][str(pk)]
            request.session.modified = True

    return redirect("clip:in_cart")





