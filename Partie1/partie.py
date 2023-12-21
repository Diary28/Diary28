# Auteurs: À compléter

from tp3.Partie1.damier import Damier
from tp3.Partie1.position import Position


class Partie:
    """Gestionnaire de partie de dames.

    Attributes:
        damier (Damier): Le damier de la partie, contenant notamment les pièces.
        couleur_joueur_courant (str): Le joueur à qui c'est le tour de jouer.
        doit_prendre (bool): Un booléen r+eprésentant si le joueur actif doit absolument effectuer une prise
            de pièce. Sera utile pour valider les mouvements et pour gérer les prises multiples.
        position_source_selectionnee (Position): La position source qui a été sélectionnée. Utile pour sauvegarder
            cette information avant de poursuivre. Contient None si aucune pièce n'est sélectionnée.
        position_source_forcee (Position): Une position avec laquelle le joueur actif doit absolument jouer. Le
            seul moment où cette position est utilisée est après une prise: si le joueur peut encore prendre
            d'autres pièces adverses, il doit absolument le faire. Ce membre contient None si aucune position n'est
            forcée.

    """
    def __init__(self):
        """Constructeur de la classe Partie. Initialise les attributs à leur valeur par défaut. Le damier est construit
        avec les pièces à leur valeur initiales, le joueur actif est le joueur blanc, et celui-ci n'est pas forcé
        de prendre une pièce adverse. Aucune position source n'est sélectionnée, et aucune position source n'est forcée.

        """
        self.damier = Damier()
        self.couleur_joueur_courant = "blanc"
        self.doit_prendre = False
        self.position_source_selectionnee = None
        self.position_source_forcee = None

    def position_source_valide(self, position_source):
        """Vérifie la validité de la position source, notamment:
            - Est-ce que la position contient une pièce?
            - Est-ce que cette pièce est de la couleur du joueur actif?
            - Si le joueur doit absolument continuer son mouvement avec une prise supplémentaire, a-t-il choisi la
              bonne pièce?
        Cette méthode retourne deux valeurs. La première valeur est Booléenne (True ou False), et la seconde valeur est
        un message d'erreur indiquant la raison pourquoi la position n'est pas valide (ou une chaîne vide s'il n'y a pas
        d'erreur).

        ATTENTION: Utilisez les attributs de la classe pour connaître les informations sur le jeu! (le damier, le joueur
            actif, si une position source est forcée, etc.
        ATTENTION: Vous avez accès ici à un attribut de type Damier. vous avez accès à plusieurs méthodes pratiques
            dans le damier qui vous simplifieront la tâche ici :)

        Args:
            position_source (Position): La position source à valider.

        Returns:
            bool, str: Un couple où le premier élément représente la validité de la position (True ou False), et le
                 deuxième élément est un message d'erreur (ou une chaîne vide s'il n'y a pas d'erreur).

        """



        # TODO: À compléter
        piece_=self.damier.recuperer_piece_a_position(position_source)
        if piece_ is None:
            return False, "Aucune pièce à la position source."
        if piece_.couleur!=self.couleur_joueur_courant:
            return False,"La pièce à la position source n'appartient pas au joueur actif"
        #if self.doit_prendre and position_source != self.position_source_forcee:
         #   return False, "Le joueur doit absolument continuer avec la pièce qui a effectué la prise précédente."

         #if piece_ is not None:
         #   return True, "Aucune pièce à la position source."


        piece_a_position_source = self.damier.recuperer_piece_a_position(position_source)

        # Vérifier si la position contient une pièce
        # if not piece_a_position_source:
        #    return False, "Aucune pièce à la position source."

        # Vérifier si la pièce appartient au joueur actif
        #if piece_a_position_source.couleur != self.couleur_joueur_courant:
        #    return False, "La pièce à la position source n'appartient pas au joueur actif."

        # Vérifier si le joueur doit absolument continuer son mouvement avec une prise supplémentaire
        #if self.doit_prendre and position_source != self.position_source_forcee:
         #   return False, "Le joueur doit absolument continuer avec la pièce qui a effectué la prise précédente."
        self.position_source_selectionnee=position_source
        return True, "La position source est valide"




    def position_cible_valide(self, position_cible):
        """ Vérifie si la position cible est valide (en fonction de la position source sélectionnée). Doit non seulement
        vérifier si le déplacement serait valide (utilisez les méthodes que vous avez programmées dans le Damier!), mais
        également si le joueur a respecté la contrainte de prise obligatoire.

        Returns:
            bool, str: Deux valeurs, la première étant Booléenne et indiquant si la position cible est valide, et la
                seconde valeur est une chaîne de caractères indiquant un message d'erreur (ou une chaîne vide s'il n'y
                a pas d'erreur).
        """
        # TODO: À compléter


        # Vérifier si une position source a été sélectionnée
        if  self.position_source_selectionnee is None:
            return False, "Aucune position source n'a été sélectionnée."

        # Vérifier si la position cible est dans le damier

        if not self.damier.position_est_dans_damier(position_cible):
            return False, "La position cible n'est pas dans le damier."


        #Récupérer la pièce à la position source
        pos_source = self.position_source_selectionnee
        pos_cible=position_cible
        variable_etat=True
        variable_etat2=True

        # Vérifier si le déplacement serait valide
        if not self.damier.piece_peut_se_deplacer_vers(pos_source,pos_cible):
            variable_etat=False

        if variable_etat==True:

            if  not self.damier.piece_peut_sauter_vers(pos_source,pos_cible):
                 variable_etat2=False

            if variable_etat is False and  variable_etat2 is False:

               return False, "Déplacement invalide."

       # if not self.damier.piece_peut_se_deplacer_vers(pos_source,pos_cible):
        #    return False, "Déplacement invalide."



        # Si le joueur doit prendre, vérifier si la pièce peut effectuer une prise
        if self.doit_prendre==True and not self.damier.piece_peut_sauter_vers(self.position_source_selectionnee, position_cible):
            return False, "Le joueur doit effectuer une prise."

        return True, ""  # La position cible est valide




    def demander_positions_deplacement(self):
        """Demande à l'utilisateur les positions sources et cible, et valide ces positions. Cette méthode doit demander
        les positions à l'utilisateur tant que celles-ci sont invalides.

        Cette méthode ne doit jamais planter, peu importe ce que l'utilisateur entre.

        Returns:
            Position, Position: Un couple de deux positions (source et cible).

        """
        # TODO: À compléter
        while True:
            try:
                # Demander la position source
                source_str = input(f"Joueur {self.couleur_joueur_courant}, veuillez entrer la position source (ligne colonne). Ex: 5 2 : ")
                position_source = Position(*map(int, source_str.split()))

                if not position_source:
                     raise ValueError(message_erreur_source)
                print(position_source)

                # Valider la position source
                validite_source, message_erreur_source = self.position_source_valide(position_source)
                if not validite_source:
                    raise ValueError(message_erreur_source)

                # Demander la position cible
                cible_str = input(f"Joueur {self.couleur_joueur_courant}, veuillez entrer la position cible (ligne colonne): Ex: 5 2 : ")
                position_cible = Position(*map(int, cible_str.split()))

                # Valider la position cible
                validite_cible, message_erreur_cible = self.position_cible_valide(position_cible)
                if not validite_cible:
                    raise ValueError(message_erreur_cible)

                # Si les positions sont valides, retourner le couple de positions
                return position_source, position_cible

            except ValueError as e:
                print(f" Position Invalide  Merci de saisir une Postion Valide !!! (ligne colonne)  ex: 5 2 :   ")



    def tour(self):
        """Cette méthode effectue le tour d'un joueur, et doit effectuer les actions suivantes:
        - Assigne self.doit_prendre à True si le joueur courant a la possibilité de prendre une pièce adverse.
        - Affiche l'état du jeu
        - Demander les positions source et cible (utilisez self.demander_positions_deplacement!)
        - Effectuer le déplacement (à l'aide de la méthode du damier appropriée)
        - Si une pièce a été prise lors du déplacement, c'est encore au tour du même joueur si celui-ci peut encore
          prendre une pièce adverse en continuant son mouvement. Utilisez les membres self.doit_prendre et
          self.position_source_forcee pour forcer ce prochain tour!
        - Si aucune pièce n'a été prise ou qu'aucun coup supplémentaire peut être fait avec la même pièce, c'est le
          tour du joueur adverse. Mettez à jour les attributs de la classe en conséquence.

        """

        # Détermine si le joueur courant a la possibilité de prendre une pièce adverse.
        if self.damier.piece_de_couleur_peut_faire_une_prise(self.couleur_joueur_courant):
            self.doit_prendre = True

        # Affiche l'état du jeu
        print(self.damier)
        print("")
        print("Tour du joueur", self.couleur_joueur_courant, end=".")
        if self.doit_prendre:
            if self.position_source_forcee is None:
                print(" ")
            else:
                print(" Doit prendre avec la pièce en position {}.".format(self.position_source_forcee))
        else:
            print("")

        # Demander les positions
        # TODO: À compléter
        position_source, position_cible=self.demander_positions_deplacement()
        #print("----------lll---")
        #print(self.damier)

        # Effectuer le déplacement (à l'aide de la méthode du damier appropriée)
        # TODO: À compléter
        self.damier.deplacer(position_source,position_cible)


        # Mettre à jour les attributs de la classe
        # TODO: À compléter
        if self.couleur_joueur_courant == "blanc":
            self.couleur_joueur_courant="noir"
        else:
            self.couleur_joueur_courant="blanc"

        self.doit_prendre = False
        self.position_source_selectionnee = None
        self.position_source_forcee = None

    def jouer(self):
        """Démarre une partie. Tant que le joueur courant a des déplacements possibles (utilisez les méthodes
        appriopriées!), un nouveau tour est joué.

        Returns:
            str: La couleur du joueur gagnant.
        """

        while self.damier.piece_de_couleur_peut_se_deplacer(self.couleur_joueur_courant) or \
                self.damier.piece_de_couleur_peut_faire_une_prise(self.couleur_joueur_courant):
            self.tour()

        if self.couleur_joueur_courant == "blanc":
            return "noir"
        else:
            return "blanc"
