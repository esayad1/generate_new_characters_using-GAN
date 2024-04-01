# -*- coding: utf-8 -*-


import streamlit as st
from PIL import Image
from keras.models import load_model
import numpy as np
import base64
from io import BytesIO
import os
# CSS pour l'effet de survol et les cadres
hover_css = """
<style>
.hover-effect img {
    transition: transform .2s; /* Animation */
    margin: 0 auto;
    border: 3px solid #ccc; /* Bordure de l'image */
    border-radius: 10px; /* Coins arrondis */
}
.hover-effect img:hover {
    transform: scale(1.1); /* Agrandir l'image */
}
.hover-effect p {
    text-align: center;
    margin-top: 5px;
    border: 2px solid #ccc; /* Bordure du nom */
    border-radius: 5px; /* Coins arrondis pour le nom */
    padding: 5px;
}
</style>
"""
# CSS pour réduire l'espace en haut de la page
space_css = """
<style>
/* Réduire l'espace autour du corps de l'application */
     body {
    margin-top: 0px; /* Ajustez cette valeur à 0px ou une autre valeur qui convient mieux à votre design */
}

/* Style personnalisé pour le titre */
.title-style {
    font-size: 40px;
    font-weight: bold;
    color: #0078D4;
    text-align: center;
    margin-top: 20px;
    margin-bottom: 20px;
}
</style>
"""
# CSS pour styliser le bouton
button_css = """
<style>
button {
    background-color: #0078D4; /* Couleur de fond */
    color: white; /* Couleur du texte */
    padding: 10px 20px; /* Padding autour du texte */
    border-radius: 5px; /* Bordures arrondies */
    border: none; /* Pas de bordure */
    outline: none; /* Pas de contour */
    transition: all 0.3s ease; /* Animation */
}

button:hover {
    background-color: #0056b3; /* Couleur de fond au survol */
    transform: scale(1.1); /* Agrandir légèrement */
}
</style>
"""


# CSS pour le conteneur flexible et l'effet de survol
flex_container_css = """
<style>
.flex-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
.hover-effect img {
    transition: transform .2s; /* Animation */
    margin: 10px;
    border: 3px solid #ccc; /* Bordure de l'image */
    border-radius: 10px; /* Coins arrondis */
}
.hover-effect img:hover {
    transform: scale(1.1); /* Agrandir l'image */
}
</style>
"""



st.markdown(flex_container_css, unsafe_allow_html=True)


st.markdown(hover_css, unsafe_allow_html=True)

st.markdown(space_css, unsafe_allow_html=True)

st.markdown('<h1 class="title-style">Générateur de personnages One Piece</h1>', unsafe_allow_html=True)
st.markdown(button_css, unsafe_allow_html=True)





# Charger le modèle GAN
model = load_model('./Models/mon_gan.h5')

# Fonction pour générer une image
def generer_image(model):
    noise = np.random.normal(0, 1, (1, 100))  # Exemple de génération de bruit
    generated_image = model.predict(noise)[0]
    generated_image = (generated_image * 127.5 + 127.5).astype(np.uint8)
    return Image.fromarray(generated_image)

# Fonction pour charger et redimensionner une image
def charger_et_redimensionner_image(chemin, taille=(256, 256)):
    img = Image.open(chemin)
    img = img.resize(taille)
    return convertir_image_base64(img)

def convertir_image_base64(img):
    """ Convertit une image PIL en chaîne base64 pour l'HTML. """
    if img.mode != 'RGB':
        img = img.convert('RGB')
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/jpeg;base64,{img_str}"



taille_image = (256, 256)

col1, col2, col3,col4,col5 = st.columns(5)

# Charger les images
img_luffy = charger_et_redimensionner_image('./Data display/Luffy/6.jpg', taille_image)
img_shanks = charger_et_redimensionner_image('./Data display/Shanks/1.png', taille_image)
img_ace = charger_et_redimensionner_image('./Data display/Ace/8.jpg', taille_image)
img_zoro = charger_et_redimensionner_image('./Data display/Zoro/1.jpg', taille_image)
img_nami = charger_et_redimensionner_image('./Data display/Nami/5.jpg', taille_image)



