import java.io.*;
import java.util.*;
public class Main{
	public static int solve(String s)
	{
		long sum = 0;
		for (int i = 0; i < s.length(); i++) {
			sum+=Integer.parseInt(s.charAt(i)+"");			
		}
		if(sum<10)
			return (int)sum;
		return solve(sum+"");
	}	

	public static void main(String[] args) throws Throwable {
        Scanner sc = new Scanner(System.in);
		while(true)
		{
			String s = sc.nextLine();
			if(s.equals("0"))
				break;
            System.out.println(solve(s));
		}
	}
}