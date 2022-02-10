from commerce.form import CreateUserForm
from django.contrib.auth.forms import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .form import ReviewsForm
from .models import Category, Product, Subcategory, ProductImage, ProductDiscription, AditionalInform, Reviews
from django.http import HttpResponseRedirect

# from .forms import Reviews
# Create your views here.
# def index(request):
#     return render(request, 'commerce/index.html')
User = get_user_model()


def index1(request):
    mobile_products = Product.objects.filter(category__name="Mobile")[:6]
    products = Product.objects.filter(trend=True)[:6]
    tablet_products = Product.objects.filter(category__name="Tablet")
    mobile_subcategory = Subcategory.objects.filter(category__name="Mobile")[:6]
    laptop_subcategory = Subcategory.objects.filter(category__name="Laptop")
    tablet_subcategory = Subcategory.objects.filter(category__name="Tablet")
    is_slider = Product.objects.filter(is_slider=True)
    is_promotion = Product.objects.filter(is_slider=True)[:4]
    category = Category.objects.all()
    categories = Subcategory.objects.all()
    item_id = request.GET.get('item')
    # if item_id:
    #     categories = Product.get_all_brand_by_id(item_id)
    # else:
    #     categories= Product.get_all_brand()
    context = {
        'mobile_products': mobile_products,
        'msubcategory': mobile_subcategory,
        'lsubcategory': laptop_subcategory,
        'tsubcategory': tablet_subcategory,
        'products': products,
        'tablet_products': tablet_products,
        'categories': categories,
        'item_id': item_id,
        'category': category,
        'is_slider': is_slider,
        'is_promotion': is_promotion,
    }
    return render(request, 'commerce/index.html', context)


def index(request, id):
    product = Product.objects.filter(subcategory=id)[:5]
    products = Product.objects.filter(category=id)
    context = {
        'mobile_products': product,
        'products': products,
    }
    return render(request, 'commerce/filter.html', context)


def product_detail(request, id):
    hanif = 'hanif'
    product = Product.objects.filter(trend=True)[:6]
    product_det = Product.objects.get(id=id)
    pro_images = ProductImage.objects.filter(id=id)
    review_data = Reviews.objects.filter(product_id=id).order_by('-created_at')
    pro_det_description = ProductDiscription.objects.get(product_id=id)
    prod_aditional_infrm = AditionalInform.objects.get(product_id=id)
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            if request.user.is_authenticated:
                form.user = request.user
                form.product = product_det
                form.save()
            else:
                return redirect("login")
    form = ReviewsForm()
    context = {'product_det': product_det, "pro_images": pro_images, 'prod_aditionanl_infrm': prod_aditional_infrm,
               'pro_det_description': pro_det_description, 'product': product, 'review_data': review_data, 'form': form,
               'hanif': hanif}
    return render(request, 'commerce/product_detail.html', context)


def product(request):
    # product: Product.objects.all()[:6]
    keyword = request.GET.get('keyword')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    if keyword is not None:
        product = Product.objects.filter(name__icontains=keyword, price__range=[price_min, price_max])
        category = Category.objects.all()
    context = {
        'product': product,
        'category': category,
    }
    return render(request, 'commerce/product.html', context)


def signuppage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account is just created for ' + user)
                return redirect('index')

        context = {'form': form}

        return render(request, 'movieview/index.html', context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'User name Or password is incorrect')

        return render(request, 'header.html')


def logoutuser(request):
    logout(request)
    return redirect('login')

# def name_add(request):
#     hanif = 'hanif'
#     return render(request, 'header.hatml', {'hanif': hanif})
#
# @login_required
#     product = Product.objects.get(pk=pk)
#     # form = ReviewsForm
#     if request.method == 'POST':
#         form = ReviewsForm(request.POST)
#         if form.is_valid():
#             form = form(commit=False)
#             form.user = request.user
#             form.product = product
#             form.save()
#     form = ReviewsForm()
#     # data = User.objects.all()
#     return render(request, 'commerce/product_detail.html', {'form': form})

# if request.method == 'POST':
#     name = request.POST.get("name")
#     product = request.POST.get("prod_id")
#     product_instance = Product.objects.get(id=product)
#     title = request.POST.get("title")
#     comment = request.POST.get("review")
#     rate = request.POST.get("rate")
#     rev = Reviews(user=request.user, name=name, product=product_instance, title=title, comment=comment, rate=rate)
#     rev.save()
#     return redirect('product_detail', id=product)


def checkout_cart(request):
    return render(request, 'commerce/checkout_cart.html')
