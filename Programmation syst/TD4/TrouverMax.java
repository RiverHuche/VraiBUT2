import java.util.List;
import java.util.concurrent.RecursiveTask;

public class TrouverMax extends RecursiveTask <Integer>{

    private int debut,fin;

    private List<Integer> liste;
    
    public TrouverMax(int debut, int fin, List<Integer> liste){
        this.debut = debut;
        this.fin = fin;
        this.liste = liste;
    }


    @Override
    protected Integer compute() {
        int taille = this.fin - this.debut;
        int max = -1;
        if(taille < 100){
            for(int i = this.debut; i< this.fin; i++){
               if(this.liste.get(i) > max){
                    max = this.liste.get(i);
               }
            }
        }
        else{
            int moitier =this.debut + taille/2;
            TrouverMax max1 = new TrouverMax(debut, moitier,this.liste);
            max1.fork(); /* créer une nouvelle tâche et la fournie au pool. */
            TrouverMax max2 = new TrouverMax(moitier, fin,this.liste);

            int resultatMax2 = max2.compute(); /*  */
            int resultatMax1 = max1.join();
            return Math.max(resultatMax1, resultatMax2);
        }
        return max;
    }
    
}