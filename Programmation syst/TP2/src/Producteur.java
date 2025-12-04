import java.util.ArrayList;
import java.util.List;
import java.util.Random;

class Producteur extends Thread{
    private Donnee donnee;
    private List<String> listeMot;

    public Producteur(Donnee donnee){
        this.donnee=donnee;
        this.listeMot = new ArrayList<>();
        this.listeMot.add("a");
        this.listeMot.add("b");
        this.listeMot.add("c");
        this.listeMot.add("d");
    }

    public void run(){
        Random random = new Random();
        for (int i = 0 ; i<10 ; i++){
            int aleatoire = random.nextInt(this.listeMot.size());
            this.donnee.ajouter(listeMot.get(aleatoire));
            try {
                Thread.sleep(aleatoire*1000+ 1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }
}