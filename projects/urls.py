from django.urls import include, path
from projects import views

app_name = "projects"

urlpatterns = [
    path('', views.show_all_projects, name="all_projects"),
    path('<int:pk>', views.show_project_details, name="project_details"),
    path('yadda', views.yadda),
    path('dc', views.introduce_the_douyoncovers),
]