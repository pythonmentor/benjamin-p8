from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product, Favorite


def result_search(request):
    """Django view search result page."""

    result = None
    try:
        product_search = request.GET['q']
        product = Product.objects.filter(
            product_name_fr__icontains=product_search).first()
        if product:
            substituts = product.better_products()
        else:
            product = None
            substituts = None

    except KeyError:
        print('Pas de requête')

    return render(request, 'products/result_search.html', {'substituts': substituts, 'product': product})


def product_sheet(request, code):
    """Django view product page."""

    product = get_object_or_404(Product, id=code)
    return render(request, 'products/product_sheet.html', {'product': product})


def favorites(request):
    """Django view favorite recording page."""

    if request.method == 'POST':
        user = request.user
        id_product = request.POST['id_product']
        product = Product.objects.get(id=id_product)
        product_save = Favorite.objects.get_or_create(
            user=user,
            id_result=product
            )
        return render(request, 'products/product_sheet.html', {'product': product})

    return redirect('home')
