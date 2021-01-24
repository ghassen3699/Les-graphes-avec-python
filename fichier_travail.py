



# le remplissage et la validation d'une matrice de graphe
def remplissage_validation_matrice () :
    # les declarations
    ####################################################################################################
    liste_matrice = []

    resultat = False
    #####################################################################################################


    # lire le nombre de sommet de l'utilisateur
    #####################################################################################################
    print("ENTRER LE NOMBRE DE SOMMETS DE VOTRE GRAPHE : ")     # message pour l'utilisateur
    while resultat == False :
        while True :                    # boucle while pour evitter les erreurs de l'utilisation
            try:
                nombre_sommets = int(input("---> "))      # lire le nombre de sommets de l'utilisateur
                break
            except ValueError :                           # la condition d'erreur
                print("ERREUR !!! ENTRER UN ENTIER ")        # le message d'erreur
        if nombre_sommets > 1 :
            resultat = True
        else :
            resultat = False
            print("ERREUR !!! ENTRER UN ENTIER SUPERIER A 1")
    #####################################################################################################



    # initialisation de la liste de matrice
    #####################################################################################################
    for i in range(nombre_sommets):  # boucle for pour parcourir toutes la matrice
        liste_matrice.append(list(nombre_sommets * [0]))  # l'itialisation de la matrice
    #####################################################################################################


    # le remplissage et la validation de la matrice
    #####################################################################################################
    print("LE REMPLISSAGE DE VOTRE MATRICE : ")
    resultat_final = False
    while resultat_final == False :

        for ligne in range(nombre_sommets) :
            for colonne in range(nombre_sommets) :
                test_1 = False
                while test_1 == False :
                    while True:  # boucle while pour evittez les erreurs de l'utilisation
                        try:  # la vrai condition
                            entrer = int(input(f"CASE[{ligne}][{colonne}] = "))  # lire l'entier de l'utilisateur
                            break
                        except ValueError:  # la fausse condition
                            print("ERREUR !!! TAPPER UN ENTIER ")  # le message d'erreur

                    if ((entrer == 0) or (entrer == 1)):  # boucle if pour tester les entrer de l'utilisateur
                        liste_matrice[ligne][colonne] = entrer  # enregistrer l'entier de l'utilisateur
                        test_1 = True  # si il est vrai le test va prendre TRUE
                    else:
                        test_1 = False  # la fausse condition
                        print("ERREUR !!! IL FAUT ENTRER 0 OU 1 ")  # le message d'erreur

        compteur = 0        # initialisation d'un compteur
        element = liste_matrice[0][0]      # initialiser l'element au premier indice de la liste
        for i in range(len(liste_matrice)) :     # parcourir les ligne de la liste
            for j in range(len(liste_matrice)) :     # parcourir les colonnes de la liste
                if i == j :                             # si l'indice de i egale a l'indice de j
                    if liste_matrice[i][j] == element :             # si le contenu de [i][j] egale a l'element
                        compteur += 1                             # incrementation par 1
                else:                                     # si non
                    pass                              # on passe a l'indice suivant
        if compteur >= len(liste_matrice) :            # si le compteur superieur au longueur de la liste matrice
            resultat_final = True                    # le test sera vrai
        else :                                             # si non
            resultat_final = False                    # le test sa sera faux
            print("ERREUR !!! MATRICE NON VALIDE ")         # le message d'erreur
    print("REMPLISSAGE TERMINER ")                     # le message de la validation
    return liste_matrice                    # retourner la liste de la matrice
    ########################################################################################################







# remplir le dictionnaire chaque sommet par son relation
def retourner_dictionnaire(liste_matrice) :
    # les declarations
    #######################################################################################################
    liste_alphabtique = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']
    dictiannaire_relation = {}    # dictionnaire pour enregistrer les relations de chaque sommets
    i = 0         # initialisation d'un compteur
    #######################################################################################################

    for i in range(len(liste_matrice)):       # boucle for pour parcourir les lignes de la matrice
        j = 0        # initialiser d'un autre compteur
        liste_secondaire = []       # initialisation d'une liste
        while j < len(liste_matrice):       # boucle while pour parcourir les colonnes de la matrice
            if liste_matrice[i][j] == 1:          # si le colonne egale 1
                liste_secondaire.append(liste_alphabtique[j])          # enregistrer le nom du sommet
                dictiannaire_relation[liste_alphabtique[i]] = liste_secondaire         # enregistrer le cle et les sommets qu'ils ont des relations avec se cle
            j += 1         # passe au colonne suivant
    #########################################################################################################
    return dictiannaire_relation          # retourner le contenu du dictionnaire





def liste_sommet(matrice):
    liste_alphabtique = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']
    liste_relation = []
    i = 0

    for i in range(len(matrice)) :
        liste_relation.append(liste_alphabtique[i])

    return liste_relation




# le degree de la graphe
def degree_graphe(dictionnaire_matrice):
    degree = len(dictionnaire_matrice)  # calculer le degree de la graphe
    return degree  # retourner le degree de la graphe





