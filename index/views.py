from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request=request, template_name='admin/index.html')


def account(request):
    return render(request=request, template_name='admin/account.html')


def recharge(request):
    return render(request=request, template_name='admin/recharge.html')
