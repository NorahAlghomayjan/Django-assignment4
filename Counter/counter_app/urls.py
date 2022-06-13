from django.urls import path , include
from . import views

urlpatterns = [
    path('',views.index),
    path('destroy_session',views.destroy_session),
    path('increment2',views.increment2),
    path('userCount', views.userCount)
]