# Liste des personnages et descriptions
personnages = ["Luffy", "Shanks", "Ace", "Zoro", "Nami","Akainu","Brook","Chopper","Crocodile","Franky","Jinbei","Kurohige","Mihawk","Robin","Sanji","Shanks","Usopp"]
personnages_descriptions = {
    "Luffy": "Charismatique et intrépide, Luffy est déterminé à trouver le One Piece et à devenir le Roi des Pirates. Son style de combat est principalement basé sur l'élasticité de son corps, lui permettant de lancer des coups puissants. Il est aussi extrêmement résilient et possède une volonté indomptable.",
    "Ace": " Frère de Luffy, Ace est courageux, loyal et a un sens aigu de la justice. Il est très populaire et respecté parmi les pirates et a un passé complexe lié à son père, le Roi des Pirates, Gol D. Roger.",
    "Zoro": " Zoro est déterminé, sérieux et souvent stoïque. Il s'entraîne constamment pour atteindre son objectif de devenir le meilleur épéiste. Zoro est également connu pour son sens de l'orientation terriblement mauvais.",
    "Nami": " Nami est intelligente, rusée et a un faible pour l'argent. Cependant, elle est extrêmement loyale envers ses amis et a un passé douloureux lié à la piraterie et à la perte de sa famille adoptive.",
    "Akainu": "Akainu est impitoyable et croit fermement en une justice absolue. Il est prêt à tout pour éradiquer la piraterie, ce qui le rend l'un des antagonistes les plus redoutés de la série.",
    "Brook": "Malgré son apparence de squelette, Brook est joyeux et souvent le cœur de la fête. Il a une obsession pour les sous-vêtements et aime jouer de la musique. Son passé est tragique, ayant perdu tous ses anciens compagnons de l'équipage.",
    "Chopper": "Chopper est naïf, innocent et souvent agit comme un enfant. Il admire profondément ses compagnons et aspire à devenir un médecin capable de guérir n'importe quelle maladie.",
    "Crocodile": "Crocodile est intelligent, calculateur et impitoyable. Il a un grand sens des affaires et de la stratégie, souvent plusieurs coups d'avance sur ses adversaires.",
    "Franky": ": Franky est excentrique, flamboyant et a un cœur d'or. Il est passionné par la construction navale et est fier de ses créations, notamment le navire de l'équipage, le Thousand Sunny.",
    "Jinbei": "Jinbei est calme, réfléchi et extrêmement honorable. Il joue souvent le rôle de médiateur et est profondément engagé dans la cause des hommes-poissons et leur traitement dans le monde de One Piece.",
    "Kurohige": "Teach est ambitieux, rusé et sans scrupules. Il est connu pour sa philosophie nihiliste et sa capacité à manipuler les autres pour atteindre ses objectifs.",
    "Mihawk": "Mihawk est solitaire, stoïque et incroyablement concentré sur son art. Il vit dans un château isolé et semble prendre un intérêt particulier à suivre le développement de Zoro.",
    "Robin": "Robin est calme, mystérieuse et très intelligente. Elle a une connaissance approfondie de l'histoire et de l'archéologie, ce qui la rend indispensable pour découvrir les secrets du monde de One Piece.",
    "Sanji": "Sanji est un gentleman, un romantique et un cuisinier de génie. Il a un code moral strict qui l'empêche de frapper les femmes. Son passé est complexe et lié à une famille royale de scientifiques et de combattants.",
    "Shanks": " Shanks est détendu, joyeux et incroyablement puissant. Il joue un rôle clé dans le début de l'aventure de Luffy et est respecté même par ses ennemis pour son honneur et sa force.",
    "Usopp": "Usopp est un rêveur, un artiste et un stratège. Bien qu'il soit souvent peureux, il a un courage incroyable lorsqu'il s'agit de protéger ses amis. Son père est un pirate sous le commandement de Shanks."
               }


