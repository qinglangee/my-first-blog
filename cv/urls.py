from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_view, name='cv_view'),
    path('workexp/<int:pk>/', views.work_exp_detail, name='work_exp_detail'),
    path('workexp/new/', views.work_exp_new, name='work_exp_new'),
    path('workexp/<int:pk>/edit/', views.work_exp_edit, name='work_exp_edit'),

]