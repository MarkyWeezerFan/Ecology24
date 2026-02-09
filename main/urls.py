from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('achievements', views.achievement, name='achievements'),
    path('public', views.public, name='publications'),
    path('project', views.project, name='projects'),
    path('project/<int:ID>/', views.projects_details, name='projects-detail'),
    path('people', views.people, name='people'),
    path('people/<int:ID>/', views.people_details, name='people-detail'),
    path('news', views.news, name='news'),
    path('news/<int:ID>/', views.news_details, name='news-detail'),
    path('media', views.media, name='media'),
    path('login', views.login, name='login'),
    path('analytics', views.analytics, name='analytics'),
    path('contacts', views.contacts, name='contacts'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)