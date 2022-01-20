from django.urls import path
from . import views

urlpatterns = [
    path('states/<str:pk_test>/',views.category,name='category'),
    path('states/<str:pk_test>/<str:pk_data>/',views.subcategory),
    path('states/<str:pk_test>/<str:pk_data>/<str:pk_value>/',views.Jobs),
    path('states/',views.states,name='Home-Page'),
    path('register/',views.register),
    path('',views.register),
    path('search_states/',views.search_states,name='search_states'),
    path('search_category/',views.search_category,name='search_category'),
    path('search_sub_category/',views.search_sub_category,name='search_sub_category'),
    path('search_jobs/',views.search_jobs,name='search_jobs'),
]