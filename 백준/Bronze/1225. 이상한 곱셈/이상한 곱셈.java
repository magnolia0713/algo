import java.util.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b = sc.next();
        long c = 0, d = 0;
        for (int i = 0; i < a.length(); i++) {
            c += a.charAt(i) - '0';            
        }
        for (int i = 0; i < b.length(); i++) {
            d += b.charAt(i) - '0';            
        }
        System.out.println(c * d);
    }
}