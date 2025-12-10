public class ThrL extends Thread {
    // chaque thread calcule une ligne
    int i;
    Matrice m1, m2, res;

    public ThrL(Matrice m1, Matrice m2, Matrice res, int i) {
        this.i = i;
        this.m1 = m1;
        this.m2 = m2;
        this.res = res;
    }

	@Override
	public void run() {
		int n = m1.size();
		for (int j = 0; j < n; j++){
			int val = 0;
			for (int k = 0; k < n; k++)
				val += m1.get(i,k) * m2.get(k,j);
			res.set(i,j,val);
		}
	}
}
