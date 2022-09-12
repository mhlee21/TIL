package SWEA_5644;
/*
 * 5644. [���� SW �����׽�Ʈ] ���� ����
 * https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRDL1aeugDFAUo&
 */

import java.io.FileInputStream;
import java.util.Scanner;

public class Solution {
	static int answer;
	static int M; // �� �̵��ð�
	static int A; // BC�� ����
	static int[] userA, userB;
	static int[][] BC;
	static int[] di = {0,-1,0,1,0}; // 0 �� �� �� ��
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
			
			// ����� A�� �̵�����
			userA = new int[M+1];
			for (int i=1; i<=M; i++) {
				userA[i] = sc.nextInt();
			}
			// ����� B�� �̵�����
			userB = new int[M+1];
			for (int i=1; i<=M; i++) {
				userB[i] = sc.nextInt();
			}

			// BC �� ����
			BC = new int[A][4];
			for (int i=0; i<A; i++) {
				// �ϳ��� BC ������ ��ǥ(X, Y), ���� ����(C), ó����(P)�� �����ȴ�.
				for (int j=0; j<4; j++) {
					BC[i][j] = sc.nextInt();
				}
			}
		
			solve();
			
			System.out.println("#" + test_case + " " + answer);
		}
	}
	
	private static void solve() {
		// userA �� ���� ��ġ
		int ai = 1;
		int aj = 1;
		// userB �� ���� ��ġ
		int bi = 10;
		int bj = 10;
		
		int[] charge;
		
		for (int i=0; i<=M; i++) {
			// ��ġ ����
			ai += di[userA[i]];
			aj += dj[userA[i]];
			bi += di[userB[i]];
			bj += dj[userB[i]];
			
//			System.out.printf("i:%d [%d] %d %d [%d] %d %d\n",i, userA[i], ai,aj, userB[i], bi,bj);
			
			int max = 0;
			//����� 2���� ����ϴ� ������ �ߺ� ���� 
			for (int j=0; j<A; j++) { //A�� ����ϴ� ������
				for (int k=0; k<A; k++) { //B�� ����ϴ� ������
					int sum = 0;
					charge = new int[2];
					
					// A�� ������ �˻� �� ����
					if (getDist(ai,aj,BC[j][1], BC[j][0]) <= BC[j][2]) {
						charge[0] = BC[j][3];
					}
					// B�� ������ �˻� �� ����
					if (getDist(bi,bj,BC[k][1], BC[k][0]) <= BC[k][2]) {
						charge[1] = BC[k][3];
					}
					
					if (j!=k) { // ���� �ٸ� ������ ����ϴ� ���
						sum = charge[0] + charge[1];
					} else {	// ���� ������ ����ϴ� ���
						sum = Math.max(charge[0], charge[1]);
					}					
					// �ִ� ������ ����
					max = Math.max(sum, max);
				}
			}
			
			// i���� ��� �ִ� ������ �����ش�.
			answer += max;
			
		} /* end of for */
	}
	
	private static int getDist(int ui,int uj,int i,int j) {
		return Math.abs(ui-i) + Math.abs(uj - j);
	}
}
