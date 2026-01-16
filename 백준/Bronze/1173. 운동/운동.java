import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int m = sc.nextInt();
        int M = sc.nextInt();
        int T = sc.nextInt();
        int R = sc.nextInt();
        int ans;
        int i = 0;
        int temp = m;
        if (M - m < T) {
            ans = -1;
        } else {
            ans = 0;
            while (i < N) {
                ans++;
                if (temp + T <= M) {
                    i++;
                    temp += T;
                } else {
                    if (temp - R < m) {
                        temp = m;
                    } else {
                        temp -= R;
                    }
                }
            }
        }
        System.out.println(ans);
    }
}
