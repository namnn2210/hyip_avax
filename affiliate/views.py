from django.shortcuts import render


# Create your views here.
def overview(request):
    return render(request, template_name='admin/affiliate/overview.html')


def members(request):
    return render(request, template_name='admin/affiliate/members.html')
