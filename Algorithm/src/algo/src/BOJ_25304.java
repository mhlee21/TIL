import java.util.Scanner;

public class BOJ_25304 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int total = sc.nextInt();
        int N = sc.nextInt();
        int total_cal = 0;
        for (int i = 0; i < N; i++) {
            int cost = sc.nextInt();
            int cnt = sc.nextInt();
            total_cal += (cost * cnt);
        }
        if (total - total_cal == 0) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
