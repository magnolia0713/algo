import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] nList = new int[5];
        for (int i = 0; i <= 4; i++) {
        nList[i] = scanner.nextInt();
        }
        int n = 1;
        while (true) {
            n++;
            int cnt = 0;
            for (int i = 0; i <= 4; i++) {
                if (n % nList[i] == 0) {
                    cnt += 1;
                }
            }
            if (cnt >= 3) {
                System.out.println(n);
                break;
            }
        }
    }
}
