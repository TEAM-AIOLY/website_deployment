from django.urls import path
from django_distill import distill_path
from django_web_aioly import views
from django.shortcuts import render
from django.utils import translation
import gettext
import os


BASE_DIR = os.path.dirname(__file__)
LOCALE_DIR = os.path.join(BASE_DIR, "locale")

# --- Wrappers des vues ---
def accueil_wrapper(request, lang):
    with translation.override(lang):
        print(f"[DEBUG] activate({lang}) → current: {translation.get_language()}")
        context = {'LANGUAGE_CODE': lang, 'active_page': 'home'}
        return render(request, 'pages/accueil.html', context)

def actualites_wrapper(request, lang):
    with translation.override(lang):
        print(f"[DEBUG] activate({lang}) → current: {translation.get_language()}")
        context = {'LANGUAGE_CODE': lang, 'active_page': 'actualites'}
        return render(request, 'pages/actualites.html', context)

def apprentissage_autosup_wrapper(request, lang):
    with translation.override(lang):
        print(f"[DEBUG] activate({lang}) → current: {translation.get_language()}")
        context = {'LANGUAGE_CODE': lang, 'active_page': 'apprentissage_autosup'}
        return render(request, 'pages/apprentissage_autosup.html', context)

def polarisation_mueller_wrapper(request, lang):
    with translation.override(lang):
        print(f"[DEBUG] activate({lang}) → current: {translation.get_language()}")
        context = {'LANGUAGE_CODE': lang, 'active_page': 'polarisation_mueller'}
        return render(request, 'pages/polarisation_mueller.html', context)

def chercheurs_wrapper(request, lang):
    with translation.override(lang):
        print(f"[DEBUG] activate({lang}) → current: {translation.get_language()}")
        context = {
            'LANGUAGE_CODE': lang,
            'active_page': 'chercheurs',
            'chercheurs': views.pages
        }
        return render(request, 'pages/chercheurs.html', context)

def chercheurs_page_wrapper(request, lang, chercheur_name):
    print(f"[DEBUG] Vue chercheurs_page_wrapper appelée avec {lang=} et {chercheur_name=}")
    TRANSLATABLE_FIELDS = ['Description', 'Domaine_de_recherche', 'Biographie']

    with translation.override(lang):
        raw_data = views.pages.get(chercheur_name, {})
        print("[DEBUG wrapper] raw_data Biographie:", raw_data.get("Biographie", "")[:80])

        # 🔹 Ajouter cette ligne pour définir _ localement
        translator = gettext.translation(
            domain='django',
            localedir=LOCALE_DIR,
            languages=[lang],
            fallback=True
        )
        _ = translator.gettext

        translated_data = {}
        for key, value in raw_data.items():
            if key in TRANSLATABLE_FIELDS and isinstance(value, str):
                translated_data[key] = _(value)
            else:
                translated_data[key] = value
        print("[DEBUG wrapper] Biographie après traduction:", translated_data.get("Biographie", "")[:80])

        context = {
            'LANGUAGE_CODE': lang,
            'active_page': 'chercheurs',
            **translated_data
        }

        return render(request, 'pages/chercheurs_page.html', context)

def partenaires_wrapper(request, lang):
    with translation.override(lang):
        print(f"[DEBUG] activate({lang}) → current: {translation.get_language()}")
        context = {'LANGUAGE_CODE': lang, 'active_page': 'partenaires'}
        return render(request, 'pages/partenaires.html', context)

def contact_wrapper(request, lang):
    with translation.override(lang):
        print(f"[DEBUG] activate({lang}) → current: {translation.get_language()}")
        context = {'LANGUAGE_CODE': lang, 'active_page': 'contact'}
        return render(request, 'pages/contact.html', context)

# --- Fonctions pour Distill ---
LANGUAGES = ['fr', 'en']

def get_langs():
    return [{'lang': lang} for lang in LANGUAGES]

def get_chercheurs():
    params = []
    for lang in LANGUAGES:
        for chercheur_name in views.pages.keys():
            params.append({'lang': lang, 'chercheur_name': chercheur_name})
    return params

# --- URL patterns ---
urlpatterns = [
    distill_path('<str:lang>/', accueil_wrapper, name='home', distill_func=get_langs),
    distill_path('<str:lang>/actualites/', actualites_wrapper, name='actualites', distill_func=get_langs),
    distill_path('<str:lang>/apprentissage_autosup/', apprentissage_autosup_wrapper, name='apprentissage_autosup', distill_func=get_langs),
    distill_path('<str:lang>/polarisation_mueller/', polarisation_mueller_wrapper, name='polarisation_mueller', distill_func=get_langs),
    distill_path('<str:lang>/chercheurs/', chercheurs_wrapper, name='chercheurs', distill_func=get_langs),
    distill_path('<str:lang>/chercheurs/<str:chercheur_name>/', chercheurs_page_wrapper, name='chercheur_page', distill_func=get_chercheurs),
    distill_path('<str:lang>/partenaires/', partenaires_wrapper, name='partenaires', distill_func=get_langs),
    distill_path('<str:lang>/contact/', contact_wrapper, name='contact', distill_func=get_langs),
]
