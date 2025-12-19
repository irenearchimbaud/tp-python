from datetime import date

class Vehicule:
    def __init__(self, marque, modele, annee, kilometrage, disponible=True):
        # les attributs du vehiculze ci-dessous
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.disponible = disponible

    def __str__(self):
        # on affiche la marche le modele et l'année du vehicule
        return print("{self.marque} {self.modele} - {self.annee}")

    def __repr__(self):
        #on y affiche plus clairement avec ce a quoi representent les valeurs
        return print("Vehicule(marque={}, modele={}, annee={})".format(
            self.marque, self.modele, self.annee
        ))

    @property
    def age(self):
        # calcul de l age du vehicule
        return date.today().year - self.annee

    def louer(self):
        # vehicule loué (en false car du coup il est pas dispo)
        self.disponible = False

    def retourner(self, km_parcourus):
        # met a jour les kilometrages avec les km + les km parcourus quon entre en param, et passe disponible a oui 
        self.kilometrage += km_parcourus
        self.disponible = True


class VehiculeElectrique(Vehicule):
    def __init__(self, marque, modele, annee, kilometrage, autonomie_km, niveau_batterie):
        super().__init__(marque, modele, annee, kilometrage) #super car faut definir les attributd de la classe parent donc il herite de lui 
        self.autonomie_km = autonomie_km
        self.niveau_batterie = niveau_batterie

    def recharger(self):
        # on met la batterie a 100%
        self.niveau_batterie = 100

    def __str__(self): #on re definit str pour override l'original
        return print("{self.marque} {self.modele} - {self.autonomie_km} km, batterie {self.niveau_batterie}%")