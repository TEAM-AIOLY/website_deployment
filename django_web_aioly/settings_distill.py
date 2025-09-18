from .settings import *

# Pour Django Distill et GitHub Pages : chemins relatifs
STATIC_URL = '/website_deployment/static/'
MEDIA_URL = './media/'

# Si tu veux, tu peux aussi désactiver le debug pour le build
DEBUG = False
DISTILL_STATIC = True