# le choix de l'utilisateur
def choix_utilisateur():
    # les declarations
    ###########################################################################################
    global choix  # declaration d'un objet global qui s'appel choix
    test = False  # declaration d'un objet de type boolean pour tester la validation d'une instruction
    ###########################################################################################

    # l'affichage de menu
    ###########################################################################################
    print("ENTRER VOTRE CHOIX : ")  # le message de choix num 1
    print("1) DISTANCE ENTRE DEUX SOMMETS ")  # le message de choix num 2
    print("2) CHAINE")  # le message de choix num 3
    print("3) CYCLE")  # le message de choix num 3
    ###########################################################################################


    # tester le choix de l'utilisateur pour eviter les erreurs
    ###########################################################################################
    while test != True:  # boucle while pour eviter les erreurs de l'utilisation

        while True:  # boucle while pour eviter les erreurs de l'utilisation
            try:  # la vrai condition
                choix = int(input("---> "))  # lire le choix de l'utilisateur
                break
            except ValueError:  # le fausse choix
                print("ERREUR !!! ENTRER UN ENTIER S'IL VOUS PLAIS ")  # le message d'erreur

        if (choix == 1) or (choix == 2) or (choix == 3):  # valider le choix de l'utilisateur
            print("CHOIX VALIDEE")  # le message de validation
            test = True  # le teste va prendre TRUE
        else:  # si il y'a des erreurs
            print("ERREUR !!! ENTRER UNE AUTRE FOIS S'IL VOUS PLAIS ")  # le message d'erreur
            test = False  # le teste va prendre FALSE
    #############################################################################################

    return choix  # retourner le choix de l'utilisateur






# les sous ensembles stables
def sous_ensemble_stable (liste_matrice) :
    # les declarations
    ###############################################################################################
    liste_alphabtique = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z']    # la liste alphabetique
    ###############################################################################################

    # afficher les sous ensenmbles stables
    ###############################################################################################
    for ligne in range(len(liste_matrice)) :      # boucle for pour parcourir tout les lignes d'une matrice
        colonne = 0             # initialisation d'un compteur colonne
        liste_secondaire = []      # initialisation d'une liste
        while colonne < len(liste_matrice) :    # boucle while pour parcourir toutes les colonnes de la matrice
            if liste_matrice[ligne][colonne] == 0 :      # boucle if pour tester les valeurs de la matrice
                liste_secondaire.append(liste_alphabtique[colonne])        # inserer les sommets dans une nouvelle liste
            colonne += 1     # incrementation par 1
        if liste_alphabtique[ligne] in liste_secondaire :          # tester les sommets dans la liste secondaire
            liste_secondaire.remove(liste_alphabtique[ligne])       # suprimer les sommets qui se repete
        for compteur in range(len(liste_secondaire)) :    # boucle for pour parcourir toute la liste
            print(f"{liste_alphabtique[ligne]}----{liste_secondaire[compteur]}")     # afficher les sous ensembles stables
    ###############################################################################################




# degree de chaque sommet
def degree_chaque_sommet (dictionnaire_matrice) :
    for i in (dictionnaire_matrice.keys()) :     # boucle for pour parcourir toute les cles l'un dictionnaire
        print(f"{i} DE DEGREE {len(dictionnaire_matrice[i])}")       # l'affichage






# chaine_utilisateur
def chaine_matrice_utilisateur (matrice,s) :
    n = len(matrice)
    chaine = []
    for i in range(n):
        ch = []
        for j in range(n):
            if matrice[i][j] != 0 :
                ch = s[i]+'-'+s[j]
                if ch not in chaine:
                    chaine.append(ch)
    for i in range(len(chaine)):
        for j in range(len(chaine)):
            if chaine[i][-1] == chaine[j][0] :
                r = chaine[i]
                b = len(r) - 1
                z = r[0:b]
                ch = z + chaine[j]
                if ch not in chaine:
                    chaine.append(ch)

    return (chaine)





# afficher les cycles de la graphe
def trouve_cycle (chaine) :
    cycle = []      # initialisation d'une liste pour enregistrer les cycle
    for x in chaine:       # boucle for pour parcourir les chaines de la graphe
        if (x[0] == x[-1]):     # tester le premier indice et le dernier indice
            cycle.append(x)         # ajouter l'element x
    if len(cycle) == 0 :
        print("GRAPHE SANS CYCLE")
    else :
        print("les cycles sont: ")   # message d'affichage
        for x in cycle:            # parcourir et afficher toutes les cycles
            print(x, end=" , ")
    return (cycle)          # retoutrner les cycles








