public class Executable {
    public static void main(String[] args) {
        Donnee donneePartagee = new Donnee("S");

        Producteur producteur = new Producteur(donneePartagee);
        Consommateur consommateur = new Consommateur(donneePartagee);

        producteur.start();
        consommateur.start();
    }
}
    

