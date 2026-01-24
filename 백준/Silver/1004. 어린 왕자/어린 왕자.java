import java.util.*;

public class Main {
    static boolean inside(int x, int y, int cx, int cy, int r) {
        long dx = x - cx;
        long dy = y - cy;
        return dx*dx + dy*dy < 1L*r*r; // "내부"만 (경계는 포함X)
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int sx = sc.nextInt();
            int sy = sc.nextInt();
            int ex = sc.nextInt();
            int ey = sc.nextInt();

            int n = sc.nextInt();
            int ans = 0;

            for (int j = 0; j < n; j++) {
                int cx = sc.nextInt();
                int cy = sc.nextInt();
                int r  = sc.nextInt();

                boolean sIn = inside(sx, sy, cx, cy, r);
                boolean eIn = inside(ex, ey, cx, cy, r);

                if (sIn ^ eIn) ans++; 
            }

            System.out.println(ans);
        }
    }
}
