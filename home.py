import streamlit as st
import base64


def home():
    
    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="Le portfolio d'Abdoulaye Tangara",
        page_icon="🍕",
    )

    # CSS styles file
    with open("styles/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Profile image file
    with open("assets/maphoto.jpeg", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

    # PDF CV file
    with open("assets/TANGARA_ABDOULAYE_CV.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    
    # Top title
    st.write(f"""<div class="title"><strong>Hello ! Je m'appelle </strong> Abdoulaye Tangara👋</div>""", unsafe_allow_html=True)

    # Profile image
    st.write(f"""
    <div class="container">
        <div class="box">
            <div class="spin-container">
                <div class="shape">
                    <div class="bd">
                        <img src="{img}" alt="Abdoulaye Tangara">
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, 
    unsafe_allow_html=True)

    # Alternative image (static and rounded) uncomment it if you prefer this one
    # st.write(f"""
    # <div style="display: flex; justify-content: center;">
    #    <img src="{img}" alt="Abdoulaye Tangara" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    # </div>
    # """, unsafe_allow_html=True)

    # Subtitle
    st.write(f"""<div class="subtitle" style="text-align: center;">Statisticien-économiste</div>""", unsafe_allow_html=True)

    # Social Icons
    social_icons_data = {
        # Platform: [URL, Icon]
        "LinkedIn": ["https://www.linkedin.com/in/abdoulaye-tangara-9219a2293/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/ABLO1234", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
        "Email": ["mailto:abdoulayetangara722@gmail.com", "https://static.vecteezy.com/system/resources/previews/016/716/465/original/gmail-icon-free-png.png"]
    }

    social_icons_html = [f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'><img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'></a>" for platform in social_icons_data]

    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)

    st.write("##")

    # About me section
    st.subheader("**À propos de moi**")
    st.write("""
    - 🧑‍💻 Je suis **Statisticien et Economiste option : Ingéniérie Financière** et actuellement Mastérant en **Economie Quantitative & Calculable** 

    - ❤️ Je suis très passioné par le **Machine Learning, Data,  Optimisation, Automatisation ainsi que leur application dans l'économie et dans la finance**, et plus!
                 
    - 🏂 J'aime jouer aux échecs, lire et surtout la musique 🧗
    
    - 📫 Comment me joindre ? : +22372228699 / Par mon adrresse Email ci-dessus
    
    - 🏠 Mali, Bamako
    """)
    st.write("--")
    
    st.subheader("**Mes compétences**")
    
    st.subheader("**Logiciel**")
    st.write("""
        - IBM SPSS
        - Power Query
        - pgAdmin4 (PostGreSql)
        - STATA
        - EVIEWS
        - CSPro
        - KOBOTOOLBOX
        - NestarPublisher
        - Jupyter NoteBook
        - VS code """)
        
    st.suheader(**Langage de programmation**)
    st.write("""
        - Python
        - SQL
        - STATA
        - EVIEWS
        - R
        - SPSS LANGUAGE
    """)

    
    st.write("**Mon CV 😊**")

    # Download CV button
    st.download_button(
        label="📄 Vous pouvez télécharger mon CV",
        data=pdf_bytes,
        file_name="TANGARA_ABDOULAYE_CV.pdf",
        mime="application/pdf",
    )

    st.write("##")
    
    st.write(f"""<div class="subtitle" style="text-align: center;">🚀 Vous pouvez voir mes projets, ci-dessous </div>""", unsafe_allow_html=True)


    tabs = st.tabs(["Machine Learning", "Tableau de bord", "Web Scraping"])


    with tabs[0]:
        st.subheader("1-    **Optimisation de portefeuille d'investissement (Projet en cours)**")
        st.write(""" 
                 **Description** : 
                 Il s'agit de l'application de techniques de machine learning à la finance.
                L'objectif du projet est de développer une application web destinée aux investisseurs, leur permettant, 
                à partir des caractéristiques de leur portefeuille, d'optimiser ce dernier en minimisant les risques tout en maximisant les gains. 
                
                 """)
        st.image("https://th.bing.com/th/id/R.29c69915712f9b4ab4ab41b1e1ad0ffa?rik=efeNiqWLFZAqYg&riu=http%3a%2f%2fwww.experts-comptables-fr.org%2fwp-content%2fuploads%2f2017%2f01%2finvestir.jpg&ehk=Axn7KZyNE%2fdSHpHUsLHWyvIGnbNKHmqylDmwcSE%2fdUU%3d&risl=&pid=ImgRaw&r=0")
        st.write("---")

        st.subheader("**2-  Prédiction du prix dune voiture avec un modèle KNN**")
        st.write(""" 
                 **Description** : 

Le projet consiste à développer un modèle de machine learning utilisant l’algorithme des **k-plus proches voisins (K-Nearest Neighbors, KNN)** pour prédire le prix d’une voiture en fonction de ses caractéristiques.
En fin, implémenter le modèle dans une application web utilisable par tous.
                 
### **Objectif du projet**  
Prédire le prix d’une voiture donnée en utilisant un modèle KNN basé sur les données historiques des ventes automobiles. Le modèle apprend les relations entre les caractéristiques des voitures (par exemple, la marque, l’année, le kilométrage) et leurs prix afin de fournir des prédictions pour de nouvelles observations.

### **Étapes clés**  

1. **Collecte des données**  
   - Source des données : Jeux de données publics ou propriétaires sur les ventes de voitures, collecté et mise à la disposible par Jeffrey C. Schlimmer (Jeffrey.Schlimmer@a.gp.cs.cmu.edu).  
   - Variables importantes : 
     - Caractéristiques : *Marque, modèle, année de fabrication, kilométrage, type de carburant, transmission, puissance du moteur, etc.*
     - Cible : *Prix de la voiture*.  

2. **Exploration et préparation des données**  
   - Nettoyage des données : 
     - Gestion des valeurs manquantes (par exemple, imputation).
     - Conversion des variables catégorielles (ex. marque) en variables numériques à l’aide de techniques comme le **One-Hot Encoding**.
   - Normalisation des variables : Les distances dans le KNN sont influencées par l'échelle des données. Une normalisation est donc essentielle pour les variables continues.  

3. **Division des données**  
   - Séparation en ensembles : *Entraînement (70-80%)* et *test (20-30%)*.  

4. **Construction du modèle KNN**  
   - Définir les hyperparamètres : 
     - *k* : Nombre de voisins (souvent déterminé via validation croisée).
     - Mesure de distance : Distance euclidienne ou Manhattan.  
   - Entraîner le modèle en utilisant les données d'entraînement.  

6. **Optimisation des hyperparamètre**  
   - Les hyperparamètres ont été optimisé à l'aide du GridSearchCV et d'une Validation Croisée.

5. **Évaluation du modèle**  
   - Utilisation de métriques d’évaluation telles que :
     - Erreur quadratique moyenne (**RMSE**).
     - Score R².  
   - Comparaison des performances pour différents *k* afin de trouver le meilleur paramètre.
                 
7. **Prédiction**  
   - Le modèle prédit le prix d'une voiture en calculant les distances entre la voiture cible et les *k* observations les plus proches dans l'ensemble d'entraînement, puis en prenant la moyenne (ou une autre agrégation) des prix des voisins.  

### **Avantages du KNN dans ce projet**  
- **Facilité d’implémentation** : KNN est simple à configurer.  
- **Non-paramétrique** : Pas besoin de supposer une forme spécifique pour la distribution des données.  
- **Flexibilité** : Gère bien les données avec des relations complexes entre les variables.  

### **Limitations potentielles**  
- **Sensibilité à l’échelle des données** : Nécessite une normalisation appropriée.  
- **Complexité en temps** : Pour de grands ensembles de données, la recherche des *k* voisins peut être coûteuse.  
- **Sensibilité au bruit** : Les observations bruitées peuvent fausser les prédictions.  

### **Outils et technologies utilisés**  
- **Python** : Langage principal.
- **Bibliothèques** : 
  - `scikit-learn` pour l’implémentation de KNN.
  - `pandas` et `numpy` pour la manipulation des données.
  - `matplotlib` et `seaborn` pour les visualisations.  

### **Résultat attendu**  
Un modèle capable de fournir des prédictions précises et fiables sur le prix des voitures, et un tableau de bord interactif (optionnel avec **Streamlit**) pour visualiser les prédictions et explorer les données.
                 """)
        st.image("https://blog.vivacar.fr/wp-content/uploads/2017/03/estimer-prix-voiture.webp")

        st.write("---")
        
        st.subheader("**Crédit Scoring avec Régression Logistique et Arbre de Décision**")

        st.write("""
        Ce projet vise à développer un système de **crédit scoring** pour évaluer la probabilité qu’un client rembourse ou non son crédit, en utilisant deux modèles de machine learning : la **régression logistique** et l’**arbre de décision**.


        ### **Objectif du projet**  
        Fournir un outil fiable qui aide les institutions financières à prendre des décisions éclairées sur l'octroi de crédits, en classant les clients en deux catégories :  
        1. *Solvables* (remboursement probable).  
        2. *Non solvables* (risque de défaut).

        ### **Étapes clés**  

        #### 1. **Collecte des données**  
        - Sources potentielles :  
        - Datasets publics comme *Credit Default Dataset* ou *Home Credit Default Risk*.  
        - Données réelles des institutions financières.  
        - Variables utilisées :  
        - **Caractéristiques** (*inputs*) : âge, sexe, statut matrimonial, revenu mensuel, montant du crédit, historique de crédit, ratio dette/revenu, etc.  
        - **Cible** (*output*) : Classe binaire (0 : remboursé, 1 : défaut).

        #### 2. **Exploration et préparation des données**  
        - Nettoyage des données :  
        - Gestion des valeurs manquantes et outliers.  
        - Encodage des variables catégorielles (par exemple, *sexe*, *statut matrimonial*).  
        - Transformation des données :  
        - Standardisation pour la régression logistique (centrage et réduction des variables).  
        - Préparation des données catégorielles pour l’arbre de décision.  
        - Gestion des classes déséquilibrées :  
        - Utilisation de techniques comme **SMOTE** ou pondération des classes.

        #### 3. **Division des données**  
        - Division en ensembles d'entraînement (70-80%) et de test (20-30%).  

        #### 4. **Modélisation**  
        **Régression logistique** :  
        - Modèle statistique qui estime la probabilité d’appartenance à une classe en fonction d’une fonction logistique.  
        - Analyse des coefficients pour comprendre l’influence de chaque caractéristique sur la probabilité de défaut.  

        **Arbre de décision** :  
        - Modèle basé sur une structure arborescente pour classer les clients en fonction de règles décisionnelles.  
        - Facile à interpréter, avec des visualisations montrant les critères de décision (par exemple, seuils de revenu ou d’endettement).  

        #### 5. **Évaluation des modèles**  
        - Métriques utilisées :  
        - **Accuracy** : Précision globale.  
        - **Précision et rappel** : Évaluer les performances sur la classe "défaut".  
        - **AUC-ROC** : Comparer les capacités discriminatoires des deux modèles.  
        - Comparaison des performances pour choisir le modèle le plus adapté.  

        #### 6. **Prédiction et interprétation**  
        - Génération de prédictions pour de nouveaux clients.  
        - Analyse des erreurs (faux positifs et faux négatifs).  

        ### **Avantages des modèles utilisés**  
        **Régression logistique** :  
        - Facile à interpréter.  
        - Performant pour des relations linéaires entre les variables et la cible.  

        **Arbre de décision** :  
        - Compréhensible pour les non-experts grâce aux visualisations.  
        - Capture les relations non linéaires et les interactions entre variables.  

        ### **Outils et technologies utilisés**  
        - **Python** : Langage principal.  
        - Bibliothèques :  
        - `pandas` et `numpy` pour la manipulation des données.  
        - `scikit-learn` pour les modèles de machine learning.  
        - `matplotlib` et `seaborn` pour les visualisations.  
        - `imbalanced-learn` pour gérer les déséquilibres de classes.

        ### **Résultats attendus**  
        - **Modèle prédictif robuste** pour évaluer la solvabilité des clients.  
        - **Visualisation des résultats** : Courbe ROC, arbre de décision, etc.  
        - **Application pratique** : Une interface simple (par exemple avec **Streamlit**) pour prédire la classe des clients en temps réel.
                 """)

        st.image("https://wrestlingjunkie.usatoday.com/gcdn/-mm-/b240875430a593c78f8a88c3e24a2d274266415a/c=0-34-580-360/local/-/media/2017/09/17/USATODAY/usatsports/credit-score-over-800_large.jpg?width=579&height=326&fit=crop&format=pjpg&auto=webp")

    with tabs[1]:
        st.subheader("**Tableau de Bord pour la Gestion d’un Supermarché**")
        st.write("""   
Ce projet vise à concevoir un tableau de bord interactif pour visualiser et analyser les performances d’un supermarché, en utilisant des données historiques sur les ventes, les produits, et les clients. Cet outil aide les gestionnaires à prendre des décisions éclairées pour améliorer les ventes, optimiser les stocks et comprendre le comportement des clients.  

### **Objectif du projet**  
Créer un tableau de bord dynamique et interactif permettant :  
1. De suivre les indicateurs clés de performance (KPI) comme le chiffre d’affaires, les marges, et les ventes par catégorie.  
2. D’identifier les tendances et les produits les plus performants.  
3. D’améliorer la gestion des stocks et les stratégies de marketing.

### **Étapes clés**  

#### 1. **Collecte des données**  
- **Sources de données** :  
Il s'agit d'une base donnée issue d'un supermarché des USA  
- **Variables importantes** :  
  - *Date*, *produit*, *quantité vendue*, *prix unitaire*, *catégorie de produit*.  
  - Données clients : âge, sexe, localisation, fréquence d’achat.  

#### 2. **Nettoyage et préparation des données**  
- Gestion des valeurs manquantes et suppression des doublons.  
- Création de nouvelles variables :  
  - Revenus = Quantité × Prix unitaire.  
  - Marges = Revenus - Coûts des produits.  
- Agrégation par périodes (jours, semaines, mois) et par catégories de produits.  

#### 3. **Conception des visualisations**  
- Graphiques interactifs pour :  
  - **Suivi des ventes** : Ligne temporelle pour analyser les variations du chiffre d’affaires.  
  - **Analyse par catégorie de produit** : Histogrammes ou diagrammes circulaires.  
  - **Localisation des ventes** : Carte géographique pour les analyses régionales.  
  - **Performance des produits** : Tableau des produits les plus vendus avec indicateurs (revenu, profit).  
  - **Analyse des clients** : Segmentation des clients selon leur fréquence d’achat ou panier moyen.  

#### 4. **Création du tableau de bord avec Streamlit**  
- Intégration des données nettoyées et pré-traitées.  
- Ajout de widgets interactifs :  
  - Sélection des périodes (*date picker*).  
  - Filtres par catégorie de produit, région, ou client.  
  - Visualisations dynamiques : possibilité de zoomer, filtrer, ou télécharger les données.  

#### 5. **Analyse approfondie**  
- Identification des périodes de forte et faible activité (saisonnalité).  
- Analyse des produits invendus ou à faible rotation.  
- Segmentation des clients pour les campagnes ciblées.  


### **Avantages du tableau de bord**  
- **Vision globale** : Accès rapide aux indicateurs clés.  
- **Facilité d’utilisation** : Interface intuitive et interactive pour les gestionnaires.  
- **Prise de décision basée sur les données** : Meilleure compréhension des performances pour ajuster les stratégies.  


### **Outils et technologies utilisés**  
- **Python** pour le traitement et la visualisation des données.  
- Bibliothèques :  
  - `pandas` et `numpy` pour la manipulation des données.  
  - `matplotlib` et `seaborn` pour les graphiques statiques.  
  - `plotly` et `seaborn` pour les visualisations interactives.  
  - **Streamlit** pour la création de l’interface utilisateur.  

### **Résultats attendus**  
Un tableau de bord opérationnel avec :  
- Une présentation claire et intuitive des données.  
- Des filtres interactifs pour personnaliser l’analyse.  
- Des recommandations basées sur les tendances identifiées (ex. produits à prioriser, périodes de forte demande).  

Ce tableau de bord peut être utilisé par les gestionnaires pour optimiser les performances et ajuster les stratégies de gestion et de marketing.
""")

if __name__ == "__main__":

    home()
