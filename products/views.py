from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import Product

from .forms import NameForm, ProductForm,MyProductForm

# authentication tutorial
# https://www.youtube.com/watch?v=dBctY3-Z5hY
#file upload tutorial
#https://www.youtube.com/watch?v=v5FWAxi5QqQ
#https://www.youtube.com/watch?v=KQJRwWpP8hs  BETTER?

#session
#https://www.youtube.com/watch?v=EW_vjGzXPCc

def index(request):
    products = Product.objects.all()
    print('***products')
    print(products)
    return render(request, 'index.html', { 'products': products })

#https://www.youtube.com/watch?v=qwE9TFNub84
def monform(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MyProductForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/products/thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MyProductForm()

    return render(request, 'myproductform.html', {'form': form})

"""def add(request):
    p = Product()
    p.name = "Test Nom"
    p.price = 20.0
    p.stock = 10
    p.image = 'http://'
    p.save()
    return HttpResponse('Nouveau produit inséré')"""



def thanks(request):
    return HttpResponse('Merci')


def add_product_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MyProductForm(request.POST, request.FILES)
        print('in the add 1a ******')
        print(request.POST)
        print('in the add 1b ******')
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print('in the add 2 ******')
            product = form.save(commit=False)
            print('*********',request.FILES)
            product.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/products/thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MyProductForm()

    return render(request, 'myproductform.html', {'form': form})

def edit_product(request,pk):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MyProductForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # TODO process the data in form.cleaned_data as required
            product = form.save()

            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."
            # name = form.cleaned_data['name']
            # save https://www.youtube.com/watch?v=dBctY3-Z5hY
            # redirect to a new URL:
            return HttpResponseRedirect('/products/thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        print('my_recordxxx ',pk)
        my_record = Product.objects.get(id=pk)
        print('start printing my_recordxxx',my_record.name)
        print('****')
        form = MyProductForm(instance=my_record)

    return render(request, 'editform.html', {'form': form})