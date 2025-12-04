public class Donnee {
    private String data;
        //si data==null <=>vide


    public Donnee(String data){
        this.data=data;
    }
    
    public String getData(){

        return this.data;
    }

    public synchronized void ajouter(String nouvelleData){
        while (this.data != null){
            System.out.println("En attente de place");
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        data = nouvelleData;
        System.out.println("Fin de l'attente, ajout de ."+ nouvelleData);
        notify();
    }

     public synchronized String retirer(){
        while (this.data ==null){
            System.out.println("En attente d'objet");
            try {
                wait();
            }catch (InterruptedException e){
                e.printStackTrace();
            }
        }
        String tmp = data;
        data = null;
        System.out.println("Consommation de ."+tmp);
        notify();
        return tmp;
    }

}
