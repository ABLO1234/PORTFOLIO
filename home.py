import streamlit as st
import base64


def home():
    
    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="Le portfolio d'Abdoulaye Tangara",
        page_icon="💼",
        layout="wide"
    )

    # CSS styles file
    with open("styles/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Profile image file
    with open("assets/maphoto.png", "rb") as img_file:
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
    st.write(f"""<div class="subtitle" style="text-align: center;color: blue;">Étudiant en Master Économie Quantitative et Calculable</div>""", unsafe_allow_html=True)

    # Social Icons
    social_icons_data = {
        # Platform: [URL, Icon]
        "LinkedIn": ["https://www.linkedin.com/in/abdoulaye-tangara-9219a2293/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
        "GitHub": ["https://github.com/ABLO1234", "https://cdn-icons-png.flaticon.com/512/25/25231.png"],
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
    st.markdown("<h1 style='text-align: center;'>⚠️À la recherche d'opportunités stimulantes !⚠️</h1>",
    unsafe_allow_html=True)
    st.subheader("**À propos de moi** 🧑‍💼")
    st.write("""
    - 🎓 Je suis étudiant en **Master en Economie Quantitative et Calculable**. 
    
        Mon programme de Master combine des connaissances approfondies en théorie économique avec des compétences avancées en modélisation quantitative et calcul informatique.
        Il me permettra de développer des compétences solides en microéconomie, macroéconomie, économétrie, statistiques, optimisation, et programmation (Python, R, STATA, EVIEWS). 
        j'y apprends à construire, estimer et simuler des modèles économiques en s’appuyant sur des techniques telles que l’analyse de séries temporelles, les méthodes bayésiennes, ou encore le machine learning.
    
    - ❤️ Je suis très passioné par le **Machine Learning, Data,  Optimisation, Automatisation ainsi que leur application dans l'économie et dans la finance**, et plus!
                 
    - 🏂 J'aime jouer aux échecs, lire et surtout la musique 🧗
    
    - 📫 Comment me joindre ? 📞 +22372228699 / Par mon adrresse Email ✉️ ci-dessus
    
    - 🏠 Mali, Bamako
    
    ⚠️ **Je suis prêt à relever des défis et à apporter des solutions innovantes. Parlons-en !**
    """)
    st.write("---")
    
    st.subheader("**Mes compétences**")
    
    st.subheader("**Expertise en Analyse et Modélisation de Données** 📊")
    st.write("""
    🔹 Je suis passionné par la transformation de données brutes en informations stratégiques. Grâce à une approche rigoureuse et scientifique, je maîtrise l'ensemble du cycle d'analyse de données à savoir :  

    - ✔️ **Préparation des données** : Nettoyage et structuration de données imparfaites et/ou complexes pour en garantir la qualité et la fiabilité.  
    - ✔️ **Analyse et exploration** : Identification des tendances, des schémas et des insights clés à travers des outils statistiques avancés et des techniques de visualisation.  
    - ✔️ **Modélisation** : Développement de modèles de machine learning adaptés à divers domaines (finance, marketing, énergie, etc.), en optimisant les performances pour répondre à des problématiques spécifiques.  

    🔹 Je suis également compétent dans la conduite d’enquêtes et d’études scientifiques, en assurant leur conception méthodologique, leur réalisation sur le terrain et leur analyse approfondie. Ces capacités me permettent de proposer des solutions basées sur des données concrètes et d'apporter une valeur ajoutée stratégique aux projets sur lesquels je travaille.  

    Avec une expertise en outils 🔧 tels que Python, R, SQL, et une maîtrise des techniques de machine learning 🤖 (régressions, arbres de décision, clustering, etc.), je suis capable d’apporter une réponse adaptée aux besoins analytiques et décisionnels dans divers contextes.  

    Ma vision 🔍: **Transformer les données en un levier puissant pour orienter les stratégies et accompagner la prise de décision éclairée**.
""")
        
    st.subheader("**Langage de programmation**")
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
        st.subheader("1-  **Optimisation de portefeuille d'investissement (Projet en cours)**")
        st.write(""" 
                 **Description** : 
        Il s'agit de l'application de techniques de machine learning à la finance.
        L'objectif du projet est de développer une application web destinée aux investisseurs, leur permettant, 
        à partir des caractéristiques de leur portefeuille, d'optimiser ce dernier en minimisant les risques tout en maximisant les gains. 
                
                 """)
        st.image("https://th.bing.com/th/id/R.29c69915712f9b4ab4ab41b1e1ad0ffa?rik=efeNiqWLFZAqYg&riu=http%3a%2f%2fwww.experts-comptables-fr.org%2fwp-content%2fuploads%2f2017%2f01%2finvestir.jpg&ehk=Axn7KZyNE%2fdSHpHUsLHWyvIGnbNKHmqylDmwcSE%2fdUU%3d&risl=&pid=ImgRaw&r=0")
        st.write("---")

        st.subheader("2-  **Prédiction du prix d'une voiture avec un modèle KNN** 💻")
        st.write(""" 
        🚗 **Description** : 

        Ce projet consistait à concevoir une solution d’Intelligence Artificielle capable de prédire le prix d’une voiture en fonction de ses caractéristiques (marque, année, kilométrage, etc.). 
        🔗L'IA a été intégrée dans une application web interactive, accessible à tous, pour répondre aux besoins des utilisateurs de manière simple et efficace
                 
        🎯**Objectif du projet**  
            
        L'objectif du projet est de fournir une estimation précise et fiable du prix d'une voiture en utilisant une solution d'Intelligence Artificielle basée sur un modèle classification **KNN**, afin d'aider les utilisateurs (particuliers ou professionnels) à évaluer la valeur d'un véhicule en fonction de ses caractéristiques.

        🤖**Quest-ce que le **KNN ou k-plus proches voisins****

        Il s'agit d'un algorithme d’apprentissage supervisé utilisé pour des tâches de classification et de régression. Il est basé sur le principe de proximité dans un espace multi-dimensionnel.
        L'idée principale de ce modèle est que pour une nouvelle donnée (par exemple, une voiture dont on veut prédire le prix), il identifie les k données les plus proches dans l’ensemble d’apprentissage (les "voisins").
        La proximité étant mesurée à l’aide de distances, comme la distance euclidienne et autre pour faire une prédiction, d'une tâche de régression (comme prédire un prix), le KNN calcule une moyenne (ou une autre agrégation) des valeurs cibles des k voisins les plus proches.
        Et une tâche de classification (comme déterminer un type), il assigne la classe majoritaire parmi les k voisins.

        ✨**Les avantages de ce modèle**

        - 📈 Facilité d’implémentation : Simple à configurer.
        - 🛠️ Non-paramétrique : Pas besoin de supposer une forme spécifique pour les données.
        - 🌐 Flexibilité : Gère les relations complexes entre variables.

            ⚠️**Limitations potentielles** 
            
        - 📏 Sensibilité à l’échelle : Exige une normalisation des données.
        - ⏳ Temps de calcul élevé : Recherche des voisins coûteuse pour de grands ensembles de données.
        - 🔊 Sensibilité au bruit : Les données bruitées peuvent affecter les prédictions.

        💡**Pourquoi le modèle KNN est adapté pour ce projet?**  

        Le KNN (k-plus proches voisins) est adapté à cette prédiction du prix d'une voiture pour plusieurs raisons :  

        1. **Simplicité et Intuitivité** :  
        Le KNN compare directement une voiture cible avec des véhicules similaires dans les données historiques, ce qui reflète bien la logique de tarification basée sur des comparaisons.  

        2. **Adaptation à des relations complexes** :  
        Il n'exige pas de supposer une relation linéaire entre les caractéristiques (ex. année, kilométrage) et le prix. Cela le rend flexible pour capturer des relations non linéaires présentes dans les données automobiles.  

        3. **Utilisation des données historiques** :  
        Le KNN se base sur des observations existantes pour fournir une estimation, ce qui est particulièrement utile dans des cas où les données passées sont fiables et représentatives des tendances actuelles.  

        4. **Prise en compte des caractéristiques multiples** :  
        En calculant les distances dans un espace multi-dimensionnel, le KNN considère simultanément plusieurs variables pertinentes (marque, type de carburant, etc.) pour produire une estimation.  

        5. **Facilité de mise en œuvre** :  
        Le KNN est facile à configurer et ne nécessite pas d'entraînement complexe, ce qui le rend efficace pour des projets de prédiction simples.  

        🔧 **Outils et technologies utilisés**  

        -🐍 **Python** : Langage principal.
        
        -📚 **Bibliothèques** : 
        - `scikit-learn` pour l’implémentation de KNN.
        - `pandas` et `numpy` pour la manipulation des données.
        - `matplotlib` et `seaborn` pour les visualisations.  

        📌 **Résultat attendu**  

        **Résultats fonctionnels :**  
        a.✅ **Prédictions précises :**  
        - Fournir une estimation fiable du prix des voitures en fonction de leurs caractéristiques.  
        - Réduire l’erreur entre les prix prédits et les prix réels, mesurée par des métriques comme l’erreur quadratique moyenne (**RMSE**) ou le coefficient de détermination (**R²**).  

        b.💻 **Application interactive :**  
        - Une interface conviviale où les utilisateurs peuvent entrer les caractéristiques d’une voiture et obtenir une estimation instantanée du prix.  

        c.⚙️ **Personnalisation :**  
        - Capacité d’ajuster certains paramètres (par exemple, le nombre de voisins *k*) ou d’explorer les données utilisées pour les prédictions.  

        **Impact pratique :**  
        a.💼 **Prise de décision facilitée :**  
        - Aider les particuliers et les professionnels (vendeurs, acheteurs, concessionnaires) à évaluer rapidement et précisément la valeur d’un véhicule.  

        b.🔍 **Transparence :**  
        - Mettre en avant les voisins considérés pour chaque prédiction, offrant une compréhension claire de l’estimation.  

        **Indicateurs de succès :**  
        a. **Précision :**  
        - Une **RMSE** faible et un score **R²** élevé sur l’ensemble de test.  

        b. **Utilisabilité :**  
        - Temps de réponse rapide et facilité d’utilisation de l’application web streamlit.  

        🌟**Valeur ajoutée globale :**  

        Un système performant et intuitif qui combine la puissance d’un modèle d’IA avec une accessibilité pratique pour répondre à des besoins concrets dans le domaine automobile.                 """)
        st.image("https://blog.vivacar.fr/wp-content/uploads/2017/03/estimer-prix-voiture.webp")

        st.write("---")
        
        st.subheader("**3-  Crédit Scoring avec Régression Logistique et Arbre de Décision**")

        st.write("""
        Ce projet vise à développer un système de **crédit scoring** pour évaluer la probabilité qu’un client rembourse ou non son crédit, en utilisant deux modèles de machine learning : la **régression logistique** et l’**arbre de décision**.

        🎯**Objectif du projet**  
        
        Fournir un outil fiable qui aide les institutions financières à prendre des décisions éclairées sur l'octroi de crédits, en classant les clients en deux catégories :  
        1. *Solvables* (remboursement probable).  
        2. *Non solvables* (risque de défaut).

        🤖**Modèles utilisés : Logistique & Arbre de décision**

        **Régression logistique**
        - Principe :
           Modèle statistique qui prédit la probabilité d’appartenance à une classe (0 ou 1) en utilisant une fonction logistique.
           
        - Avantages :
           Interprétabilité des coefficients (chaque variable montre son effet sur la probabilité de défaut). Performant pour des relations linéaires entre les caractéristiques et la cible.
           
        - Limites :
        Sensibilité aux valeurs extrêmes.
        Nécessite des données bien préparées et standardisées.

        **Arbre de décision**
        
        - Principe :
          Modèle basé sur une structure arborescente qui applique des règles décisionnelles simples pour classer les données.
          
        - Avantages :
        Facile à interpréter grâce à des visualisations (par ex., seuils de revenu ou ratio dette/revenu). Capte les relations non linéaires et les interactions entre les variables.
        
        - Limites :
        Peut sur-apprendre si non régularisé.
        Sensible aux données bruitées.


        🔧 **Outils et technologies utilisés**  
        
        - **Python** : Langage principal.  
        
        - **Bibliothèques** :  
        - `pandas` et `numpy` pour la manipulation des données.  
        - `scikit-learn` pour les modèles de machine learning.  
        - `matplotlib` et `seaborn` pour les visualisations.  
        - `imbalanced-learn` pour gérer les déséquilibres de classes.

       📌 Résultats attendus
       
        ✅ Prédictions fiables :
        Un modèle performant et explicable pour classer les clients.
        Réduction des risques grâce à une précision élevée.
        
       💻 Interface intuitive :
       Application conviviale pour une utilisation pratique par les décideurs.
       
       ⚙️ Transparence des décisions :
       Visualisation des facteurs influençant les prédictions.
       Indicateurs de succès
       
       Performance des modèles :
       AUC-ROC supérieur à 0.75.
       Réduction des faux négatifs pour minimiser les risques.
       
       Utilisabilité :
       Temps de réponse rapide (<1s) pour les prédictions.
        Simplicité d’utilisation pour des utilisateurs non techniques.
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