# afficher les distances entre les sommets :
def mat_graphe (liste,s) :

    # les declarations
    ###############################################################################
    s_inconnu = {}
    infini  = sum(sum(ligne) for ligne in liste) + 1
    nb_sommets = len(liste)
    s_connu = {s : [0 , [s]] }
    s_inconnu = {k : [infini, ''] for k in range(nb_sommets) if k != s}
    ################################################################################

    for suivant in range(nb_sommets) :
        if liste[s][suivant] :
            s_inconnu[suivant] = [liste[s][suivant] , s]

    print("DANS LE GRAPHE D'ORIGINE {} DE MATRICE D'ADJACENTE : ".format(s))
    for ligne in liste :
        print(ligne)
    print()
    print("PLUS COURS CHEMIN de ")

    while s_inconnu and any(s_inconnu[k][0] < infini for k in s_inconnu) :
        u = min(s_inconnu,key = s_inconnu.get)
        longueur_u , precedent_u = s_inconnu[u]
        for v in range(nb_sommets) :
            if liste[u][v] and v in s_inconnu :
                d = longueur_u + liste[u][v]
                if d < s_inconnu[v][0] :
                    s_inconnu[v] = [d,u]
        s_connu[u] = [longueur_u,s_connu[precedent_u][1] + [u] ]
        del s_inconnu[u]
        print("LONGUEUR",longueur_u,":","-->".join(map(str,s_connu[u][1])))

    for k in s_inconnu :
        print("IL N'Y A AUCUN CHEMIN DE {} A {}".format(s,k))





# le diametre de la graphe

def diametre_graphe (visite , graphe , noeud ) :

    if noeud not in visite :
        visite.add(noeud)
        for neighbour in graphe[noeud] :
            diametre_graphe(visite,graphe,neighbour)

    return visite








# les bornes sup et inf de la matrices
def borne_sup (liste_matrice) :
    # les declarations
    ############################################################################################
    liste_max = []   # intialisation d'une liste pour enregistrer les degrees de chaque sommets
    borne_sup = 0    # initialisation de la borne sup de la matrice
    borne_inf = 0    # initialisation de la borne inf de la matrice
    ############################################################################################


    # trouver le bornes sup du gaphe
    ############################################################################################
    for i in range(len(liste_matrice)) :     # parcourir les lignes de la matrices
        compteur = 0         # intialisation d'un compteur pour compter les donnees de chaque sommets
        for j in range(len(liste_matrice)) :       # parcourir les colonnes de la matrices
            if liste_matrice[i][j] == 1 :                  # tester les relations de chaque sommets
                compteur += 1          # incrementation par 1
        liste_max.append(compteur)          # enregistrer le degree de chaque sommets a la liste
    i = 0             # intialisation d'un autre compteur
    borne_sup = liste_max[i]            # le borne sup prendre la premiere valeur de la liste
    for i in range (1,len(liste_max)) :   # parcour de la liste
        if borne_sup < liste_max[i] :        # tester le plus grand degree de sommet de la matrice
            borne_sup = liste_max[i]               # borne sup prendre le sommet le plus grand sommet
    borne_sup += 1
    ###############################################################################################
    return borne_sup







def ordonner_les_sommets (matrice,liste_sommets) :
    ordre = []
    for i in range(len(matrice)) :
        for j in range(len(matrice)) :
            if liste_sommets[j] not in ordre :
                deg = 0
                max_deg = 0
                for k in range(len(matrice)) :
                    if (matrice[j][k] == 1) :
                        deg += 1
                if max_deg < deg :
                    s_max = liste_sommets[j]
        ordre.append(s_max)
    return ordre





def borne_inferieur(matrice,ordre) :
    borne_inf = 0
    couleur = []
    a = []
    c = 0
    for i in range(len(matrice)) :
        if ordre[i] not in couleur :
            test = [ordre[i]]
            for j in range(len(matrice)) :
                if i != j :
                    if matrice[i][j] == 0 :
                        test_2 = True
                        for k in range(len(test)) :
                            if matrice[k][j] != 0 :
                                test_2 = False
                        if test_2 == True :
                            test.append(ordre[j])

        if test not in couleur :
            if test.reverse() not in couleur :
                couleur.append(test)
                couleur.extend(test)
                borne_inf += 1
    return borne_inf






# deusieme choix de l'utilisateur
def deuxieme_choix () :
    # les declarations
    #######################################################################################
    test = False      # intialiser un test pour evitter les erreurs de l'utilisation
    #######################################################################################

    print("VOUS VOULEZ ENTRER UNE AUTRE MATRICE ")       # message pour l'utilisateur
    print("1) OUI")                 # message pour l'utilisateur
    print("2) NON")                 # message pour l'utilisateur
    while test != True :                 # boucle WHILE pour evitter les erreurs de l'utilisation
        while True :                           # boucle WHILE pour evitter les erreurs de l'utlisations
            try:
                choix = int(input("---> "))               # lire le choix de l'utlisateur
                break
            except ValueError :                            # si il y'a des erreurs
                print("ERREUR !!! IL FAUT ENTRER UN ENTIER ")        # le message d'erreur
        if choix == 1 or choix == 2 :                          # la vrai condition
            test = True                                            # le test va prendre vrai
            print("CHOIX VALIDEE ")                             # message de validation
        else :                                                # si il y'a des erreurs
            test = False                                 # le test va prendre faux
            print("ERREUR !!! IL FAUT ENTRER 1 OU 2 ")          # message d'erreur
    return choix                      # retourner le choix




