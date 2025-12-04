public class Executable {
    public static void main(String []args){
        Matrice mat1 = new Matrice(1000, 4);
        Matrice mat2 = new Matrice(1000,3);

        long deb2 = System.currentTimeMillis();
        Matrice lol = mat1.MatriceMultiplier(mat2);
        long fin2 = System.currentTimeMillis();

        long deb1 = System.currentTimeMillis();
        Matrice lol2 = mat1.MatriceMultiplierThreads(mat2);
        long fin1 = System.currentTimeMillis();

        long t1 = fin1 - deb1;
        long t2 = fin2 - deb2;
        System.out.println("Sequence :" + t2 + "ms");
        System.out.println("Thread :" + t1 + "ms");

    }
    
}
