

                                               # le programme principale
        ########################################################################################################################




                                            # importer les fonctions du travail
                        #################################################################################
from fichier_travail import remplissage_validation_matrice
from fichier_travail import deuxieme_choix
from fichier_travail import choix_utilisateur
from fichier_travail import borne_sup
from fichier_travail import borne_inferieur
from fichier_travail import diametre_graphe
from fichier_travail import mat_graphe
from fichier_travail import trouve_cycle
from fichier_travail import chaine_matrice_utilisateur
from fichier_travail import degree_graphe
from fichier_travail import degree_chaque_sommet
from fichier_travail import sous_ensemble_stable
from fichier_travail import liste_sommet
from fichier_travail import retourner_dictionnaire
from fichier_travail import ordonner_les_sommets

                        #################################################################################





                                                        # le travail
                                ##################################################################

print("-------------------------------------------------------------BIENVENUE---------------------------------------------------------------------------")
test = False             # initialiser un test pour repeter autre fois ce programme suivant le choix de l'utilisateur
while test != True :
    print()                                   # afficher un retour a la ligne
    matrice = []
    dictionnaire_matrice = {}
    liste_s = []
    chaine = []
    sommet_ordonnee = []
    matrice = remplissage_validation_matrice()
    dictionnaire_matrice = retourner_dictionnaire(matrice)
    liste_s = liste_sommet(matrice)
    degree = degree_graphe(dictionnaire_matrice)
    visite = set()
    diametre = len(diametre_graphe(visite,matrice,0))
    print()
    print(f"LE DIAMETRE DE LA GRAPHE EST {diametre}")
    print()
    degree_chaque_sommet(dictionnaire_matrice)
    print()
    print("LES SOUS ENSEMBLES STABLES : ")
    sous_ensemble_stable(matrice)
    choix = choix_utilisateur()
    if choix == 1 :
        test = False
        while test != True :
            print("ENTRER LE NOM DE VOTRE SOMMET : ")
            s = input('---> ')
            if s in liste_s :
                test = True
        indice = liste_s.index(s)
        mat_graphe(matrice,indice)
    elif choix == 2 :
        chaine = chaine_matrice_utilisateur(matrice,liste_s)
        print(chaine)
        print()
    else :
        ch = []
        ch = chaine_matrice_utilisateur(matrice,liste_s)
        trouve_cycle(ch)
        print()


    borne_superieur = borne_sup(matrice)
    sommet_ordonnee = ordonner_les_sommets(matrice,liste_s)
    borne_inf = borne_inferieur(matrice,sommet_ordonnee)
    print()
    print(f"LE BORNE superieur EGALE A {borne_superieur}")
    print()
    print(f"LE BORNE inferieur EGALE A {borne_inf}")
    print()
    choix_2 = deuxieme_choix()
    if choix_2 == 1:  # la premiere condition
        test = False
    else:
        test = True  # la deuxieme condition
        print("-------------------------------------------------------------AU REVOIR---------------------------------------------------------------------------")

                                    ########################################################################

                ########################################################################################################################





























                