from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse
from projects.models import Project

# Create your views here.
def yadda(request):
    return render(request, 'projects/yadda.html')

def send_bad_request(request):
    return HttpResponseBadRequest()

def introduce_the_douyoncovers(request):
    return HttpResponse('<h1>We are the DCs!</h1>')

def show_all_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html',
                  {'projects': projects})

def show_project_details(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/project_details.html',
                  {'project': project})