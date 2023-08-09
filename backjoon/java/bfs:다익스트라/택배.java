/*
 * 번호 : 1719
 */
import java.io.*;
import java.nio.Buffer;
import java.util.*;

public class Main {
    static int n, m;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        ArrayList<Node>[] graph = new ArrayList[n + 1];
        for(int i = 0; i <= n; i++) graph[i] = new ArrayList<>();
        for(int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph[a].add(new Node(b, c));
            graph[b].add(new Node(a, c));
        }

        for(int i = 1; i <= n; i++){
            dik(i, graph);
        }
    }

    static void dik(int start, ArrayList<Node>[] graph){
        int[] distance = new int[n + 1];
        int[] route = new int[n + 1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[start] = 0;
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start, 0));
        while(!pq.isEmpty()){
            Node now = pq.poll();
            if(distance[now.x] < now.c) continue;
            for(Node r : graph[now.x]){
                int cost = now.c + r.c;
                if(distance[r.x] > cost){
                    pq.add(new Node(r.x, cost));
                    distance[r.x] = cost;
                    if(now.x == start) route[r.x] = r.x;
                    else route[r.x] = route[now.x];
                }
            }
        }
        for(int i = 1 ; i <= n; i++){
            if(i == start) System.out.print("- ");
            else System.out.print(route[i] + " ");
        }
        System.out.println();
    }

    static class Node implements Comparable<Node>{
        int x, c;

        public Node(int x, int c) {
            this.x = x;
            this.c = c;
        }

        public int compareTo(Node r){
            return this.c - r.c;
        }
    }
}