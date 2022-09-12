package SWEA_5644;
/*
 * 5644. [모의 SW 역량테스트] 무선 충전
 * https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo&
 */

import java.io.FileInputStream;
import java.util.Scanner;

public class Solution {
	static int answer;
	static int M; // 총 이동시간
	static int A; // BC의 개수
	static int[] userA, userB;
	static int[][] BC;
	static int[] di = {0,-1,0,1,0}; // 0 상 우 하 좌
	static int[] dj = {0,0,1,0,-1};
	
	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("src/SWEA_5644/sample_input.txt"));
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++)
		{
			answer = 0;
			M = sc.nextInt();
			A = sc.nextInt();
			
			// 사용자 A의 이동정보
			userA = new int[M+1];
			for (int i=1; i<=M; i++) {
				userA[i] = sc.nextInt();
			}
			// 사용자 B의 이동정보
			userB = new int[M+1];
			for (int i=1; i<=M; i++) {
				userB[i] = sc.nextInt();
			}

			// BC 의 정보
			BC = new int[A][4];
			for (int i=0; i<A; i++) {
				// 하나의 BC 정보는 좌표(X, Y), 충전 범위(C), 처리량(P)로 구성된다.
				for (int j=0; j<4; j++) {
					BC[i][j] = sc.nextInt();
				}
			}
		
			solve();
			
			System.out.println("#" + test_case + " " + answer);
		}
	}
	
	private static void solve() {
		// userA 의 시작 위치
		int ai = 1;
		int aj = 1;
		// userB 의 시작 위치
		int bi = 10;
		int bj = 10;
		
		int[] charge;
		
		for (int i=0; i<=M; i++) {
			// 위치 갱신
			ai += di[userA[i]];
			aj += dj[userA[i]];
			bi += di[userB[i]];
			bj += dj[userB[i]];
			
//			System.out.printf("i:%d [%d] %d %d [%d] %d %d\n",i, userA[i], ai,aj, userB[i], bi,bj);
			
			int max = 0;
			//사용자 2명이 사용하는 충전소 중복 조합 
			for (int j=0; j<A; j++) { //A가 사용하는 충전소
				for (int k=0; k<A; k++) { //B가 사용하는 충전소
					int sum = 0;
					charge = new int[2];
					
					// A의 충전량 검사 후 갱신
					if (getDist(ai,aj,BC[j][1], BC[j][0]) <= BC[j][2]) {
						charge[0] = BC[j][3];
					}
					// B의 충전량 검사 후 갱신
					if (getDist(bi,bj,BC[k][1], BC[k][0]) <= BC[k][2]) {
						charge[1] = BC[k][3];
					}
					
					if (j!=k) { // 서로 다른 충전소 사용하는 경우
						sum = charge[0] + charge[1];
					} else {	// 같은 충전소 사용하는 경우
						sum = Math.max(charge[0], charge[1]);
					}					
					// 최대 충전량 갱신
					max = Math.max(sum, max);
				}
			}
			
			// i초인 경우 최대 충전량 더해준다.
			answer += max;
			
		} /* end of for */
	}
	
	private static int getDist(int ui,int uj,int i,int j) {
		return Math.abs(ui-i) + Math.abs(uj - j);
	}
}
