import java.util.ArrayList;
import java.util.List;
import java.util.Random;


public class Threads extends Thread {
    Matrice m1;
    Matrice m2;
    Matrice res;
    int i;
    

    public Threads(Matrice m1,Matrice m2, Matrice res, int i){
        this.m1 = m1;
        this.m2 = m2;
        this.res=res;
        this.i=i;

    }

    public void run(){
        for (int j = 0 ; j < m1.taille ; j++){
                int somme = 0;
                for (int k =0 ; k < m1.taille ; k++){
                    somme += m1.matrice.get(i).get(k) * m2.matrice.get(k).get(j);
                    
                }
                res.matrice.get(i).add(somme);
        }
    }
}

    
    

