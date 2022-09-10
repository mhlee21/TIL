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
				if (arr[i][j] == 9) { //아기 상어의 위치
					arr[i][j] = 0;
					cur = new Point(i,j,1);
				}
				if (arr[i][j] != 9 && arr[i][j] != 0) { // 물고기 수 세기
					fishNum += 1;
				}
			}
		}
		
		int tmp;
		while(fishNum!=0) { // 남은 물고기가 없을 때 까지 탐색
			tmp = fishNum;
//			System.out.printf("%d %d %d[%d]\n", cur.i, cur.j, cur.time, fishNum);
			bfs(cur);
			if (tmp == fishNum) {
				// 탐색 전 후가 같은 경우 종료 -> 더이상 먹을 수 있는 물고기가 없음
				break;
			}
		}
		
		System.out.println(time);
	}
	
	private static void bfs(Point cur) {
		boolean[][] visited = new boolean[N][N]; //방문 여부 체크
		Point next = new Point(-1,-1,Integer.MAX_VALUE); // 다음 먹기로 정해진 물고기의 좌표
		Queue<Point> q = new LinkedList<Point>();
		q.add(cur);
		visited[cur.i][cur.j] = true;
		
		/*
		 * 아기상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
		 * 먹을 수 있는 물고기가 여러마리라면, 거리가 가장 가까운 물고기를 먹으러 간다.
		 * 거리가 가까운 물고기가 많다면, 가장 위, 왼쪽에 있는 물고기를 먹는다.
		 * 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.
		 */
		while (!q.isEmpty()) {
			Point p = q.poll();
			
			// 다음 먹기로 정한 물고기보다 이동시간 오래걸리면 탐색 종료
			if (next.time < p.time) break;
			
			for(int n=0; n<4; n++) {
				int ni = p.i + di[n];
				int nj = p.j + dj[n];
				
				// 좌표 유효성 체크
				if (0>ni || ni>=N || 0>nj || nj>=N || visited[ni][nj] || arr[ni][nj] > babyShark) continue;

				// 이동할 위치에 물고기가 있고, 아기상어보다 크기가 작은 경우
				if (arr[ni][nj] != 0 && arr[ni][nj] < babyShark) {
					// 다음 먹을 물고기가 정해지지 않은 경우
					if (next.i == -1 && next.j == -1) {
						next.i = ni;
						next.j = nj;
						next.time = p.time;
					}
					// 다음 먹을 물고기보다 현재 물고기가 더 위쪽에 위치하거나
					// 다음 먹을 물고기가 현재 물고기보다 더 왼쪽에 위치하는 경우
					else if ((next.i > ni) ||
							 (next.i == ni && next.j > nj)) {
						next.i = ni;
						next.j = nj;
					}
				}
				
				visited[ni][nj] = true; // 방문여부 체크
				q.add(new Point(ni,nj,p.time+1)); // q에 추가
			} /* end of for */
		} /* end of while */
		
		
		if (next.i != -1 && next.j != -1) { // 먹을 수 있는 물고기가 주어진 경우
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
