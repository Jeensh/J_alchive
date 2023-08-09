/*
 * 번호 : 2665
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[][] map = new int[n][n];
        for(int i = 0; i < n; i++){
            String s = br.readLine();
            for(int j = 0; j < n; j++){
                map[i][j] = s.charAt(j) - '0';
            }
        }

        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        int[][] ch = new int[n][n];
        for(int[] r : ch) Arrays.fill(r, Integer.MAX_VALUE);
        Queue<Node> q = new LinkedList();
        q.add(new Node(0, 0, 0));
        ch[0][0] = 0;
        while(!q.isEmpty()){
            int size = q.size();
            for(int t = 0; t < size; t++){
                Node now = q.poll();
                for(int i = 0; i < 4; i++){
                    int nx = now.x + dx[i];
                    int ny = now.y + dy[i];
                    if(nx >= 0 && nx < n && ny >= 0 && ny < n && ch[nx][ny] > now.d){
                        if(map[nx][ny] == 1){
                            ch[nx][ny] = now.d;
                            q.add(new Node(nx, ny, now.d));
                        }
                        else if(map[nx][ny] == 0){
                            ch[nx][ny] = now.d + 1;
                            q.add(new Node(nx, ny, now.d + 1));
                        }
                    }
                }
            }
        }
        System.out.println(ch[n - 1][n - 1]);
    }

    static class Node{
        int x, y, d;
        Node(int x, int y, int d){
            this.x = x;
            this.y = y;
            this.d = d;
        }
    }
}