# Créer un menu latéral pour la sélection des personnages
with st.sidebar:
    st.title("Menu des personnages")
    personnage_choisi = st.selectbox("Choisissez un personnage", [""] + personnages)





if not personnage_choisi:
    # Galerie de personnages existants  
    with col1:
        st.markdown(f"""
        <div class="hover-effect">
            <img src="{img_luffy}" alt="Luffy" style="width:100%">
        </div>
        <p>Luffy</p>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="hover-effect">
            <img src="{img_shanks}" alt="Shanks" style="width:100%">
        </div>
        <p>Shanks</p>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="hover-effect">
            <img src="{img_ace}" alt="Ace" style="width:100%">
        </div>
        <p>Ace</p>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="hover-effect">
            <img src="{img_zoro}" alt="Zoro" style="width:100%">
        </div>
        <p>Zoro</p>
        """, unsafe_allow_html=True)
    with col5:
        st.markdown(f"""
        <div class="hover-effect">
            <img src="{img_nami}" alt="Nami" style="width:100%">
        </div>
        <p>Nami</p>
        """, unsafe_allow_html=True)    
        
    st.markdown("<h2>Description de la série One Piece :</h2>", unsafe_allow_html=True)
    col_desc, col_img = st.columns([6, 6])  # Ajustez les proportions si nécessaire
    with col_desc:
        st.markdown("""
            <div style="border: 2px solid #ccc; padding: 10px; border-radius: 10px;">
                <p><b>"One Piece"</b> est une série manga et anime japonaise créée par Eiichiro Oda. Elle a débuté en 1997 et est devenue l'une des séries les plus populaires et les plus longues de l'histoire.</p>
                <p>L'histoire de "One Piece" se déroule dans un monde fictif dominé par les océans, où des pirates aspirent à une ère de liberté et d'aventure. L'intrigue suit Monkey D. Luffy, un jeune homme dont le corps a acquis les propriétés du caoutchouc après avoir mangé un fruit du démon. Luffy explore le Grand Line avec son équipage de pirates, nommé les "Chapeaux de Paille", dans le but de trouver le trésor ultime connu sous le nom de "One Piece" pour devenir le prochain Roi des Pirates.</p>
                <p>Pour ajouter de nouveaux personnages à "One Piece", on pourrait envisager des individus qui apportent de nouvelles dynamiques et compétences à l'univers déjà riche de la série. Ces personnages pourraient avoir des pouvoirs uniques grâce à des fruits du démon non explorés, des origines culturelles diverses reflétant les différents royaumes et îles du monde de One Piece, ou des liens avec des éléments existants de l'histoire pour enrichir la trame narrative.</p>
            </div>
        """, unsafe_allow_html=True)
    with col_img:
        st.image("./Images-pages/manga-one-piece-1070.webp")  
        st.image("./Images-pages/1842996.webp")
        
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
        
    # Bouton pour générer un nouveau personnage
    if st.button('Générer un nouveau personnage'):
        img = generer_image(model)
        st.image(img, caption='Nouveau personnage généré')

# Afficher les informations du personnage choisi
else:    
    st.header(f"{personnage_choisi}")
    st.write(personnages_descriptions[personnage_choisi])

    st.markdown('<div class="flex-container">', unsafe_allow_html=True)
    for i in range(1, 30):  # Supposons qu'il y a plusieurs images par personnage
        for ext in ['.jpg', '.png']:
            chemin_image = f'./Data display/{personnage_choisi}/{i}{ext}'
            if os.path.exists(chemin_image):
                img_base64 = charger_et_redimensionner_image(chemin_image, taille_image)
                st.markdown(f"""
                    <div class="hover-effect">
                        <img src="{img_base64}" style="max-width: 256px; height: auto;">
                    </div>
                """, unsafe_allow_html=True)
                break  # Sortir de la boucle si l'image a été trouvée
    st.markdown('</div>', unsafe_allow_html=True)