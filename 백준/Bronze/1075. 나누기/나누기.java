import java.util.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {

        
        Scanner sc = new Scanner(System.in);
        
        int target = sc.nextInt();
        int division = sc.nextInt();
        target = target - target % 100;
        int n = target % division;
        int ans;
            
        if (n == 0) {
            ans = 0;
        } else {
        ans = division - n;
        }
        
        String b;
        if (ans < 10) {
            b = "0" + ans;
        } else {
            b = String.valueOf(ans);
        }
        System.out.println(b);
    }
}