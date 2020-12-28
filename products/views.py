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
#authentication
#https://www.youtube.com/watch?v=qwE9TFNub84

def liste(request):
    products = Product.objects.all()
    return render(request, 'liste.html', { 'products': products })


def add_product(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MyProductForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            product = form.save(commit=False)
            product.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/products/thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MyProductForm()

    return render(request, 'myproductform.html', {'form': form})

def edit_product(request,pk):
    #https://www.youtube.com/watch?v=EX6Tt-ZW0so&t=264s
    product = Product.objects.get(id=pk)
    form = MyProductForm(instance=product)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MyProductForm(request.POST,request.FILES,instance=product)
        # check whether it's valid:
        if form.is_valid():
            # TODO process the data in form.cleaned_data as required
            print('form is valid')
            product = form.save(commit=False)
            product.save()
            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."
            # name = form.cleaned_data['name']
            # save https://www.youtube.com/watch?v=dBctY3-Z5hY
            # redirect to a new URL:
            return HttpResponseRedirect('/products/thanks')
    return render(request, 'editform.html', {'form': form})

def thanks(request):
    return HttpResponse('Merci')