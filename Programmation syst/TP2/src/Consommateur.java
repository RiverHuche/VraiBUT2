public class Consommateur extends  Thread {
    private Donnee donnee;

    public Consommateur(Donnee donnee){
        this.donnee = donnee;
    }

    public void run(){
        for (int i = 0 ; i<10 ; i++){
            this.donnee.retirer();
            try {
                Thread.sleep(1000 + 1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }
    
}
