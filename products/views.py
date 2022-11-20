from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from products.models import Category, Product, OrderProduct, Order
import datetime


def professions_page(request):
    if request.user.is_authenticated:
        return render(request, 'profession.html', {
        })
    else:
        response = redirect('/accounts/login/')
        return response


def cashier_view(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.profession == 'cashier':
            all_category = Category.objects.all()
            objects = []
            for category in all_category:
                category_products = Product.objects.filter(category=category)
                objects.append({'category': category, 'products': category_products})

            return render(request, 'profession-cashier.html', {
                'objects': objects,
            })
        else:
            return redirect('/page/not_found/')
    else:
        response = redirect('/accounts/login/')
        return response

@login_required
def add_to_card(request, id):
    product = get_object_or_404(Product, id=id)
    order_product, created = OrderProduct.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False,
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__id=product.id).exists():
            order_product.quantity += 1
            order_product.save()
            messages.info(request, "Bu mahsulot miqdori yangilandi!")
            return redirect("/profession/cashier")
        else:
            order.products.add(order_product)
            messages.info(request, "Mahsulot qo'shildi!")
            return redirect('/profession/cashier')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user,
            ordered_date=ordered_date
        )
        order.products.add(order_product)
        messages.info(request, "Mahsulot qo'shildi!")
        return redirect('/profession/cashier')

@login_required
def remove_from_card(request, id):
    product = get_object_or_404(Product, id=id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False,
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(product__id=product.id).exists():
            order_product = OrderProduct.objects.filter(
                product=product,
                user=request.user,
                ordered=False,
            )[0]
            order.products.remove(order_product)
            messages.info(request, "Bu mahsulot olib tashlandi!")
            return redirect('/profession/cashier')
        else:
            messages.info(request, "This item was not in your cart")
            return redirect('/profession/cashier')
    else:
        messages.info(request, "You do not have an active order")
        return redirect('/profession/cashier')


def chef_view(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.profession == 'chef':
            # all_baskets = Basket.objects.all()
            # baskets_list = []
            # for basket in all_baskets:
            #     products = Product.objects.filter(basket=basket)
            #     baskets_list.append({'basket': basket, 'products': products})
            #
            # baskets_list.reverse()
            return render(request, 'profession-chef.html', {
                # 'baskets': baskets_list,
            })
        else:
            return redirect('/page/not_found/')
    else:
        return redirect('/accounts/login/')


def accountant_view(request):
    if request.user.is_superuser or request.user.profession == 'accountant':
        today = datetime.date.today()
        # today_baskets = Basket.objects.filter(add_date__gte=today)
        # baskets_list = []
        # umumiy_summa = 0
        # for basket in today_baskets:
        #     products = Product.objects.filter(basket=basket)
        #     summa = 0
        #     for product in products:
        #         if product.discount_price:
        #             summa += product.discount_price
        #         else:
        #             summa += product.price
        #     baskets_list.append({'basket': basket, 'products': products, 'price': summa})
        #     umumiy_summa += summa
        return render(request, 'admin_page/home.html', {
            # 'today_baskets': baskets_list,
            # 'umumiy_summa': umumiy_summa,
        })
    else:
        return redirect('/page/not_found/')

def accountant_view1(request):
    if request.user.is_superuser or request.user.profession == 'accountant':
        week = datetime.date.today() - datetime.timedelta(days=7)
        # this_week_baskets = Basket.objects.filter(add_date__gte=week)
        # baskets_list = []
        # umumiy_summa = 0
        # for basket in this_week_baskets:
        #     products = Product.objects.filter(basket=basket)
        #     summa = 0
        #     for product in products:
        #         if product.discount_price:
        #             summa += product.discount_price
        #         else:
        #             summa += product.price
        #     baskets_list.append({'basket': basket, 'products': products, 'price': summa})
        #     umumiy_summa += summa
        return render(request, 'admin_page/home1.html', {
            # 'this_week_baskets': baskets_list,
            # 'umumiy_summa': umumiy_summa,
        })
    else:
        return redirect('/page/not_found/')


def accountant_view2(request):
    if request.user.is_superuser or request.user.profession == 'accountant':
        week = datetime.date.today() - datetime.timedelta(days=30)
        # this_week_baskets = Basket.objects.filter(add_date__gte=week)
        # baskets_list = []
        # umumiy_summa = 0
        # for basket in this_week_baskets:
        #     products = Product.objects.filter(basket=basket)
        #     summa = 0
        #     for product in products:
        #         if product.discount_price:
        #             summa += product.discount_price
        #         else:
        #             summa += product.price
        #     baskets_list.append({'basket': basket, 'products': products, 'price': summa})
        #     umumiy_summa += summa
        return render(request, 'admin_page/home2.html', {
            # 'this_week_baskets': baskets_list,
            # 'umumiy_summa': umumiy_summa,
        })
    else:
        return redirect('/page/not_found/')


def categories_view(request):
    if request.user.is_superuser or request.user.profession == 'accountant':
        all_categoies = Category.objects.all()

        return render(request, 'admin_page/categories.html', {
            'categories': all_categoies,
        })
    else:
        return redirect('/page/not_found/')

class CategoryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    template_name = 'admin_page/create_category.html'
    fields = ['name', ]

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser

class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    template_name = 'admin_page/update_category.html'
    fields = ['name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser


class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    template_name = 'admin_page/delete_category.html'
    success_url = reverse_lazy('categories')

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser


def products_view(request):
    if request.user.is_superuser or request.user.profession == 'accountant':
        products = Product.objects.all()

        return render(request, 'admin_page/products.html', {
            'products': products,
        })
    else:
        return redirect('/page/not_found/')

class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    template_name = 'admin_page/create_product.html'
    fields = ['name', 'price', 'discount_price', 'category',]

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'admin_page/update_product.html'
    fields = ['name', 'price', 'discount_price', 'category',]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'admin_page/delete_product.html'
    success_url = reverse_lazy('products')

    # user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser