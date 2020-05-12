'''def add_to_cart(request):
    request.session['cart'] = request.session.get('cart', [])
    product = request.GET.get('product')
    shopping_cart = request.session['cart']
    if product is not None and product not in shopping_cart:
        shopping_cart.append(product)
    print('Product to add', product)
    print('Shopping cart', shopping_cart)
    return redirect("clip:all")'''