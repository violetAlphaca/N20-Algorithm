package com.example.algorithm.D20210430;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class MakeCouple_SungChul {
    public static void main(String args[]) {
        FastScanner sc = new FastScanner();

        int n = sc.nextInt();
        int m = sc.nextInt();

        int[] boy = new int[n + 1];
        int[] girl = new int[m + 1];

        for (int i = 1; i <= n; i++) {
            boy[i] = sc.nextInt();
        }

        for (int i = 1; i <= m; i++) {
            girl[i] = sc.nextInt();
        }

        Arrays.sort(boy);
        Arrays.sort(girl);

        if (n > m) {
            int[] temp = boy;
            boy = girl;
            girl = temp;
        }


        int x = boy.length;
        int y = girl.length;


        long[][] dp = new long[x][y];

        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                dp[i][j] = Integer.MAX_VALUE;
            }
        }

        dp[1][1] = Math.abs(boy[1] - girl[1]);

        for (int i = 2; i < y; i++) {
            dp[1][i] = Math.min(dp[1][i - 1], Math.abs(boy[1] - girl[i]));
        }

        for (int i = 2; i < x; i++) {
            for (int j = i; j < y; j++) {
                if (i == j) {
                    dp[i][j] = dp[i - 1][j - 1] + Math.abs(boy[i] - girl[j]);
                } else {
                    dp[i][j] = Math.min(dp[i - 1][j - 1] + Math.abs(boy[i] - girl[j]), dp[i][j - 1]);
                }
            }
        }


        System.out.println(dp[x - 1][y - 1]);

    }

    public static void printMap(long[][] map) {
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map[0].length; j++) {
                System.out.print(map[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    static class FastScanner {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer("");

        String next() {
            while (!st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        int[] readArray(int n) {
            int[] a = new int[n];
            for (int i = 0; i < n; i++) {
                a[i] = nextInt();
            }
            return a;
        }

        long nextLong() {
            return Long.parseLong(next());
        }
    }

}