import sys
import json
import commune
import math

class Departement:
    def __init__(self, nom, communes):
        self._nom = nom
        self._communes = communes

    def communes(self):
        return self._communes

    def population(self):
        total = 0
        for c in self.communes():
            total += c.population()
        return total

    def superficie(self):
        total = 0
        for c in self.communes():
            total += c.superficie()
        return total

    def nom(self):
        return self._nom

    def plusGrdCommune(self): # question 25
        pop_max = -math.inf # moins l'infini
        nom = None
        for c in self.communes():
            pop = c.population()
            if pop > pop_max:
                nom = c.nom()
                pop_max = pop
        return nom

    def liste_noms_communes(self):
        liste = []
        for c in self.communes():
            liste.append(c.nom())
        return liste
    
    def medecins_par_10_000_hab(self):
        total_m = 0
        for c in self.communes():
            m = c.medecins_par_10_000_hab() * (c.population() / 10000)
            total_m += m
        pop = self.population()
        if pop == 0:
            return 0
        else:
            return 10000 * total_m / self.population()

    def as_dict(self):
        dictionnaires_communes = []
        for c in self.communes():
            dict_c = c.as_dict()
            dictionnaires_communes.append(dict_c)
        return { "nom": self.nom,
                 "communes": dict_c
        }

def dict_vers_departement(d):
    dictionnaires_communes = d["communes"]
    communes = []
    for dico_commune in dictionnaires_communes:
        c = commune.dict_vers_commune(dico_commune)
        communes.append(c)
    return Departement(d["nom"], communes)

class Region:
    def __init__(self, nom, departements):
        self._nom = nom
        self._departements = departements

    def departements(self):
        return self._departements

    def population(self):
        total = 0
        for d in self.departements():
            total += d.population()
        return total
    
    def liste_nom_departements(self):
        liste = []
        for d in self.departements():
            liste.append(d.nom())
        return liste

    def superficie(self):
        total = 0
        for d in self.departements():
            total += d.superficie()
        return total

    def liste_noms_communes_r(self):
        nom = []
        for d in self.departements():
            liste = d.liste_noms_communes()
            for communes in liste:
                nom.append(communes)
        return nom

    def nom(self):
        return self._nom

    def medecins_par_10_000_hab(self):
        med = 0
        for d in self.departements():
            m = d.medecins_par_10_000_hab() * (d.population() / 10000)
            med += m
        pop = self.population()
        if pop == 0:
            return 0
        else:
            return 10000*med/self.population()
        
    def nombre_communes(self):
        nb = 0
        for d in self.departements():
            for c in d.communes():
                nb += 1
        return nb
        
    def nbHabitantsMcarré(self): # question 26
        return self.population() / self.superficie()

    def as_dict(self):
        dictionnaires_departements = []
        for d in self.departements():
            dict_d = d.as_dict()
            dictionnaires_departements.append(dict_d)
        return { "nom": self.nom,
                 "departements": dict_d
        }

def dict_vers_region(d):
    dictionnaires_departements = d["departements"]
    departements = []
    for dico_departement in dictionnaires_departements:
        dep = dict_vers_departement(dico_departement)
        departements.append(dep)
    return Region(d["nom"], departements)

    
    
class Pays:
    def __init__(self, nom, regions):
        self._nom = nom
        self._regions = regions

    def regions(self):
        return self._regions

    def nom(self):
        return self._nom

    def population(self):
        pop = 0
        for r in self.regions():
            pop += r.population()
        return pop

    def nombre_communes(self):
        nb = 0
        for r in self.regions():
            nb += r.nombre_communes()
        return nb

    def liste_nom_regions(self):
        liste = []
        for r in self.regions():
            liste.append(r.nom())
        return liste
        
    def superficie(self):
        total = 0
        for r in self.regions():
            total += r.superficie()
        return total
    
    def liste_noms_communes_p(self):
        nom = []
        for r in self.regions():
            liste = r.liste_noms_communes_r()
            for communes in liste:
                nom.append(communes)
        return nom
    
    def liste_noms_departements(self):
        nom=[]
        for r in self.regions():
            liste = r.liste_nom_departements()
            for departement in liste:
                nom.append(departement)
        return nom

    def medecins_par_10_000_hab(self):
        total_m = 0
        for r in self.regions():
            m = r.medecins_par_10_000_hab() * (r.population() / 10000)
            total_m += m
        pop = self.population()
        if pop == 0:
            return 0
        else:
            return 10000 * total_m / self.population()

    def as_dict(self):
        dictionnaires_regions = []
        for r in self.regions():
            dict_r = r.as_dict()
            dictionnaires_regions.append(dict_r)
        return { "nom": self.nom,
                 "regions": dict_r
        }

def dict_vers_pays(d):
    dictionnaires_regions = d["regions"]
    regions = []
    for dico_region in dictionnaires_regions:
        reg = dict_vers_region(dico_region)
        regions.append(reg)
    return Pays(d["nom"], regions)


                
def main(nom_fichier_json):
    with open(nom_fichier_json) as j:
        dictionnaires_pays = json.load(j)
        pays = []
        for d in dictionnaires_pays:
            p = dict_vers_pays(d)
            pays.append(p)

        for p in pays:
            print("Bienvenue en", p.nom())
            print("Il y a", p.population(), "habitants.")
            print("La superficie est de", p.superficie(), "km².")
            print("Il y a", p.medecins_par_10_000_hab(), "médecins pour 10_000 hab.")
            # print("Ce pays est composé de", p.nombre_communes(), "communes")
            print(p.liste_nom_regions())
            print(p.liste_noms_communes_p())
            print(p.liste_noms_departements())
            print(p.nombre_communes())
            print("")

            
if __name__ == "__main__":
    nom_fichier_json = sys.argv[1]
    main(nom_fichier_json)
