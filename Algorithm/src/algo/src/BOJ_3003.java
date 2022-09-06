import java.util.Scanner;

public class BOJ_3003 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] origin = {1,1,2,2,2,8};
        int[] add = {0,0,0,0,0,0};
        for (int i=0; i<origin.length; i++) {
            int num = sc.nextInt();
            add[i] = origin[i] - num;
            System.out.printf("%d ",add[i]);
        }

    }
}