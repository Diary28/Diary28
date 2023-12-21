# Auteurs: À compléter

from tp3.Partie1.piece import Piece
from tp3.Partie1.position import Position


class Damier:
    """Plateau de jeu d'un jeu de dames. Contient un ensemble de pièces positionnées à une certaine position
    sur le plateau.


    Attributes:
        cases (dict): Dictionnaire dont une clé représente une Position, et une valeur correspond à la Piece
            positionnée à cet endroit sur le plateau. Notez bien qu'une case vide (sans pièce blanche ou noire)
            correspond à l'absence de clé la position de cette case dans le dictionnaire.

        n_lignes (int): Le nombre de lignes du plateau. La valeur est 8 (constante).
        n_colonnes (int): Le nombre de colonnes du plateau. La valeur est 8 (constante).

    """

    def __init__(self):
        """Constructeur du Damier. Initialise un damier initial de 8 lignes par 8 colonnes.

        """
        self.n_lignes = 8
        self.n_colonnes = 8

        self.cases = {
            Position(7, 0): Piece("blanc", "pion"),
            Position(7, 2): Piece("blanc", "pion"),
            Position(7, 4): Piece("blanc", "pion"),
            Position(7, 6): Piece("blanc", "pion"),
            Position(6, 1): Piece("blanc", "pion"),
            Position(6, 3): Piece("blanc", "pion"),
            Position(6, 5): Piece("blanc", "pion"),
            Position(6, 7): Piece("blanc", "pion"),
            Position(5, 0): Piece("blanc", "pion"),
            Position(5, 2): Piece("blanc", "pion"),
            Position(5, 4): Piece("blanc", "pion"),
            Position(5, 6): Piece("blanc", "pion"),
            Position(2, 1): Piece("noir", "pion"),
            Position(2, 3): Piece("noir", "pion"),
            Position(2, 5): Piece("noir", "pion"),
            Position(2, 7): Piece("noir", "pion"),
            Position(1, 0): Piece("noir", "pion"),
            Position(1, 2): Piece("noir", "pion"),
            Position(1, 4): Piece("noir", "pion"),
            Position(1, 6): Piece("noir", "pion"),
            Position(0, 1): Piece("noir", "pion"),
            Position(0, 3): Piece("noir", "pion"),
            Position(0, 5): Piece("noir", "pion"),
            Position(0, 7): Piece("noir", "pion"),
        }



    def recuperer_piece_a_position(self, position):
        """Récupère une pièce dans le damier à partir d'une position.

        Args:
            position (Position): La position où récupérer la pièce.

        Returns:
            La pièce (de type Piece) à la position reçue en argument, ou None si aucune pièce n'était à cette position.

        """
        if position not in self.cases:
            return None

        return self.cases[position]



    def position_est_dans_damier(self, position):
        """Vérifie si les coordonnées d'une position sont dans les bornes du damier (entre 0 inclusivement et le nombre
        de lignes/colonnes, exclusement.

        Args:
            position (Position): La position à valider.

        Returns:
            bool: True si la position est dans les bornes, False autrement.
        """
        # TODO: À compléter
        return 0 <= position.ligne < self.n_lignes and  0 <= position.colonne < self.n_colonnes



    def piece_peut_se_deplacer_vers(self, position_piece, position_cible):
        """Cette méthode détermine si une pièce (à la position reçue) peut se déplacer à une certaine position cible.
        On parle ici d'un déplacement standard (et non une prise).

        Une pièce doit être positionnée à la position_piece reçue en argument (retourner False autrement).

        Une pièce de type pion ne peut qu'avancer en diagonale (vers le haut pour une pièce blanche, vers le bas pour
        une pièce noire). Une pièce de type dame peut avancer sur n'importe quelle diagonale, peu importe sa couleur.
        Une pièce ne peut pas se déplacer sur une case déjà occupée par une autre pièce. Une pièce ne peut pas se
        déplacer à l'extérieur du damier.

        Args:
            position_piece (Position): La position de la pièce source du déplacement.
            position_cible (Position): La position cible du déplacement.

        Returns:
            bool: True si la pièce peut se déplacer à la position cible, False autrement.


        # TODO: À compléter

        """
        if not self.position_est_dans_damier(position_piece):
            return False

        # Récupérer la pièce à la position_piece
        piece_source = self.recuperer_piece_a_position(position_piece)

        # Vérifier si la pièce source existe
        if piece_source is None:
            return False

        # Vérifier si la position_cible est dans le damier
        if not self.position_est_dans_damier(position_cible):
            return False

        # Récupérer la pièce à la position_cible
        piece_cible = self.recuperer_piece_a_position(position_cible)

        # Vérifier si la case cible est vide
        if piece_cible is not None:
            return False  # La case est occupée, la pièce ne peut pas se déplacer

        # Vérifier si la pièce peut se déplacer en fonction de ses règles spécifiques
        if piece_source.est_pion():
            # Vérifier le déplacement en diagonale pour un pion
            delta_ligne = position_cible.ligne - position_piece.ligne
            delta_colonne = position_cible.colonne - position_piece.colonne

            if piece_source.est_blanche():
                return delta_ligne == -1 and abs(delta_colonne) == 1
            elif piece_source.est_noire():
                return delta_ligne == 1 and abs(delta_colonne) == 1
        elif piece_source.est_dame():
            # Vérifier le déplacement en diagonale pour une dame (peu importe la couleur)
            return abs(position_cible.ligne - position_piece.ligne) == abs(position_cible.colonne - position_piece.colonne)

        # Si la pièce n'est ni un pion ni une dame, elle ne peut pas se déplacer
        return False



    def piece_peut_sauter_vers(self, position_piece, position_cible):
        """Cette méthode détermine si une pièce (à la position reçue) peut sauter vers une certaine position cible.
        On parle ici d'un déplacement qui "mange" une pièce adverse.

        Une pièce doit être positionnée à la position_piece reçue en argument (retourner False autrement).

        Une pièce ne peut que sauter de deux cases en diagonale. N'importe quel type de pièce (pion ou dame) peut sauter
        vers l'avant ou vers l'arrière. Une pièce ne peut pas sauter vers une case qui est déjà occupée par une autre
        pièce. Une pièce ne peut faire un saut que si elle saute par dessus une pièce de couleur adverse.

        Args:
            position_piece (Position): La position de la pièce source du saut.
            position_cible (Position): La position cible du saut.

        Returns:
            bool: True si la pièce peut sauter vers la position cible, False autrement.

        """
        # TODO: À compléter

        piece = self.recuperer_piece_a_position(position_piece)

        if not piece:
            return False

        # Utiliser la méthode quatre_positions_diagonales pour obtenir les positions diagonales possibles
        positions_diagonales = position_piece.quatre_positions_diagonales()
        #if position_cible not in positions_diagonales:
            #return False


        # Vérifier si la pièce peut se déplacer vers au moins une des positions diagonales
        for pos in positions_diagonales:
            if self.position_est_dans_damier(pos):
                piece_sur_case = self.recuperer_piece_a_position(pos)
                if not piece_sur_case:
                    return True


        return False


    def piece_peut_se_deplacer(self, position_piece):
        """Vérifie si une pièce à une certaine position a la possibilité de se déplacer (sans faire de saut).

        ATTENTION: N'oubliez pas qu'étant donné une position, il existe une méthode dans la classe Position retournant
        les positions des quatre déplacements possibles.

        Args:
            position_piece (Position): La position source.

        Returns:
            bool: True si une pièce est à la position reçue et celle-ci peut se déplacer, False autrement.

        """
        # TODO: À compléter
        piece = self.recuperer_piece_a_position(position_piece)

        if not piece:
            return False

        # Vérifie si la pièce peut se déplacer vers au moins une des positions adjacentes
        return any(self.piece_peut_se_deplacer_vers(position_piece, pos) for pos in position_piece.quatre_positions_diagonales())




    def piece_peut_faire_une_prise(self, position_piece):



        """Vérifie si une pièce à une certaine position a la possibilité de faire une prise.

        Warning:
            N'oubliez pas qu'étant donné une position, il existe une méthode dans la classe Position retournant
            les positions des quatre sauts possibles.

        Args:
            position_piece (Position): La position source.

        Returns:
            bool: True si une pièce est à la position reçue et celle-ci peut faire une prise. False autrement.

        """
        # TODO: À compléter
        piece = self.recuperer_piece_a_position(position_piece)

        if not piece or not self.position_est_dans_damier(position_piece):
            return False

        sauts_possibles = position_piece.quatre_positions_sauts()

        return any(self.piece_peut_sauter_vers(position_piece, saut) for saut in sauts_possibles)


    def piece_de_couleur_peut_se_deplacer(self, couleur):
        """Vérifie si n'importe quelle pièce d'une certaine couleur reçue en argument a la possibilité de se déplacer
        vers une case adjacente (sans saut).

        ATTENTION: Réutilisez les méthodes déjà programmées!

        Args:
            couleur (str): La couleur à vérifier.

        Returns:
            bool: True si une pièce de la couleur reçue peut faire un déplacement standard, False autrement.
        """
        # TODO: À compléter
        for position, piece in self.cases.items():
             if piece.couleur == couleur and self.piece_peut_se_deplacer(position):
                  return True

        return False

        #return any(self.piece_peut_se_deplacer(position) for position, piece in self.cases.items() if piece.couleur == couleur)

    def piece_de_couleur_peut_faire_une_prise(self, couleur):
        """Vérifie si n'importe quelle pièce d'une certaine couleur reçue en argument a la possibilité de faire un
        saut, c'est à dire vérifie s'il existe une pièce d'une certaine couleur qui a la possibilité de prendre une
        pièce adverse.


        ATTENTION: Réutilisez les méthodes déjà programmées!

        Args:
            couleur (str): La couleur à vérifier.

        Returns:
            bool: True si une pièce de la couleur reçue peut faire un saut (une prise), False autrement.
        """
        # TODO: À compléter
        #return any(self.piece_peut_faire_une_prise(position) for position, piece in self.cases.items() if piece.couleur == couleur)
        for position, piece in self.cases.items():
            if piece.couleur == couleur and self.piece_peut_faire_une_prise(position):
                 return True
        return False

    def deplacer(self, position_source, position_cible):
        """Effectue le déplacement sur le damier. Si le déplacement est valide, on doit mettre à jour le dictionnaire
        self.cases, en déplaçant la pièce à sa nouvelle position (et possiblement en supprimant une pièce adverse qui a
        été prise).

        Cette méthode doit également:
        - Promouvoir un pion en dame si celui-ci atteint l'autre extrémité du plateau.
        - Retourner un message indiquant "ok", "prise" ou "erreur".

        ATTENTION: Si le déplacement est effectué, cette méthode doit retourner "ok" si aucune prise n'a été faite,
            et "prise" si une pièce a été prise.
        ATTENTION: Ne dupliquez pas de code! Vous avez déjà programmé (ou allez programmer) des méthodes permettant
            de valider si une pièce peut se déplacer vers un certain endroit ou non.

        Args:
            position_source (Position): La position source du déplacement.
            position_cible (Position): La position cible du déplacement.

        Returns:
            str: "ok" si le déplacement a été effectué sans prise, "prise" si une pièce adverse a été prise, et
                "erreur" autrement.
        """
        # TODO: À compléter

        if not self.position_est_dans_damier(position_source) or not self.position_est_dans_damier(position_cible):
            return "erreur"
        piece_source = self.recuperer_piece_a_position(position_source)
        piece_cible = self.recuperer_piece_a_position(position_cible)

        if piece_source is None :
            return "erreur"

        # Vérifier si le déplacement est valide (standard ou prise)
        if self.piece_peut_se_deplacer_vers(position_source, position_cible):

            if self.cases[position_source].couleur=="noir":
                piece_changer=Piece("noir", "pion")
            else:
                piece_changer=Piece("blanc", "pion")
            del self.cases[position_source]
            self.cases[position_cible]=piece_changer



         #Verifier si c<est une prise


            # Promouvoir un pion en dame si nécessaire
            if position_cible.ligne == 0 and self.cases[position_cible].type == "pion":
                self.cases[position_cible] = Piece(self.cases[position_cible].couleur, "dame")

            else:
                return "ok"
        if self.piece_peut_faire_une_prise(position_source):

                if abs(position_cible.ligne-position_source.ligne)==2:
                    if piece_cible is not None:
                        return "erreur"
                    else:
                        if self.cases[position_source].couleur=="noir":
                               piece_changer=Piece("noir", "pion")
                        else:
                                piece_changer=Piece("blanc", "pion")
                        del self.cases[position_source]
                        self.cases[position_cible]=piece_changer
                        #if position_cible.colonne<position_source.colonne:
                        piece_prise_position=Position(abs(max(position_cible.ligne,position_source.ligne)-1),abs(max(position_source.colonne,position_cible.colonne)-1))
                       # else:
                        #    piece_prise_position=Position(abs(position_cible.ligne-1),abs(position_source.colonne+1))

                        del self.cases[piece_prise_position]

                        return "prise"

        return "erreur"



    def __repr__(self):
        """Cette méthode spéciale permet de modifier le comportement d'une instance de la classe Damier pour
        l'affichage. Faire un print(un_damier) affichera le damier à l'écran.

        """
        s = " +-0-+-1-+-2-+-3-+-4-+-5-+-6-+-7-+\n"
        for i in range(0, 8):
            s += str(i)+"| "
            for j in range(0, 8):
                if Position(i, j) in self.cases:
                    s += str(self.cases[Position(i, j)])+" | "
                else:
                    s += "  | "
            s += "\n +---+---+---+---+---+---+---+---+\n"


           # print("\n")
           # print(self.cases)

        return s


