import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ForkJoinPool;

public class Tab {

    private List<Integer> liste;
    private int max;

    public Tab(int max){
        this.max = max;
        this.liste = new ArrayList<>();
        Random rand = new Random();
        for (int i=0; i< this.max; i++){
            this.liste.add(rand.nextInt(max));
        }
    }

    public void genererListe(int nbNombre, int max){
        Random rand = new Random();
        for (int i=0; i< nbNombre; i++){
            this.liste.add(rand.nextInt(max));
        }
    }

    public void updateMax(){
        ForkJoinPool pool = new ForkJoinPool();
        
    }

    public List<Integer> getListe(){
        return this.liste;
    }
    
}
