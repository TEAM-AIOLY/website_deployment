from django.contrib import admin
from django.urls import path
from django_distill import distill_path
from . import views

'''urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accueil, name='home'),
    path('acceuil/', views.accueil, name='home'),
    path('actualites/', views.actualites, name='actualites'),
    path('actualites/apprentissage_autosup/', views.apprentissage_autosup, name='apprentissage_autosup'),
    path('actualites/polarisation_mueller/', views.polarisation_mueller, name='polarisation_mueller'),
    path('chercheurs/', views.chercheurs, name='chercheurs'),
    path('chercheurs/<str:chercheur_name>/', views.chercheurs_page, name='chercheurs_page'),
    path('partenaires/', views.partenaires, name='partenaires'),
    path('contacts/', views.contact, name='contact'),

]'''
def get_none():
    return None

# Pour les pages "chercheurs"
def get_chercheurs():
    for key in views.pages.keys():
        yield {'chercheur_name': key}

urlpatterns = [
    distill_path('', views.accueil, name='home', distill_func=get_none, distill_file='index.html'),
    distill_path('acceuil/', views.accueil, name='acceuil', distill_func=get_none, distill_file='acceuil/index.html'),
    distill_path('actualites/', views.actualites, name='actualites', distill_func=get_none, distill_file='actualites/index.html'),
    distill_path('actualites/apprentissage_autosup/', views.apprentissage_autosup, name='apprentissage_autosup', distill_func=get_none, distill_file='actualites/apprentissage_autosup/index.html'),
    distill_path('actualites/polarisation_mueller/', views.polarisation_mueller, name='polarisation_mueller', distill_func=get_none, distill_file='actualites/polarisation_mueller/index.html'),
    distill_path('chercheurs/', views.chercheurs, name='chercheurs', distill_func=get_none, distill_file='chercheurs/index.html'),
    distill_path('chercheurs/<str:chercheur_name>/', views.chercheurs_page, name='chercheurs_page', distill_func=get_chercheurs),
    distill_path('partenaires/', views.partenaires, name='partenaires', distill_func=get_none, distill_file='partenaires/index.html'),
    distill_path('contact/', views.contact, name='contact', distill_func=get_none, distill_file='contact/index.html'),
]