package algorism;

import java.util.Scanner;

/*
 * 정수 n이 주어지면, n개의 여는 괄호 "("와 n개의 닫는 괄호 ")"로 만들 수 있는 괄호 조합을 모두 구하시오.
 * (시간 복잡도 제한 없습니다).
 * */
public class BracketTie {
private static Scanner scanner;
public static int n;
/*
 * Input: 1
 * Output: ["()"]
 * 
 * Input: 2
 * Output: ["(())", "()()"]
 * 
 * Input: 3
 * Output: ["((()))", "(()())", "()(())", "(())()", "()()()"]
 * 
 */
	public static void main(String[] args) {
		scanner = new Scanner(System.in);
		System.out.println("숫자를 입력하여 주세요.");
		n = scanner.nextInt();
		//2^(n-1)
		for(int i = 1; i<n; i++) {
			
		}
	}
}
