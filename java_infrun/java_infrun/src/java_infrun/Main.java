package java_infrun;

import java.util.*;

public class Main {
	
	public static ArrayList<Integer> solve(int n, int k, int[] arr) {
		ArrayList<Integer> answer = new ArrayList<>();
		HashMap<Integer, Integer> map = new HashMap<>();
		for(int i = 0; i < k - 1; i++)
			map.put(arr[i], map.getOrDefault(arr[i], 0) + 1);
		int lt = 0;
		for(int rt = k - 1; rt < n; rt++)
		{
			map.put(arr[rt], map.getOrDefault(arr[rt], 0) + 1);
			answer.add(map.size());
			map.put(arr[lt], map.get(arr[lt]) - 1);
			if (map.get(arr[lt]) == 0)
				map.remove(arr[lt]);
			lt++;
		}
		
		
		
		return answer;
	}
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int n, k;
		n = scan.nextInt();
		k = scan.nextInt();
		int arr[] = new int[n];
		for(int i = 0; i < n; i++)
			arr[i] = scan.nextInt();
		for(int x : solve(n, k, arr))
			System.out.print(x + " ");
	}
}