# coding : utf-8

#Salut JH! Voici mon devoir 4. Ça s'est très bien passé grâce à tout ce qu'on a vu en classe. Voici mon script:

### BONJOUR SANDRINE
### SUPER! ALLONS VOIR CELA

#Importation des modules nécessaires, Spacy, Counter et CSV afin de lire le csv des chroniques de Martineau
import csv
import spacy
from collections import Counter

#Pour le langage français de spacy
tal = spacy.load("fr_core_news_md")

# Comme noté dans le cours, je retranche le mot "gens" des mots vides. 
tal.Defaults.stop_words.remove("gens")
#Pour comprendre cette commande, voir note de fin*
tal.Defaults.stop_words.add("y")

### EN EFFET, CELA NE SEMBLE FINALEMENT PAS PRODUIRE L'EFFET ESCOMPTÉ...
### POURTANT, QUAND ON PRINT LA LISTE DES MOTS VIDES, ON CONSTATE QUE LE "Y" S'Y TROUVE... MYSTÈRE...
# print(tal.Defaults.stop_words)

#On commence le code. Je vais chercher les infos dans le fichier csv avec la formule habituelle. 
# chroniquesmartino = "martino.csv"
chroniquesmartino = "../martino.csv" ### ICI, JE CHANGE SEULEMENT LE "CHEMIN" VERS LE FICHIER POUR QUE TON SCFRIPT PUISSE FONCTIONNER SUR MON ORDI
f = open(chroniquesmartino)
contenu = csv.reader(f)
next(contenu)

#Création de la liste qui contiendra des paires de mots. 
LesPaires = []

#Création de la boucle pour trouver les infos:
for chronique in contenu:
    #print(chronique)
    #ça marche
    print(chronique[1]) ### J'AIME BIEN FAIRE UN AFFICHAGE, COMME ICI DE LA DATE, POUR VOIR LA PROGRESSION DE MON SCRIPT DANS LE TERMINAL
    # articles = chronique[3]
    ### POUR RÉGLER UN PROBLÈME QUE TU AS MENTIONNÉ PLUS BAS, J'AI CHANGÉ TA LIGNE CI-DESSUS PAR LA LIGNE CI-DESSOUS
    articles = chronique[3].replace("\xa0", " ").replace("  "," ").strip()
    doc = tal(articles)

    #Retrancher la ponctuation et les mots vides
    ### LES DEUX LIGNES CI-DESSOUS SONT BONNES, MAIS LA DEUXIÈME ÉCRASE LA VARIABLE "LEMMES" DÉFINIE DANS LA PREMIÈRE
    ### LA DIFFÉRENCE PRINCIPALE EST QUE ".TEXT" VA CONSERVER LES MAJUSCULES, ALORS QUE ".LEMMA_" PAS;
    ### TU AURAS DONC MOINS DE BIGRAMS QUI RÉPONDRONT À LA CONDITION QUE TU FIXES À LA LIGNE 57
    lemmes = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False]
    lemmes = [token.text for token in doc if token.is_stop == False and token.is_punct == False]
    
    #Deuxième boucle pour la création des paires de mots, tel que vu en classe
    for x, y in enumerate(lemmes[:-1]):
        bigrams = "{} {}".format(lemmes[x],lemmes[x + 1])

        #Création d'une condition dans la deuxième boucle, afin d'aller viser les paires de mots contenant "islam" et "musulm". 
        if "islam" in bigrams or "musulm" in bigrams:
            LesPaires.append(bigrams)

    print(len(LesPaires)) ### POUR VOIR LE SCRIPT TRAVAILLER

#Formule finale pour les 50 paires de mots les plus fréquentes. 
freq = Counter(LesPaires)
print(freq.most_common(50))
#Tout fonctionne, quoique les les paires de mots se sont affichées après un bon délai (3-4 minutes), je ne sais pas si c'est normal? ### OUI C'EST NORMAL; POUR VOIR TON SCRIPT TRAVAILLER, FAIT DES PRINT DES ÉTAPES IMPORTANTES

#Juste pour vérifier que tout est 100% correct
print(len(LesPaires))

#Note de fin: En regardant les résultats, je note qu'une paire contient "y, musulman". Je retourne plus haut l'ajouter aux mots vides.
#Je remarque aussi des ""\xa0" dans les résultats. Selon le web, il s'agit des non-breaking space. J'ai cherché comment faire pour les retirer, sans succès. Ça semblait assez complexe.
#Je ne sais pas s'il me manque une étape plus haut qui ferait en sorte que ça serait filtré? ### UTILISER LES LEMMES, EN GÉNÉRAL, PERMET D'ALLER À L'ESSENCE DU TEXTE
#Merci JH!

### BRAVO! LES COMMENTAIRES QUE TU AJOUTES DÉMONTRENT QUE TU AS CHERCHÉ À COMPRENDRE CE QUE TU FAISAIS ET POURQUOI CERTAINES CHOSES NE FONCTIONNAIENT PAS