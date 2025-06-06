from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, "pages/index.html")

def brand_detail(request):
    pass


def restore_product(request):
    pass