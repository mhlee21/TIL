package java_algo_eclipse;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_16928 {
	static int N, M;
	static int[] ladderAndSnake = new int[101];
	static int[] cnt = new int[101];
	static boolean[] visited = new boolean[101];
	
	static void bfs(int start) {
		// ť ����
		Queue<Integer> q = new LinkedList<Integer>();
		q.offer(start);
		//���۳�� �湮 ó��
		visited[start] = true;
		
		while(!q.isEmpty()) {
			int node = q.poll();
			if (node == 100) {
				System.out.println(cnt[node]);
				return;
			}
			for(int i=1; i<=6; i++) {
				int nextNode = node + i;
				if (nextNode > 100) continue;
				if (visited[nextNode]) continue;
				visited[nextNode] = true;
				
				if (ladderAndSnake[nextNode] != 0) {
					if(!visited[ladderAndSnake[nextNode]]) {
						q.offer(ladderAndSnake[nextNode]);
						visited[ladderAndSnake[nextNode]] = true;
						cnt[ladderAndSnake[nextNode]] = cnt[node] + 1;
					}
				} else {
					q.offer(nextNode);
					cnt[nextNode] = cnt[node] + 1;
				}
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		
		for(int i=0;i<N;i++) { //��ٸ� ����
			int x = sc.nextInt();
			int y = sc.nextInt();
			ladderAndSnake[x] = y;
		}
		
		for(int j=0; j<M; j++) { //���� ����
			int u = sc.nextInt();
			int v = sc.nextInt();
			ladderAndSnake[u] = v;
		}
		
		bfs(1);
	}
}
