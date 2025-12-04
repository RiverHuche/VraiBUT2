#!/usr/bin/env python3

class Arbre:
    def __init__(self, etiquette, enfants):
        self.__etiquette = etiquette
        self.__enfants = enfants

    def etiquette(self):
        return self.__etiquette

    def enfants(self):
        return self.__enfants
    
    def nbEnfants(self):
        return len(self.__enfants)
    
    def nbFeuilles(self):
        if self.nbEnfants() == 0:
            return 1 
        total_feuilles = 0
        for enfant in self.enfants():
            total_feuilles += enfant.nbFeuilles()
        return total_feuilles

    def nbNoeudsInternes(self):
        nbNoeudsInt = 0
        if self.nbEnfants() >= 1:
            nbNoeudsInt +=1
        for e in self.enfants():
            nbNoeudsInt += e.nbNoeudsInternes()
        return nbNoeudsInt
    
    def hauteur(self):
        if self.nbEnfants() == 0:
            return 0
        hauteur = 0
        for e in self.enfants():
            hauteur +=max(hauteur,e.hauteur())
        return hauteur + 1
    
    def degre(self):
        if self.enfants() == []:
            return 0
        d = len(self.enfants())
        for e in self.enfants():
            d2 = e.degre()
            if d2>d :
                d = d2
        return d 
    
    def q8(self):
        if self.enfants() == []:
            return type(self.etiquette()) == int
        else:
            return(self.etiquette() == "*" or self.etiquette() == "+" and len(self.enfants()) ==2 and self.enfants()[0].verif() and self.enfants()[1].verif()) 


    def q9(self):
        if self.enfants() ==[]:
            return int(self.etiquette())
        elif self.etiquette() == '*':
            return self.enfants()[0].q9() * self.enfants()[1].q9()
        else:
            return self.enfants()[0].q9() + self.enfants()[1].q9()

    @classmethod
    def Feuille(cls_arbre, etiquette): #méthode statique
        return cls_arbre(etiquette, [])

    def add(self, nourisson):
        """
        ajoute un enfant à l'arbre
        """
        self.__enfants.append(nourisson)

    def __repr__(self):
        repr_enfants = ",".join(("%r" % e) for e in self.enfants())
        return "%r<%s>" % (self.etiquette(), repr_enfants)
    
    def trouver0(a):
        if a.etiquette == 0 :
            return []
        if a.enfants().etiquette() == 0:
            return a.etiquette()
        else :
            return 


def heritier(pers, date):
    for personne in pers.enfants():
        if personne


a1 = Arbre("a1",[])
e = Arbre("e",[])
e1 = Arbre("e",[])
e2 = Arbre("e",[])
a2 = Arbre("a2",[e,e1,e2])

q8 = Arbre("*",[])
q80 = Arbre("+",[])
q81 = Arbre("*",[])

qf = Arbre.Feuille("2")
qf1 = Arbre.Feuille("3")
qf2 = Arbre.Feuille("1")
qf3 = Arbre.Feuille("4")

q8.add(q80)
q8.add(q81)
q80.add(qf)
q80.add(qf1)
q81.add(qf2)
q81.add(qf3)



f = Arbre.Feuille("feuille1")
f2 = Arbre.Feuille("feuille2")
f3 = Arbre.Feuille("feuille3")
f4 = Arbre.Feuille("feuille4")
f5 = Arbre.Feuille("feuille5")

a2.add(f2)
a2.add(f3)
a2.add(f4)
a2.add(f5)
print(q8)
print(q8.q8())
print((q8.q9()))



