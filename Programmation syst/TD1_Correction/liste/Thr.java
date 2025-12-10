public class Thr extends Thread {
    // Chaque thread calcule une case de la matrice resultat

    int i, j;
    Matrice m1, m2, res;

    public Thr(Matrice m1, Matrice m2, Matrice res, int i, int j) {
        this.i = i;
        this.j = j;
        this.m1 = m1;
        this.m2 = m2;
        this.res = res;
    }

    @Override
    public void run() {
        int n = m1.size();
        int val =0;
        for (int k = 0; k < n; k++)
            val += m1.get(i, k) * m2.get(k,j);
        res.set(i,j,val);
    }
}
