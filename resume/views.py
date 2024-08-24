from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse

# Create your views here.
def show_resume(request):
    return render(request, 'resume/index.html')