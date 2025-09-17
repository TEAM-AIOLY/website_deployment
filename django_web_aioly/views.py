from django.shortcuts import render

def accueil(request):
    return render(request, 'pages/accueil.html', {"active_page": "home"})

# Page Actualités
def actualites(request):
    return render(request, "pages/actualites.html", {"active_page": "actualites"})

def apprentissage_autosup(request):
    return render(request, "pages/apprentissage_autosup.html", {"active_page": "actualites"})
def polarisation_mueller(request):
    return render(request, "pages/polarisation_mueller.html", {"active_page": "actualites"})

pages = {
    'Ryad_BENDOULA': {
        'Prenom': 'Ryad',
        'Nom':"BENDOULA",
        'Etablissement':'INRAE',
        'Description' : 'Directeur Laboratoire COMIC',
        'Domaine_de_recherche': 'Optique, Chimiométrie',
        'Google_Scholar': 'https://scholar.google.fr/citations?user=29G4y-gAAAAJ&hl=fr',
        'Linkedin': '',
        'Biographie': "Après un doctorat consacré au développement de biocapteurs optiques pour le secteur biomédical, Ryad a passé 2 ans à l'Institut Femto-St pour le développement d'oscillateurs micro-ondes optoélectroniques. Depuis 2007, il est chercheur à l'INRAE (Institut national de recherche pour l'agriculture, l'alimentation et l'environnement). Ryad dirige le groupe \"Capteurs optiques pour milieux complexes\". Ses activités de recherche se concentrent sur la spectrométrie Vis-NIR appliquée à la conception de capteurs pour l’agriculture et l’environnement. Il développe des méthodes et dispositifs optiques spécifiques afin d'améliorer la qualité du signal et la précision des mesures spectrométriques. Il participe également à la conception de nouveaux dispositifs spectroscopiques.",
        'Publications': [],
        'Brevets': [],
        'Image_path' : 'Ryad_Bendoula.jpg'
    },
    'Daphne_HERAN': {
        'Prenom': 'Daphné',
        'Nom': "HERAN",
        'Etablissement':'INRAE',
        'Description': 'Chargée de recherche optique',
        'Domaine_de_recherche': 'Optique, Chimiométrie',
        'Google_Scholar': '',
        'Linkedin': '',
        'Biographie': "",
        'Publications': [],
        'Brevets': [],
        'Image_path': 'daphne_HERAN.jpg'
    },
    'Jean_Michel_ROGER': {
        'Prenom': 'Jean-Michel',
        'Nom': "ROGER",
        'Etablissement':'INRAE',
        'Description': 'Ingénieur du génie rural pour l\'environnement et l\'agriculture',
        'Domaine_de_recherche': 'Chimiométrie, Spectroscopie',
        'Google_Scholar': 'https://scholar.google.fr/citations?user=doxD0JMAAAAJ&hl=fr',
        'Linkedin': 'https://www.linkedin.com/in/jean-michel-roger-37297a13b/',
        'Biographie': "Jean-Michel ROGER a obtenu son diplôme d\'ingénieur du génie rural en 1990 et son doctorat en 1995. Depuis les années 90, il mène des recherches en spectrométrie proche infrarouge et en chimiométrie. Son souci constant est de produire des solutions simples et opérationnelles pour mettre en œuvre la NIRS pour l\'environnement et à l\'agriculture. Pour rendre les capteurs embarqués opérationnels, il a d\'abord étudié les problèmes de robustesse de l\'étalonnage. Il a ainsi promu les méthodes d\'orthogonalisation, qui sont maintenant utilisées dans des applications pratiques, comme le transfert d\'étalonnage ou la correction de l\'effet d\'humidité. Il a également étudié les techniques de sélection de variables, dédiées au cas spécifique de la NIRS, ce qui lui a permis de développer des capteurs NIR pour l\'agriculture. En 2016, il a reçu le prix Tomas Hirschfeld du Comité international de la spectroscopie NIR et le prix de la recherche appliquée de la FIECC. En 2018, il a créé le pôle de recherche en chimiométrie ChemHouse, qui promeut l\'éducation, la recherche et la coopération autour de la NIRS et de la chimiométrie (http://chemproject.org).",
        'Publications': [],
        'Brevets': [],
        'Image_path': 'Jeanmichel_ROGER.jpg'
    },
    'Florent_ABDELGHAFOUR': {
        'Prenom': 'Florent',
        'Nom': "ABDELGHAFOUR",
        'Etablissement':'INRAE',
        'Description': '',
        'Domaine_de_recherche': 'Chimiométrie, Inteligence Artificielle',
        'Google_Scholar': '',
        'Linkedin': '',
        'Biographie': "",
        'Publications': [],
        'Brevets': [],
        'Image_path': 'Florent_Abdelghafour.png'
    },
    'David_ESTEVE': {
        'Prenom': 'David',
        'Nom': "ESTEVE",
        'Etablissement': 'PST',
        'Description': 'Directeur R&D',
        'Domaine_de_recherche': 'Matériaux et optique',
        'Google_Scholar': '',
        'Linkedin': 'https://fr.linkedin.com/in/desteve',
        'Biographie': "Ingénieur Polytech Paris Sud, spécialisé en sciences et génie des matériaux, et docteur en optique appliquée aux couches minces (2010). Il a 15 ans d'expérience dans le milieu des semi-conducteurs, et a rejoint Pellenc ST en 2022. Il a amélioré l'efficacité énergétique des machines en proposant des nouvelles architectures pneumatiques. Il a également proposé un nouveau système de gestion des perturbations aérauliques permettant d'améliorer significativement l'efficacité de tri des films et papiers. Il conduit actuellement plusieurs développements autour de technologies clefs de détection pour l'entreprise, notamment des systèmes de spectroscopie proche et moyen infrarouge. Il défini, oriente et encadre les travaux de R&D de l'équipe composée de 11 ingénieurs, dont 1 docteur et 3 doctorants dans les domaines de l'intelligence artificielle, de la vision par ordinateur et des technologies de détection.",
        'Publications': [],
        'Brevets': ["FR3148921A1","EP4605146A1","US2014245955","US2014007814","US2015247234","US2015307984","FR3075854"],
        'Image_path': 'David_ESTEVE.png'
    },
    'Maxime_METZ': {
        'Prenom': 'Maxime',
        'Nom': "METZ",
        'Etablissement': 'PST',
        'Description': 'Ingénieur intelligence artificielle',
        'Domaine_de_recherche': 'Intelligence artificielle',
        'Google_Scholar': '',
        'Linkedin': 'https://www.linkedin.com/in/maxime-metz-0792a2160/',
        'Biographie': "Maxime Metz, ingénieur en R&D , titulaire d\'un doctorat de Montpellier SupAgro obtenu en 2021 avec une spécialisation en traitement des données spectrales, a développé plusieurs méthodes de traitement de données. Ses travaux se sont principalement concentrés sur des approches de traitement des données spectrales pour les données volumineuses, ainsi que sur des méthodes de traitement de données robustes. En 2022, il a rejoint Pellenc ST où il travaille sur le développement de nouveaux modèles d\'intelligence artificielle pour le tri des déchets.",
        'Publications': [],
        'Brevets': [],
        'Image_path': 'Maxime_metz.jpg'
    },
    'Nicolas_EMANUELY': {
        'Prenom': 'Nicolas',
        'Nom': "EMANUELY",
        'Etablissement': 'PST',
        'Description': 'Ingénieur optique et traitement d\'image',
        'Domaine_de_recherche': 'Optique, Intelligence artificielle',
        'Google_Scholar': '',
        'Linkedin': 'https://www.linkedin.com/in/nicolas-emanuely-6947b3129/',
        'Biographie': "Diplomé d'un double diplome Supoptique-ESPCI, Nicolas a démarré en tant qu'ingénieur d'application dans le domaine de l'imagerie médicale. Il poursuit sa carriere au sein de Pellenc ST en tant qu'ingénieur optique et traitement d'image.",
        'Publications': ["'Simplified Instrument Calibration for Wide‐Field Fluorescence Resonance Energy Transfer (FRET) Measured by the Sensitized Emission Method', Cytometry A, 2021"],
        'Brevets': [],
        'Image_path': 'Nicolas_emanuely.PNG'
    },
    'Gwenaele_LECORRE': {
        'Prenom': 'Gwenaële',
        'Nom': "LE CORRE",
        'Etablissement': 'PST',
        'Description': 'Ingénieure optique et chef de projet',
        'Domaine_de_recherche': 'Optique',
        'Google_Scholar': '',
        'Linkedin': 'https://fr.linkedin.com/in/gw%C3%A9na%C3%ABle-le-corre-b252318a',
        'Biographie': "",
        'Publications': [],
        'Brevets': [],
        'Image_path': 'gwen2.png'
    },
    'Ivy_TUMOINE': {
        'Prenom': 'Ivy',
        'Nom': "TUMOINE",
        'Etablissement': 'PST',
        'Description': 'Doctorant',
        'Domaine_de_recherche': 'Intelligence artificielle, Chimiométrie',
        'Google_Scholar': '',
        'Linkedin': 'https://www.linkedin.com/in/ivy-tumoine-820204228/',
        'Biographie': "",
        'Publications': [],
        'Brevets': [],
        'Image_path': 'Ivy_TUMOINE_carre.jpg'
    },
    'Vincent_ROLLAND': {
        'Prenom': 'Vincent',
        'Nom': "ROLLAND",
        'Etablissement': 'PST',
        'Description': 'Ingénieur developpement IA',
        'Domaine_de_recherche': 'Intelligence artificielle',
        'Google_Scholar': '',
        'Linkedin': 'https://fr.linkedin.com/in/vincent-rolland-6406b0193',
        'Biographie': "Diplômé en génie informatique de l\'UTC en 2023, il intègre Pellenc ST en tant qu\'ingénieur vision R&D, spécialisé dans les modèles de vision RGB. Il évolue ensuite vers un poste d\'ingénieur vision dédié au développement et à l\'industrialisation de l\'IA. Ses travaux portent principalement sur l\'intégration de modèles d\'IA sur les machines de tri et sur la création d\'outils facilitant leur entraînement et leur déploiement.",
        'Publications': [],
        'Brevets': [],
        'Image_path': 'Vincent_ROLLAND.png'
    },
    'Tom_MONTAURIOL': {
        'Prenom': 'Tom',
        'Nom': "MONTAURIOL",
        'Etablissement': 'PST',
        'Description': 'Ingénieur developpement IA',
        'Domaine_de_recherche': 'Intelligence artificielle',
        'Google_Scholar': '',
        'Linkedin': 'https://fr.linkedin.com/in/tom-montauriol',
        'Biographie': "",
        'Publications': [],
        'Brevets': [],
        'Image_path': 'Tom_MONTAURIOL.jpg'
    }
}

def chercheurs(request):
    context = {"chercheurs": pages,"active_page": "chercheurs"}
    return render(request, "pages/chercheurs.html", context)

def chercheurs_page(request,chercheur_name):
    if chercheur_name.endswith('.html'):
        chercheur_name = chercheur_name[:-5]

    context = pages.get(chercheur_name)
    context.update({"active_page": "chercheurs"})
    return render(request, "pages/chercheurs_page.html", context)


def partenaires(request):
    return render(request, "pages/partenaires.html", {"active_page": "partenaires"})

# Page Contact
def contact(request):
    return render(request, "pages/contact.html", {"active_page": "contact"})