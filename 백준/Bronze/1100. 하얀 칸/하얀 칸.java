import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char[][] board = new char[8][8];

        // 입력 받기
        for (int i = 0; i < 8; i++) {
            String line = sc.next();   // 공백 없는 문자열
            for (int j = 0; j < 8; j++) {
                board[i][j] = line.charAt(j);
            }
        }

        int count = 0;

        // 하얀 칸 위의 F 개수 세기
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if ((i + j) % 2 == 0 && board[i][j] == 'F') {
                    count++;
                }
            }
        }

        System.out.println(count);
    }
}
