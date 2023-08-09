/*
 * 번호 : 13913
 */
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        if(n == k){
            System.out.println(0);
            System.out.println(n);
            return;
        }

        Map<Integer, Boolean> map = new HashMap<>();
        int[] route = new int[100001];
        Arrays.fill(route, -1);
        Queue<Integer> q = new LinkedList();
        q.add(n);
        map.put(n, true);
        int L = 1;
        loop1:
        while(!q.isEmpty()){
            int size = q.size();
            for(int i = 0; i < size; i++){
                int now = q.poll();
                for(int j = 0; j < 3; j++){
                    int nx;
                    if(j == 0) nx = now - 1;
                    else if(j == 1) nx = now + 1;
                    else nx = now * 2;
                    if(nx >= 0 && nx <= 100000 && !map.getOrDefault(nx, false)){
                        q.add(nx);
                        map.put(nx, true);
                        route[nx] = now;
                        if(nx == k){
                            break loop1;
                        }
                    }
                }
            }
            L++;
        }

        Stack<Integer> stack = new Stack<>();
        int x = k;
        while(x != -1){
            stack.push(x);
            x = route[x];
        }

        System.out.println(L);
        StringBuilder sb = new StringBuilder();
        while(!stack.isEmpty()){
            sb.append(stack.pop() + " ");
        }
        System.out.println(sb.toString());

    }
}
