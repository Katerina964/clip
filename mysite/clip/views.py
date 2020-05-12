from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Hairclip
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.db.models import F
from PIL import Image


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
    product = request.GET.get('product')
    # если такого продукта нет в корзине, то мы его добавляем с количеством 1 по умолчанию
    if not cart.get(product):
        cart[product] = {'quantity': 1}
    return redirect("clip:all")


def in_cart(request):

    # cart_list = request.session.get('cart_list', [])

    # in_cart_list = Hairclip.objects.filter(pk__in=cart_list)
    # total = in_cart_list.count()

    # if request.GET.get("plus"):
    #     pk = request.GET.get("plus")
    #     in_cart_list.filter(pk=pk).update(quantity=F('quantity') + 1)
    #
    # elif request.GET.get("minus"):
    #     pk = request.GET.get("minus")
    #     in_cart_list.filter(pk=pk).update(quantity=F('quantity') - 1)

    # paginator = Paginator(in_cart_list, 3)
    # page = request.GET.get('page')
    # page_obj = paginator.get_page(page)

    # context = {'page_obj': page_obj, "total": total}

    cart = request.session.get('cart', {})

    cart_products = Hairclip.objects.filter(pk__in=cart.keys())

    cart_description = []
    for cart_product in cart_products:
        cart_description.append(
            {
                "pk": cart_product.pk,
                "title": cart_product.title,
                "img": {
                    "url": cart_product.img.url,
                    "name": cart_product.img.name
                },
                "characteristic": cart_product.characteristic,
                "quantity": cart[str(cart_product.pk)]['quantity']
            }
        )

    paginator = Paginator(cart_description, 3)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {"page_obj": page_obj, "total": len(cart_description)}

    # return redirect("clip:in_cart")
    return render(request, 'clip/cart_list.html', context)


def manage_cart(request):
    print(request.GET)
    plus = request.GET.get("plus")
    minus = request.GET.get("minus")
    pk = plus or minus
    if pk is not None:
        print("PK IS", pk)
        request.session['cart'] = request.session.get('cart', {})
        cart = request.session['cart']
        product = cart.get(str(pk), {'quantity': 0})
        print("PRODUCT IS", product)

        if plus:
            product['quantity'] += 1
        elif minus:
            product['quantity'] -= 1

        print("PRODUCT AFTER OPERATION", product)
        if product['quantity'] > 0:
            print("ENSURING PRODUCT EXISTS")
            cart[str(pk)] = product
        elif cart.get(str(pk)):
                print("ENSURING PRODUCT DELETED")
                del cart[str(pk)]
    return redirect("clip:in_cart")



