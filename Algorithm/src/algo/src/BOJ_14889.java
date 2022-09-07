import java.util.Scanner;

public class BOJ_14889 {
    static int N;
    static int[][] arr;
    static boolean[] visited;
    static int Min = Integer.MAX_VALUE;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        arr = new int[N][N];
        visited = new boolean[N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j<N; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        dfs(0,0);
        System.out.println(Min);
    }

    static void dfs (int idx, int dep) {
        if (Min == 0) {
            return;
        }
        if (dep == N / 2) {
            diff();
            return;
        }
        for (int i = idx; i < N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                dfs(i + 1, dep + 1);
                visited[i] = false;
            }
        }
    }

    static void diff() {
        int start_total = 0;
        int link_total = 0;
        for (int i=0; i<N-1; i++){
            for (int j=i+1; j<N; j++){
                if (visited[i] && visited[j]) {
                    start_total += arr[i][j];
                    start_total += arr[j][i];
                }
                if (!visited[i] && !visited[j]) {
                    link_total += arr[i][j];
                    link_total += arr[j][i];
                }
            }
        }
        int val = Math.abs(start_total - link_total);
        if (Min > val) {
            Min = val;
        }
    }
}
