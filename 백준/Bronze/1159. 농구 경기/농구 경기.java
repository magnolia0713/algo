import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();           // 사람 수
        int[] spellDict = new int[26];  // a~z 카운트

        for (int i = 0; i < n; i++) {
            String name = sc.next();    // 이름(공백 없음)
            int idx = name.charAt(0) - 'a';
            spellDict[idx]++;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 26; i++) {
            if (spellDict[i] >= 5) {
                sb.append((char) ('a' + i));
            }
        }

        if (sb.length() == 0) {
            System.out.print("PREDAJA");
        } else {
            System.out.print(sb.toString());
        }

        sc.close();
    }
}
