import java.util.Scanner;

public class MedianUnion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);


        int N = scanner.nextInt();
        int L = scanner.nextInt();


        int[][] sequences = new int[N][L];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < L; j++) {
                sequences[i][j] = scanner.nextInt();
            }
        }


        for (int i = 0; i < N - 1; i++) {
            for (int j = i + 1; j < N; j++) {
                int[] merged = merge(sequences[i], sequences[j]);
                System.out.println(merged[L - 1]); 
            }
        }

        scanner.close();
    }


    private static int[] merge(int[] a, int[] b) {
        int[] merged = new int[a.length + b.length];
        int i = 0, j = 0, k = 0;

        while (i < a.length && j < b.length) {
            if (a[i] <= b[j]) {
                merged[k++] = a[i++];
            } else {
                merged[k++] = b[j++];
            }
        }


        while (i < a.length) {
            merged[k++] = a[i++];
        }
        while (j < b.length) {
            merged[k++] = b[j++];
        }

        return merged;
    }
}
