public class Composant {
    public enum Type {
        CARROSSERIE(5),
        MOTEUR(3),
        ROUE(20);

        private final int quantite;

        Type(int quantite) {
            this.quantite = quantite;
        }

        public int getQuantite() {
            return quantite;
        }
    }

    private Type type;
    private String nom;

    public Composant(Type type, String nom) {
        this.type = type;
        this.nom = nom;
    }

    public Type getType() {
        return type;
    }

    public String getNom() {
        return nom;
    }

    @Override
    public String toString() {
        return "Composant{" +
                "type=" + type +
                ", nom='" + nom + '\'' +
                '}';
    }


}




    

