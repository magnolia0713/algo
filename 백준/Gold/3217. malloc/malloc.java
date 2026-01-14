import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();
        int N = Integer.parseInt(br.readLine().trim());

        SegTree st = new SegTree(MAX);

        for (int i = 0; i < N; i++) {
            String line = br.readLine().trim();

            // 명령 판별(많이 쓰는 방식): line[4]가 '='면 malloc, line[4]가 '('면 free, line[5]가 '('면 print
            // (출처 예시에서도 이런 식으로 파싱) :contentReference[oaicite:5]{index=5}
            if (line.charAt(4) == '=') {
                int id = varId(line, 0);
                int size = parseSize(line);
                int pos = st.allocatePos(size);
                if (pos == 0) {
                    varStart[id] = 0;
                    varLen[id] = 0;
                } else {
                    st.update(pos, pos + size - 1, 0); // occupy
                    varStart[id] = pos;
                    varLen[id] = size;
                }
            } else if (line.charAt(4) == '(') { // free(var);
                int id = varId(line, 5);
                int s = varStart[id];
                int len = varLen[id];
                if (s != 0) {
                    st.update(s, s + len - 1, 1); // free
                    varStart[id] = 0;
                    varLen[id] = 0;
                }
            } else { // print(var);
                int id = varId(line, 6);
                out.append(varStart[id]).append('\n');
            }
        }

        System.out.print(out.toString());
    }
    static final int MAX = 100000;

    // var id: 0..26^4-1
    static final int VAR_MAX = 26 * 26 * 26 * 26;
    static int[] varStart = new int[VAR_MAX];
    static int[] varLen = new int[VAR_MAX];

    static class SegTree {
        int n;
        int[] pref, suf, best, lazy; // lazy: -1 none, 0 occupied, 1 free

        SegTree(int n) {
            this.n = n;
            int sz = 4 * n + 5;
            pref = new int[sz];
            suf  = new int[sz];
            best = new int[sz];
            lazy = new int[sz];
            Arrays.fill(lazy, -1);
            build(1, 1, n);
        }

        void build(int node, int l, int r) {
            int len = r - l + 1;
            pref[node] = suf[node] = best[node] = len; // initially all free
            if (l == r) return;
            int mid = (l + r) >>> 1;
            build(node << 1, l, mid);
            build(node << 1 | 1, mid + 1, r);
        }

        void apply(int node, int l, int r, int val) {
            int len = r - l + 1;
            if (val == 0) { // occupied
                pref[node] = suf[node] = best[node] = 0;
            } else { // free
                pref[node] = suf[node] = best[node] = len;
            }
            lazy[node] = val;
        }

        void push(int node, int l, int r) {
            if (lazy[node] == -1 || l == r) return;
            int mid = (l + r) >>> 1;
            apply(node << 1, l, mid, lazy[node]);
            apply(node << 1 | 1, mid + 1, r, lazy[node]);
            lazy[node] = -1;
        }

        void pull(int node, int l, int r) {
            int mid = (l + r) >>> 1;
            int lc = node << 1, rc = node << 1 | 1;

            int leftLen = mid - l + 1;
            int rightLen = r - mid;

            pref[node] = pref[lc];
            if (pref[lc] == leftLen) pref[node] = leftLen + pref[rc];

            suf[node] = suf[rc];
            if (suf[rc] == rightLen) suf[node] = rightLen + suf[lc];

            best[node] = Math.max(Math.max(best[lc], best[rc]), suf[lc] + pref[rc]);
        }

        // assign range [ql, qr] to val (0/1)
        void update(int ql, int qr, int val) {
            update(1, 1, n, ql, qr, val);
        }

        void update(int node, int l, int r, int ql, int qr, int val) {
            if (qr < l || r < ql) return;
            if (ql <= l && r <= qr) {
                apply(node, l, r, val);
                return;
            }
            push(node, l, r);
            int mid = (l + r) >>> 1;
            update(node << 1, l, mid, ql, qr, val);
            update(node << 1 | 1, mid + 1, r, ql, qr, val);
            pull(node, l, r);
        }

        // return leftmost start position where there are >=need consecutive free cells, or 0 if impossible
        int allocatePos(int need) {
            if (best[1] < need) return 0;
            return query(1, 1, n, need);
        }

        int query(int node, int l, int r, int need) {
            if (l == r) return l;
            push(node, l, r);
            int mid = (l + r) >>> 1;
            int lc = node << 1, rc = node << 1 | 1;

            if (best[lc] >= need) {
                return query(lc, l, mid, need);
            }
            if (suf[lc] + pref[rc] >= need) {
                // crossing the middle: start is mid - suf(left) + 1
                return mid - suf[lc] + 1;
            }
            return query(rc, mid + 1, r, need);
        }
    }

    static int varId(String s, int startIdx) {
        int a = s.charAt(startIdx) - 'a';
        int b = s.charAt(startIdx + 1) - 'a';
        int c = s.charAt(startIdx + 2) - 'a';
        int d = s.charAt(startIdx + 3) - 'a';
        return (((a * 26) + b) * 26 + c) * 26 + d;
    }

    static int parseSize(String s) {
        // for "xxxx=malloc(1234);", digits start at index 12
        int i = 12;
        int val = 0;
        while (i < s.length()) {
            char ch = s.charAt(i);
            if (ch == ')') break;
            val = val * 10 + (ch - '0');
            i++;
        }
        return val;
    }

}