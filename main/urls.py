from django.urls import path
from . import views
from .views import IndexTab

urlpatterns = [
    path('', views.index_start, name='start'),
    path('tabs/', IndexTab.as_view(), name='main'),
    # path('tabs/', views.index_tab, name='main'),
    path('universities/', views.index, name='home'),
    path('university/<int:id>/view', views.university_view, name='university_view'),
    path('university/<int:id>/edit', views.university_edit, name='university_edit'),
    path('university/<int:id>/delete', views.university_delete, name='university_delete'),
    path('about-us/', views.about, name='about'),
    path('create/', views.create, name='create'),


]