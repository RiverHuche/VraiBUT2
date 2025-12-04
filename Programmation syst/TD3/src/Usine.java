import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.locks.Lock;

public class Usine {
    private List<List<Composant>> stock;
    private Lock verrouMoteur;
    private Lock verrouCarrosserie;
    private Lock verrouRoue;

public Usine(){
    this.stock = new ArrayList<>();
}

public verrouMoteur ajouterMoteur(Composant newMoteur){
        while (this.stock.get(0).size() >= 5){
            System.out.println("En attente de place");
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        this.stock.get(0).add(newMoteur);
        System.out.println("Fin de l'attente, ajout de ."+ newMoteur);
        notify();
    }


public lock Composant retirerMoteur(){
        while (this.stock.get(0) ==null){
            System.out.println("En attente d'objet");
            try {
                wait();
            }catch (InterruptedException e){
                e.printStackTrace();
            }
        }
        Composant tmp = this.stock.get(0).get(-1);
        this.stock.get(0).remove(-1);
        System.out.println("Consommation de ."+tmp);
        notify();
        return tmp;
    }



public lock void ajouterCarosserie(Composant newCarosserie){
        while (this.stock.get(1).size() >= 3){
            System.out.println("En attente de place");
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        this.stock.get(1).add(newCarosserie);
        System.out.println("Fin de l'attente, ajout de ."+ newCarosserie);
        notify();
    }


public lock Composant retirerCarosserie(){
        while (this.stock.get(1) ==null){
            System.out.println("En attente d'objet");
            try {
                wait();
            }catch (InterruptedException e){
                e.printStackTrace();
            }
        }
        Composant tmp = this.stock.get(1).get(-1);
        this.stock.get(1).remove(-1);
        System.out.println("Consommation de ."+tmp);
        notify();
        return tmp;
    }



public lock void ajouterRoue(Composant newRoue){
        while (this.stock.get(2).size() >= 20){
            System.out.println("En attente de place");
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        this.stock.get(2).add(newRoue);
        System.out.println("Fin de l'attente, ajout de ."+ newRoue);
        notify();
    }


public lock Composant retirerRoue(){
        while (this.stock.get(2) ==null){
            System.out.println("En attente d'objet");
            try {
                wait();
            }catch (InterruptedException e){
                e.printStackTrace();
            }
        }
        Composant tmp = this.stock.get(2).get(-1);
        this.stock.get(2).remove(-1);
        System.out.println("Consommation de ."+tmp);
        notify();
        return tmp;
    }



    
}
