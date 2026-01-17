import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String oct = br.readLine().trim();

        if (oct.equals("0")) {
            System.out.println("0");
            return;
        }

        String[] bin3 = {
                "000", "001", "010", "011",
                "100", "101", "110", "111"
        };

        StringBuilder sb = new StringBuilder();

        int first = oct.charAt(0) - '0';
        String firstBin = Integer.toBinaryString(first);
        sb.append(firstBin);

        for (int i = 1; i < oct.length(); i++) {
            int d = oct.charAt(i) - '0';
            sb.append(bin3[d]);
        }

        System.out.println(sb.toString());
    }
}
