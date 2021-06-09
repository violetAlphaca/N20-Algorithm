import java.util.ArrayList;
import java.util.Scanner;

public class Main {


	static ArrayList<Cell> emptyCells= new ArrayList<>(); // ArrayList 선언과 동시에 초기화???

	static int [][] A= new int[9][9];
	static boolean flag = false;
	static ArrayList<Integer>[][] avail = new ArrayList[9][9]; //ArrayList의 배열 선언 //static 공간을 할당


	/*** 메인함수 ***/
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);


		for(int i = 0; i < 9; i++) {
			for(int j = 0; j < 9; j++) {
				avail[i][j] = new ArrayList<Integer>(); // 배열에 class를 지정하여 ArrayList 저장 //힙 공간을 할당
				A[i][j] = sc.nextInt();
				if(A[i][j] == 0) {
					emptyCells.add(new Cell(j,i));
				}
			}
		}

		dfs(0,0);


		for(int i = 0; i < 9; i++) {
			for(int j = 0; j < 9; j++) {
				System.out.print(A[i][j] + " ");
			}
			System.out.println();
		}

	}//end of main

	static void dfs(int emptyIdx, int availableIdx) {

		if(emptyIdx == emptyCells.size()) {
			flag = true;
			return;
		}

		Cell now = emptyCells.get(emptyIdx);
		int x = now.x;
		int y = now.y;

		getAvailable(x, y);

		for (int i = availableIdx; i < avail[y][x].size(); i++) {
			A[y][x] = avail[y][x].get(i);
			if (isSudoku(x, y)) {
				dfs(emptyIdx + 1, 0);
				if (flag) return;
			}
			A[y][x] = 0;
		}
	}
	//x, y에 무언가를 넣었을때 스도쿠 상태인지 확인
	static boolean isSudoku(int x, int y) {

		int dx[] = {0, 0, 0, 1, 1, 1, 2, 2, 2};
		int dy[] = {0, 1, 2, 0, 1, 2, 0, 1, 2};

		int sx = x / 3;
		int sy = y / 3;
		sx *= 3;
		sy *= 3;

		for(int i = 0; i < 9; i++) {
			if (A[i][x] == A[y][x] && i != y) return false;
			if (A[y][i] == A[y][x] && i != x) return false;
			int nx = sx+dx[i];
			int ny = sy+dy[i];
			if (A[ny][nx] == A[y][x] && !(ny == y && nx == x)) return false;
		}

		return true;
	}

	static void getAvailable(int x, int y) {
		avail[y][x].clear();
		int[] cnt = new int[10];

		//가로줄 체크
		for(int i = 0; i < 9; i++) {
			cnt[A[i][x]] ++;
		}

		//세로줄 체크
		for(int i = 0; i < 9; i++) {
			cnt[A[y][i]] ++;
		}
		int sx = x / 3;
		int sy = y / 3;
		sx *= 3;
		sy *= 3;


		//x, y가 속한 3 by 3 사각형 체크
		for(int i = 0; i < 3; i++) {
			for(int j = 0; j < 3; j++) {
				cnt[A[sy+i][sx+j]]++;
			}
		}

		//avail[y][x]에 available한 수 add
		for(int i = 1; i < 10; i++) {
			if(cnt[i] == 0) {
				avail[y][x].add(i);
			}
		}

	}


}//end of Sudoku

class Cell{
	int x;
	int y;

	Cell(int x, int y){
		this.x = x;
		this.y = y;
	}
}
