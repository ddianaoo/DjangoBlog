from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def test(request):
    return render(request, "testapp/test.html", {'rubrics': Rubric.objects.all()})


def get_rubric(request, pk):
    rubric = Rubric.objects.get(pk=pk)
    return HttpResponse(f'<p>Hello, this page about {rubric}<p>')