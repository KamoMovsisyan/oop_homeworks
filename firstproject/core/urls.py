from django.urls import path
from core import views

urlpatterns = [
    path('hello/', views.hello),
    path('introduction/', views.intro),
    path('curr_time/', views.time_),
    path('solution/', views.solution),
    path('list_task/', views.list_task),
    path('home/', views.home)
]
