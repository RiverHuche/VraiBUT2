public class ThrC extends Thread {
    // Chaque thread calcule plusieurs lignes

    int debut, fin;
    Matrice m1, m2, res;

    public ThrC(Matrice m1, Matrice m2, Matrice res, int debut, int fin) {
        this.debut = debut;
        this.fin = fin;
        this.m1 = m1;
        this.m2 = m2;
        this.res = res;
    }

    public void run() {
        int n = this.m1.size();
        for (int i = debut; i < fin; i++)
            for (int j = 0; j < n; j++){
                int val = 0;
                for (int k = 0; k < n; k++)
                    val += this.m1.get(i,k) * this.m2.get(k,j);
                res.set(i, j, val);
            }

    }
}
