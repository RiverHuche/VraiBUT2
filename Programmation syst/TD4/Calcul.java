import java.util.concurrent.CyclicBarrier;

public class Calcul extends Thread {
    private Carte carte;
    private int deb;
    private int fin;
    private CyclicBarrier barriere;

    public Calcul(Carte carte,int deb, int fin){
        this.carte =carte;
        this.deb = deb;
        this.fin = fin;
        this.barriere = new CyclicBarrier(11);
    }

    public void run(){
        do {

      carte.setChanged(false);
      //Calcul de la propagation dans la zone
      for (int i = deb; i < fin; i++) {
        for (int j = 0; j < this.carte.carte.get(0).size(); j++) {
          carte.propagationCase(i, j);
        }
      } //barriere
      carte.display();
      carte.switchCarte();
      try {
        Thread.sleep(1000);
      } catch (Exception e) {
        e.printStackTrace();
      } //barriere
    } while (carte.hasChanged());
    }

    
    
}
