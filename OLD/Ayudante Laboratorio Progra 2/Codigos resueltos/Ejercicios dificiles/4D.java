import java.util.*;

public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int lady[] = new int[N];
		for (int i = 0; i < N; i++) {
			lady[i] = sc.nextInt();
		}
		
		int Q = sc.nextInt();
		while (Q-- > 0) {
			int q = sc.nextInt();
			StringBuilder sb = new StringBuilder("");
			
			for (int i = N - 1; i >= 0; i--) {
				if (q > lady[i]) {
					sb.append(lady[i]);
					break;
				}
				
				if (i == 0) {
					sb.append("X");
					break;
				}
			}
			
			for (int i = 0; i < N; i++) {
				if (q < lady[i]) {
					sb.append(" " + lady[i]);
					break;
				}
				
				if (i == N - 1) {
					sb.append(" X");
					break;
				}
			}
			System.out.println(sb.toString());		
		}
	}
}