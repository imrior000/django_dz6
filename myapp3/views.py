import datetime
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from myapp3.models import Order, Product
from myapp3.forms import ImageForm, ProductForm

def dates(q):
    date_t = str(datetime.datetime.today()).split()[0]
    yy, mm, dd = date_t.split('-')
    yy = int(yy)
    mm = int(mm)
    dd = int(dd)
    return [datetime.date(yy, mm, dd) - datetime.timedelta(days=q), datetime.date(yy, mm, dd)]

def index(request):
    res =  Order.objects.all()
    http={'qwerty': res}
    return render(request, 'myapp3/my_template.html', http)

def day(request):
    res =  Order.objects.filter(date_ordered__range=(dates(7)))
    http={'qwerty': res}
    return render(request, 'myapp3/my_template.html', http)

def month(request):
    res =  Order.objects.filter(date_ordered__range=(dates(30)))
    http={'qwerty': res}
    return render(request, 'myapp3/my_template.html', http)

def year(request):
    res =  Order.objects.filter(date_ordered__range=(dates(365)))
    http={'qwerty': res}
    return render(request, 'myapp3/my_template.html', http)

def upload_image(request, product_id):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            res =  Product.objects.filter(pk=product_id).first()
            res.image = image.name
            res.save()
    else:
        form = ImageForm()
    return render(request, 'myapp3/upload_image.html', {'form': form})

def upload_image_s1(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            col = form.cleaned_data['col']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            res =  Product(name=name, description=description, price=price, col=col, image=image)
            res.save()
    else:
        form = ProductForm()
    res =  Product.objects.all()
    http={'qwerty': res, 'form': form}
    return render(request, 'myapp3/my_template1.html', http)