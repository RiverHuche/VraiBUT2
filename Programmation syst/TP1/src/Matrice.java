import java.util.ArrayList;
import java.util.List;
import java.util.Random;


class Matrice {
    List<List<Integer>> matrice;
    int max;
    int taille;

    public Matrice(int taille, int max){
        this.taille = taille;
        this.max = max;
        this.matrice = new ArrayList<>();
        Random rdm = new Random();
        for (int i=0; i< taille; i++){
            List<Integer> element = new ArrayList<>();
            matrice.add(element);
            for(int j = 0; j< taille; j++){
                element.add(rdm.nextInt(max));
            }
            matrice.add(element);
        }
    }
    public Matrice(int taille){
        this.matrice = new ArrayList<>();
        Random rdm = new Random();
        for (int i=0; i< taille ; i++){
            List<Integer> element = new ArrayList<>();
            matrice.add(element);
            for(int j = 0; j< taille; j++){
                element.add(rdm.nextInt(5));
            }
            matrice.add(element);

        }
    }


    public Matrice MatriceMultiplier(Matrice m){
        Matrice res = new Matrice(this.taille);
        for (int i=0 ; i < this.taille ; i++){
            for (int j = 0 ; j < this.taille ; j++){
                int somme = 0;
                for (int k =0 ; k < this.taille ; k++){
                    somme += this.matrice.get(i).get(k) * m.matrice.get(k).get(j);
                    
                }
                res.matrice.get(i).add(somme);
            }
        }
        return res;
    }

    public Matrice MatriceMultiplierThreads(Matrice m){
        Matrice res = new Matrice(this.taille);
        List<Thread> listeThread = new ArrayList<>();
        for (int i=0 ; i < this.taille ; i++){
            Thread ligne = new Threads(this,m,res,i);
            ligne.start();
            listeThread.add(ligne);
            for (Thread t : listeThread){
                try  {
                    t.join();
                }
                catch (InterruptedException e){
                    e.printStackTrace();
                }
            }
        }
        return res;
    }

    @Override
    public String toString(){
        String res = "";
        for (List<Integer> ligne : this.matrice){
            res += "[";
            String res2 = "";
            for (Integer elem : ligne){
                res +=  res2 + elem  ;
                res2 = ",";
            }
            res += "]\n";
        }
        return res;
    }
}

