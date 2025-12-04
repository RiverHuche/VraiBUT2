import java.util.ArrayList;
import java.util.List;

class Carte {

  final int SEUIL_ENFLAMMATION = 6;
  final int INTENSITE_MAX = 3;
  final int INTENSITE_CENDRES = 4;
  //carte representant l'état de la zone à instant T
  public List<List<Integer>> carte;

  //carte representant l'état de la zone à instant T+1
  private List<List<Integer>> carteT1;

  //Indicateur d'un changement dans la carte, si la carte à l'instant T est identique à l'intant T+1, l'incendie ne se propage plus
  private boolean hasChanged = true;

  private void initCarte(List<List<Integer>> map, int length, int width) {
    for (int i = 0; i < length; i++) {
      List<Integer> ligne = new ArrayList<>();
      for (int j = 0; j < width; j++) {
        ligne.add(0);
      }
      map.add(ligne);
    }
  }

  public Carte(int length, int width) {
    this.carte = new ArrayList<>();
    this.carteT1 = new ArrayList<>();
    initCarte(this.carte, length, width);
    initCarte(this.carteT1, length, width);

    //initialisation de l'incendie
    this.initFeu(length / 2, width / 2, 1);
    this.initFeu(length / 2, (width / 2) - 1, 1);
    this.initFeu((length / 2) - 1, width / 2, 1);
    this.initFeu((length / 2) - 1, (width / 2) - 1, 1);
  }


  private void initFeu(int x, int y, int intensity) {
    this.carte.get(x).set(y, intensity);
  }

  private int getSommeVoisins(int i, int j) {
    int somme = 0;
    for (int k = i - 1; k <= i + 1; k++) {
      // Vérifier les limites de la ligne
      if (k >= 0 && k < this.carte.size()) {
        for (int l = j - 1; l <= j + 1; l++) {
          // Vérifier les limites de la colonne et ne pas se compter soi-même
          if (l >= 0 && l < this.carte.get(k).size() && !(k == i && l == j)) {
            int voisin = this.carte.get(k).get(l);
            if (voisin < INTENSITE_CENDRES) {
              somme += voisin;
            }
          }
        }
      }
    }
    return somme;
  }

  /**
       Calcul de la valeur de la case i,j au prochain tour à partir de la carte 'carte', et écriture dans la case i,j de la carte 'carteT1'   
     **/
  public void propagationCase(int i, int j) {
    int valeurActuelle = this.carte.get(i).get(j);

    //augmentation des flames
    if (valeurActuelle > 0 && valeurActuelle <= INTENSITE_MAX) {
      this.carteT1.get(i).set(j, this.carte.get(i).get(j) + 1);
      this.setChanged(true);
    } else if (valeurActuelle == 0) { // La case est intacte
      int sommeVoisins = getSommeVoisins(i, j);
      // voisins suffisamment enflammes, la case s'enflamme
      if (sommeVoisins >= SEUIL_ENFLAMMATION) {
        this.carteT1.get(i).set(j, 1);
        this.setChanged(true);
      } else { // La case reste intacte
        this.carteT1.get(i).set(j, valeurActuelle);
      }
    } else { // La case est en cendres ou autre, elle ne change pas
      this.carteT1.get(i).set(j, valeurActuelle);
    }
  }

  public void display() {
    for (int i = 0; i < carte.size(); i++) {
      for (int j = 0; j < carte.get(0).size(); j++)
        System.out.print(carte.get(i).get(j) + " ");
      System.out.println();
    }
    System.out.println();
  }

  public  boolean hasChanged() {
    return hasChanged;
  }

  public  void setChanged(boolean changed) {
    hasChanged = changed;
  }

  /**
       Echange des deux cartes, la carte actuelle pointe vers la carte de l'instant T+1
       La carte T+1 pointe vers l'ancienne carte pour éviter d'allouer de la mémoire
     **/
  public void switchCarte() {
    List<List<Integer>> carteAux = carte;
    carte = carteT1; // la nouvelle matrice prend la place de l'ancienne
    carteT1 = carteAux;
  }

  public void incendie() {
    do {

      this.setChanged(false);
      //Calcul de la propagation dans la zone
      for (int i = 0; i < carte.size(); i++) {
        for (int j = 0; j < carte.get(0).size(); j++) {
          this.propagationCase(i, j);
        }
      }
      this.display();
      this.switchCarte();
      try {
        Thread.sleep(1000);
      } catch (Exception e) {
        e.printStackTrace();
      }
    } while (this.hasChanged());
  }

  public void incendieParallele(){
      int n = carte.size();
			List<Calcul> listThreads = new ArrayList<>();
			int nbThreads = Runtime.getRuntime().availableProcessors();
			int nbLignesParThread = n / nbThreads;

			int debut, fin = 0;
			for (int i = 0; i < nbThreads; i++) {
				debut = i * nbLignesParThread;
				fin = (i + 1) * nbLignesParThread;
				if (i == nbThreads - 1)
					fin = n;
				Calcul cal = new Calcul(this,debut, fin);
				listThreads.add(cal);
				cal.start();
			}
      for (Calcul cal : listThreads) {
				try {
					cal.join();
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
  }

  public static void main(String args[]) {
    if (args.length != 1) {
      System.out.println("Usage: java Carte <size>");
      return;
    }
    try {
      int size = Integer.parseInt(args[0]);
      if (size <= 0) {
        System.out.println("Error: size must be a positive integer.");
        return;
      }
      Carte zone = new Carte(size, size);
      zone.incendie();
    } catch (NumberFormatException e) {
      System.out.println("Error: <size> must be an integer.");
    }
  }
}
