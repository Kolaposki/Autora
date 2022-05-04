from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    services = Product.objects.filter(status=True)
    context = {"services": services, 'key': settings.RAVE_PUBLIC_KEY}

    return render(request, 'home.html', context)


def success(request):
    return render(request, 'success.html', {})


@login_required  # redirect when user is not logged in
def checkout(request):
    print("checkout process")
    if request.method == 'GET':
        user_Details = request.user
        context = {"user_Details": user_Details, 'key': settings.RAVE_PUBLIC_KEY}
        return render(request, 'see.html', context)


def service_detail(request, slug):
    print("service_detail", slug)
    service = get_object_or_404(Product, slug=slug)
    print("service", service)

    context = {
        "service": service
    }
    return render(request, 'service_detail.html', context)