if __name__ == "__main__":
    print('Test unitaires de la classe "Damier"...')

    un_damier = Damier()

    # TODO: À compléter


    assert un_damier.position_est_dans_damier(Position(0, 0)) is True  # Position dans le coin supérieur gauche
    assert un_damier.position_est_dans_damier(Position(7, 7)) is True  # Position dans le coin inférieur droit
    assert un_damier.position_est_dans_damier(Position(8, 0)) is False  # Position en dehors du damier (ligne trop grande)
    assert un_damier.position_est_dans_damier(Position(0, 8)) is False  # Position en dehors du damier (colonne trop grande)
    assert un_damier.position_est_dans_damier(Position(-1, 0)) is False  # Position en dehors du damier (ligne trop petite)
    assert un_damier.position_est_dans_damier(Position(0, -1)) is False  # Position en dehors du damier (colonne trop petite)

    # Test de piece_peut_se_deplacer_vers

    assert un_damier.piece_peut_se_deplacer_vers(Position(5, 0), Position(4, 1)) is True  # Déplacement diagonal vers le haut
    assert un_damier.piece_peut_se_deplacer_vers(Position(0, 1), Position(1, 0)) is False  # Déplacement diagonal vers le haut


    assert un_damier.piece_peut_se_deplacer(Position(5, 0)) is True  # La pièce à cette position peut se déplacer vers au moins une case adjacente
    assert un_damier.piece_peut_se_deplacer(Position(5, 2)) is True  # La pièce à cette position ne peut pas se déplacer (bord du damier)44

    assert un_damier.piece_peut_faire_une_prise(Position(5, 2)) is True
    assert un_damier.piece_peut_faire_une_prise(Position(2, 3)) is True
    assert un_damier.piece_peut_faire_une_prise(Position(0, 1)) is False



    assert un_damier.piece_de_couleur_peut_se_deplacer("blanc") is True  # Au moins une pièce blanche peut se déplacer
    assert un_damier.piece_de_couleur_peut_se_deplacer("noir") is True  # Au moins une pièce noire peut se déplacer


    assert un_damier.piece_de_couleur_peut_faire_une_prise("blanc") is True  # Une pièce blanche peut faire une prise
    assert un_damier.piece_de_couleur_peut_faire_une_prise("noir") is True  # Une pièce noire peut faire une prise

    # Modifier le damier pour qu'aucune pièce noire ne puisse se déplacer

    assert un_damier.deplacer(Position(5, 0), Position(4, 1)) == "ok"  # Déplacement diagonal vers le haut sans prise
    assert un_damier.deplacer(Position(2, 1), Position(3, 0)) == "ok"
    assert un_damier.deplacer(Position(4, 1), Position(3, 2)) == "ok"
    assert un_damier.deplacer(Position(3, 0), Position(4, 1)) == "ok"
    assert un_damier.deplacer(Position(5, 2), Position(3, 0)) == "prise"
    assert un_damier.deplacer(Position(2, 3), Position(4, 1)) == "prise"# Prise d'une pièce adverse
    assert un_damier.deplacer(Position(3, 0), Position(8, 0)) == "erreur"
    assert un_damier.deplacer(Position(3, 0), Position(4, 1)) == "erreur"
    assert un_damier.deplacer(Position(0, 1), Position(1, 1)) == "erreur"






    print('Test unitaires passés avec succès!')

    # NOTEZ BIEN: Pour vous aider lors du développement, affichez le damier!
    print(un_damier)
