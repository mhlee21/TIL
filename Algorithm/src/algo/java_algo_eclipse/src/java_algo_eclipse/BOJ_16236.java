package java_algo_eclipse;
/*
 * https://www.acmicpc.net/problem/16236
 */

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ_16236 {
	static int N;
	static int[][] arr;
	static int[] di = {-1,0,0,1};
	static int[] dj = {0,-1,1,0};
	static Point cur;
	static int babyShark = 2;
	static int fishNum = 0;
	static int eatCnt = 0;
	static int time = 0;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		arr = new int[N][N];
		
		for(int i=0; i<N; i++) {
			for(int j=0; j<N; j++) {
				arr[i][j] = sc.nextInt();
				if (arr[i][j] == 9) { //�Ʊ� ����� ��ġ
					arr[i][j] = 0;
					cur = new Point(i,j,1);
				}
				if (arr[i][j] != 9 && arr[i][j] != 0) { // ����� �� ����
					fishNum += 1;
				}
			}
		}
		
		int tmp;
		while(fishNum!=0) { // ���� ����Ⱑ ���� �� ���� Ž��
			tmp = fishNum;
//			System.out.printf("%d %d %d[%d]\n", cur.i, cur.j, cur.time, fishNum);
			bfs(cur);
			if (tmp == fishNum) {
				// Ž�� �� �İ� ���� ��� ���� -> ���̻� ���� �� �ִ� ����Ⱑ ����
				break;
			}
		}
		
		System.out.println(time);
	}
	
	private static void bfs(Point cur) {
		boolean[][] visited = new boolean[N][N]; //�湮 ���� üũ
		Point next = new Point(-1,-1,Integer.MAX_VALUE); // ���� �Ա�� ������ ������� ��ǥ
		Queue<Point> q = new LinkedList<Point>();
		q.add(cur);
		visited[cur.i][cur.j] = true;
		
		/*
		 * �Ʊ���� �ڽ��� ũ�⺸�� ���� ����⸸ ���� �� �ִ�.
		 * ���� �� �ִ� ����Ⱑ �����������, �Ÿ��� ���� ����� ����⸦ ������ ����.
		 * �Ÿ��� ����� ����Ⱑ ���ٸ�, ���� ��, ���ʿ� �ִ� ����⸦ �Դ´�.
		 * �ڽ��� ũ��� ���� ���� ����⸦ ���� �� ���� ũ�Ⱑ 1 �����Ѵ�.
		 */
		while (!q.isEmpty()) {
			Point p = q.poll();
			
			// ���� �Ա�� ���� ����⺸�� �̵��ð� �����ɸ��� Ž�� ����
			if (next.time < p.time) break;
			
			for(int n=0; n<4; n++) {
				int ni = p.i + di[n];
				int nj = p.j + dj[n];
				
				// ��ǥ ��ȿ�� üũ
				if (0>ni || ni>=N || 0>nj || nj>=N || visited[ni][nj] || arr[ni][nj] > babyShark) continue;

				// �̵��� ��ġ�� ����Ⱑ �ְ�, �Ʊ���� ũ�Ⱑ ���� ���
				if (arr[ni][nj] != 0 && arr[ni][nj] < babyShark) {
					// ���� ���� ����Ⱑ �������� ���� ���
					if (next.i == -1 && next.j == -1) {
						next.i = ni;
						next.j = nj;
						next.time = p.time;
					}
					// ���� ���� ����⺸�� ���� ����Ⱑ �� ���ʿ� ��ġ�ϰų�
					// ���� ���� ����Ⱑ ���� ����⺸�� �� ���ʿ� ��ġ�ϴ� ���
					else if ((next.i > ni) ||
							 (next.i == ni && next.j > nj)) {
						next.i = ni;
						next.j = nj;
					}
				}
				
				visited[ni][nj] = true; // �湮���� üũ
				q.add(new Point(ni,nj,p.time+1)); // q�� �߰�
			} /* end of for */
		} /* end of while */
		
		
		if (next.i != -1 && next.j != -1) { // ���� �� �ִ� ����Ⱑ �־��� ���
			arr[next.i][next.j] = 0;
			time += next.time;
			fishNum -= 1;
			cur.i = next.i;
			cur.j = next.j;
			cur.time = 1;
			eatCnt += 1;
//			System.out.printf("%d %d %d[fishNum:%d]\n", cur.i, cur.j, cur.time, fishNum);
			if (eatCnt == babyShark) {
				eatCnt = 0;
				babyShark += 1;
			}
		}
	}
	
	private static class Point {
		private int i;
		private int j;
		private int time;
		
		public Point(int i, int j, int time) {
			this.i = i;
			this.j = j;
			this.time = time;
		}
	}
}
