from django.shortcuts import render


# Create your views here.
def news_list(request):
    return render(request, template_name='admin/news/list.html')


def news_detail(request):
    return render(request, template_name='admin/news/detail.html')
