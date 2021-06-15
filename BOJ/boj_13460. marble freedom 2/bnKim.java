import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

//백준 13460. 구슬 탈출

public class Main {

	static char[][] A;
	static int N;
	static int M;
	static final int[] dx = { 0, 0, -1, 1}; //상하좌우
	static final int[] dy = {-1, 1,  0, 0};
	static boolean redFlag = false;
	static boolean blueFlag = false;
	static boolean endFlag = false;
	static int result = 10;

	public static char[][] tilt(int dir, char[][] before) {
		int blueX = 0;
		int blueY = 0;
		int redX = 0;
		int redY = 0;
		int newX = 0;
		int newY = 0;

		char[][] newArr = new char[N][M];
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				newArr[i][j] = before[i][j];
				if(newArr[i][j] == 'B') {
					blueX = j;
					blueY = i;
				}
				else if(newArr[i][j] == 'R') {
					redX = j;
					redY = i;
				}
			}
		}

		//빨구와 파구가 서로 막힐경우를 대비해서 2번돌림
		for(int i = 0 ; i < 2; i ++) {
			//빨간구슬 굴리기
			newX = redX + dx[dir];
			newY = redY + dy[dir];
			if(newArr[newY][newX] == '.' || newArr[newY][newX] == 'O') {
				newArr[redY][redX] = '.';
				while(newArr[newY][newX] == '.') {
					redX = newX;
					redY = newY;
					newX = redX + dx[dir];
					newY = redY + dy[dir];
				}
				if(newArr[newY][newX] == 'O') {
					redFlag = true;
				}
			}
			if(!redFlag) newArr[redY][redX] = 'R';

			//파란구슬 굴리기
			newX = blueX + dx[dir];
			newY = blueY + dy[dir];
			if(newArr[newY][newX] == '.' || newArr[newY][newX] == 'O') {
				newArr[blueY][blueX] = '.';
				while(newArr[newY][newX] == '.') {
					blueX = newX;
					blueY = newY;
					newX = blueX + dx[dir];
					newY = blueY + dy[dir];
				}
				if(newArr[newY][newX] == 'O') {
					blueFlag = true;
				}
			}
			if(!blueFlag) newArr[blueY][blueX] = 'B';
		}

		return newArr;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());


		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		A = new char[N][M];

		for(int n = 0; n < N; n++) {
			String str = br.readLine();
			for(int m = 0; m < M; m++) {
				A[n][m] = str.charAt(m);
			}
		}

		dfs(A, 10);

		if(!endFlag) result = -1;
		bw.write("" + result);

		br.close();
		bw.close();

	}
/*
	private static void print(char[][]arr) {
		for(int i = 0 ; i < N; i++) {
			for(int j = 0; j < M; j++) {
				System.out.print(arr[i][j]);
			}
			System.out.println();
		}
	}
*/

	private static void dfs(char[][] arr, int cnt) {
		//더 탐색할 필요가 없음
		if(blueFlag) {
			redFlag = false;
			blueFlag = false;
			return;
		}
		else if(redFlag) {
			endFlag = true;
			redFlag = false;
			if(result > (10-cnt)) result = 10-cnt;
			return;
		}
//		if(endFlag) return;
		if(cnt == 0) return;

		char[][] newArr = new char[N][M];
		for(int i = 0; i < 4; i++) {
			newArr = tilt(i, arr);
			dfs(newArr, cnt - 1);
		}
	}
}
