from django.urls import path
from resume import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]

app_name = "resume"

urlpatterns = [
    path('', views.show_resume, name="index"),
]