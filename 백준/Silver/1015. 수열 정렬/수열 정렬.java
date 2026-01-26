import java.util.*;

public class Main {

    static class Node {
        int value;
        int index;

        Node(int value, int index) {
            this.value = value;
            this.index = index;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        Node[] arr = new Node[N];

        for (int i = 0; i < N; i++) {
            arr[i] = new Node(sc.nextInt(), i);
        }

        Arrays.sort(arr, new Comparator<Node>() {
            @Override
            public int compare(Node a, Node b) {
                return a.value - b.value;
            }
        });

        int[] P = new int[N];

        for (int i = 0; i < N; i++) {
            P[arr[i].index] = i;
        }

        for (int i = 0; i < N; i++) {
            System.out.print(P[i] + " ");
        }

        sc.close();
    }
}
