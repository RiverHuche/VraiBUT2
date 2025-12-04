import java.util.List;
import java.util.ArrayList;
import java.util.Random;

class Matrice {
	List<List<Integer>> mat;

	public Matrice(int n) {
		mat = new ArrayList<>();
		for(int i=0;i<n;i++){
			mat.add(new ArrayList<>());
			for (int j=0;j<n;j++)
				mat.get(i).add(0);
		}
	}

	public Matrice(int n, int max) {
		Random random = new Random();
		mat = new ArrayList<>();
		for(int i=0;i<n;i++){
			mat.add(new ArrayList<>());
			for (int j=0;j<n;j++)
				mat.get(i).add(random.nextInt(max));
		}
	}

	public int size(){
		return this.mat.size();
	}

	public int get(int i, int j){
		return this.mat.get(i).get(j);
	}

	public void set(int i, int j, int val){
		this.mat.get(i).set(j,val);
	}

	/**
	 * Version séquentielle
	 */
	public Matrice multiplicationSeq(Matrice matrice) {
		if (matrice.size()==this.size()){
			int n= matrice.size();
			Matrice res = new Matrice(n);
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++){
					int val=0;
					for (int k = 0; k < n; k++)
						val += this.get(i,k) * matrice.get(k,j);
					res.set(i,j,val);
				}
			return res;
		}
		throw new IllegalArgumentException("Matrice taille differente");
	}

	/**
	 * Version parallèle avec un thread par case, très lent
	 * @param matrice a multiplier (la taille doit etre identique à this)
	 * @return matrice resultat
	 */
	public Matrice multiplicationPar(Matrice matrice) {
		if (matrice.size()==this.size()){
			int n = this.size();
			Matrice res = new Matrice(n);
			List<Thr> listThreads = new ArrayList<>();
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++) {
					Thr thr = new Thr(this, matrice, res, i, j);
					listThreads.add(thr);
					thr.start();
				}

			for (Thr thr : listThreads) {
				try {
					thr.join();
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
			return res;	
		}
		throw new IllegalArgumentException("Matrice taille differente");

	}

	/**
	 * Version parallèle avec un thread par ligne. Plus rapide que la version sequentielle pour des matrices avec plusieurs centianes de lignes
	 * @param matrice a multiplier (la taille doit etre identique à this)
	 * @return matrice resultat
	 */
	public Matrice multiplicationParLigne(Matrice matrice) {
		if (matrice.size()==this.size()){

			int n = mat.size();
			Matrice res = new Matrice(n);
			List<ThrL> listThreads = new ArrayList<>();

			for (int i = 0; i < n; i++) {
				ThrL thrL = new ThrL(this, matrice, res, i);
				listThreads.add(thrL);
				thrL.start();
			}

			for (ThrL thrL : listThreads) {
				try {
					thrL.join();
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
			return res;
		}
		throw new IllegalArgumentException("Matrice taille differente");
	}

	/**
	 * Version parallèle avec autant de thread que d'unités de calcul présents sur la machine. Evite de créer trop de threads
	 * @param matrice
	 * @return
	 */
	public Matrice multiplicationParCoeur(Matrice matrice) {
		if (matrice.size()==this.size()){

			int n = this.size();
			Matrice res = new Matrice(n);
			List<ThrC> listThreads = new ArrayList<>();
			int nbThreads = Runtime.getRuntime().availableProcessors();
			int nbLignesParThread = n / nbThreads;

			int debut, fin = 0;
			for (int i = 0; i < nbThreads; i++) {
				debut = i * nbLignesParThread;
				fin = (i + 1) * nbLignesParThread;
				if (i == nbThreads - 1)
					fin = n;
				ThrC thrC = new ThrC(this, matrice, res, debut, fin);
				listThreads.add(thrC);
				thrC.start();
			}

			for (ThrC thrL : listThreads) {
				try {
					thrL.join();
				} catch (Exception e) {
					e.printStackTrace();
				}
			}

			return res;
		}
		throw new IllegalArgumentException("Matrice taille differente");


	}


	public String toString() {
		int n = this.size();
		String res = "";
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				res += this.get(i,j) + "\t";
			}
			res += "\n";
		}
		return res;
	}

	public static void main(String[] args) {

		if (args.length < 1) {
			System.out.println("java Matrice <tailleMatrice> <typeAlgo>");
			System.out.println("typeAlgo : seq | ligne | case | coeur (default)");
		} else {
			int taille = Integer.parseInt(args[0]);

			Matrice mat1 = new Matrice(taille,10);
			Matrice mat2 = new Matrice(taille,10);
			Matrice res;
			long l1 = System.currentTimeMillis();
			if (args.length == 1) {
				res = mat1.multiplicationParCoeur(mat2);
			} else {
				switch (args[1]) {
					case "seq":
						res= mat1.multiplicationSeq(mat2);
						break;
					case "ligne":
						res= mat1.multiplicationParLigne(mat2);
						break;
					case "case":
						res= mat1.multiplicationPar(mat2);
						break;
					case "coeur":
						res= mat1.multiplicationParCoeur(mat2);
						break;
					default:
						res= mat1.multiplicationParCoeur(mat2);
				}
			}
			long l2 = System.currentTimeMillis();

			// System.out.println(mat1);
			// System.out.println(mat2);
			// System.out.println(res);

			System.out.println(l2 - l1 + " ms");
		}
	}

}
