import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Fournisseur extends Thread{
    
    public List<Composant> composants;

    public Fournisseur(List<Composant> composants){
        this.composants = new ArrayList<>();
    }

    public void run(){
        Random random = new Random();
        for (int i = 0 ; i<10 ; i++){
            int aleatoire = random.nextInt(this.composants.size());
            if (this.composants.get(aleatoire) != null){
                if (this.composants.get(aleatoire).getType()==Composant.Type.CARROSSERIE)
                    this.composants.get(aleatoire).ajouterCarosserie()
            }
            this.donnee.ajouter(listeMot.get(aleatoire));
            try {
                Thread.sleep(aleatoire*1000+ 1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }
    
}
