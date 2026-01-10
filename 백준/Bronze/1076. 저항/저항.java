import java.util.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next(); 
        String b = sc.next(); 
        String c = sc.next();

        Map<String, Integer> color = new HashMap<>();
        
        color.put("black", 0);
        color.put("brown", 1);
        color.put("red", 2);
        color.put("orange", 3);
        color.put("yellow", 4);
        color.put("green", 5);
        color.put("blue", 6);
        color.put("violet", 7);
        color.put("grey", 8);
        color.put("white", 9);
        
        int first = color.get(a);
        int second = color.get(b);
        int mult = color.get(c);
        long ans = (first * 10 + second) * (long)Math.pow(10, mult);
        System.out.println(ans);
    }
}