from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', '')
    if sort == 'name':
        phones = Phone.objects.order_by("name")
        context = {'phones': phones}
    elif sort == 'min_price':
        phones = Phone.objects.order_by("price")
        context = {'phones': phones}
    elif sort == 'max_price':
        phones = Phone.objects.order_by("-price")
        context = {'phones': phones}
    else:
        phones = Phone.objects.all()
        context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.get(slug=slug)
    context = {'phones': phones}
    return render(request, template, context)
