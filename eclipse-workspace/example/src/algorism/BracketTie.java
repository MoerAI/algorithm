package algorism;

import java.util.Scanner;

/*
 * ���� n�� �־�����, n���� ���� ��ȣ "("�� n���� �ݴ� ��ȣ ")"�� ���� �� �ִ� ��ȣ ������ ��� ���Ͻÿ�.
 * (�ð� ���⵵ ���� �����ϴ�).
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
		System.out.println("���ڸ� �Է��Ͽ� �ּ���.");
		n = scanner.nextInt();
		//2^(n-1)
		for(int i = 1; i<n; i++) {
			
		}
	}
}
