from django.shortcuts import get_object_or_404, render, redirect
from .models import Hairclip, Ordershop, Positions
from django.views.generic import ListView
from django.core.paginator import Paginator
from .forms import OrdershopForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.core.mail import EmailMessage



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
    name = request.GET.get('view')
    print(name)

    if not cart.get(product):
        cart[product] = {"quantity": 1}

    return redirect(name)


def in_cart(request):

    cart_list = request.session.get('cart', {})
    in_cart_list = Hairclip.objects.filter(pk__in=cart_list)

    total = 0
    for each in in_cart_list:
        each.quantity = cart_list[str(each.id)]["quantity"]
        total += cart_list[str(each.id)]["quantity"] * each.price

    form = OrdershopForm()

    paginator = Paginator(in_cart_list, 3)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {"page_obj": page_obj, "total": total, "form": form}
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


def order(request):
    user = authenticate(username=request.POST['email'], password="k")
    # user_email = str(request.POST['email'])
    # print(user_email)
    if user is None:
        user = User.objects.create_user(username=request.POST['email'], password="k")
    cart_list = request.session.get('cart', {})
    order_list = Hairclip.objects.filter(pk__in=cart_list)
    total = 0
    number = 0
    form = OrdershopForm(request.POST)
    pk = form.save().id
    order = Ordershop.objects.get(pk=pk)

    for each in order_list:
        order.positions_set.create(img=each.img, title=each.title,
        price=each.price, quantity=cart_list[str(each.id)]["quantity"])
        total += cart_list[str(each.id)]["quantity"] * each.price
        number += cart_list[str(each.id)]["quantity"]

    #email = str(order_list)
    #
    # send_mail('Заказ', str(order_list), 'katrin.balakina@gmail.com',
    #           ['katrin.balakina@gmail.com'])
    #
    # email = EmailMessage('Hello', 'World', to=['katrin.balakina@gmail.com'])
    # email.send()

    del request.session['cart']

    request.session['order'] = user.id, total, number

    order_lists = Positions.objects.filter(ordershop_id=pk)
    content = {"order_lists": order_lists, "total": total, "number": number}
    return render(request, 'clip/order.html', content)



def emty_order(request):

    # Ordershop.objects.all().delete()
    # Positions.objects.all().delete()



    user_id = request.session.get('order', 'red')
    print(user_id)
    if user_id != 'red':
        user = get_object_or_404(User, pk=user_id[0])
        total = user_id[1]
        number = user_id[2]
        order = Ordershop.objects.filter(email=user.username).last()
        order_lists = order.positions_set.all()
        order_lists = Positions.objects.filter(pk__in=order_lists)
        content = {"order_lists": order_lists, "total": total, "number": number}
        return render(request, 'clip/order.html', content)
    return render(request, 'clip/order.html')

# def example(request, user_id):
#     print(user_id)
#     return render(request, 'clip/order.html')
