import java.util.Scanner;

public class Main {
    static int cnt;

    public static int recursion(String s, int l, int r) {
        cnt++;
        if (l >= r) return 1;
        if (s.charAt(l) != s.charAt(r)) return 0;
        return recursion(s, l + 1, r - 1);
    }

    public static int isPalindrome(String s) {
        cnt = 0;
        return recursion(s, 0, s.length() - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            String word = sc.next(); // nextLine() 말고 next() 사용
            int res = isPalindrome(word);
            System.out.println(res + " " + cnt);
        }
    }
}
