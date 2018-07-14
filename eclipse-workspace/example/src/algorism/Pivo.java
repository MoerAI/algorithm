package algorism;
import java.util.Scanner;
public class Pivo {
	
	/*피보나치 배열은 0과 1로 시작하며, 다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 된다.
	정수 N이 주어지면, N보다 작은 모든 짝수 피보나치 수의 합을 구하여라.*/
	
	private static Scanner scan;

	public static void main(String[] args) {
		scan = new Scanner(System.in);
		System.out.println("숫자를 입력하여 주세요.");
		int a = scan.nextInt();
		int b = pivo(a);
		System.out.println("입력하신 숫자"+a+"까지 모든 피보나치 짝수의 합은"+b+"입니다.");
		
	}
	
	public static int pivo(int a) {
		int b=1,c=1,sum=0;//1,2,3,5,8 
			for(;b<a;) {
				b=b+c;
				c=b-c;
				if(b%2==0) {
					sum=sum+b;
				}
			}
		return sum;
	}
	/*int evenFibSum(int N) {
		  int sum = 0;
		  int x = 1;
		  int y = 2;
		  while (x <= N) {
		    if (x % 2 == 0) {
		      sum += x;
		    }
		    int z = x + y;
		    x = y;
		    y = z;
		  }
		  return sum;
		}*/
}