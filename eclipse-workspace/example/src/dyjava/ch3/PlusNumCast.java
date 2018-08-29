package dyjava.ch3;

import java.util.Scanner;

public class PlusNumCast {

	public static Scanner input = new Scanner(System.in);

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("두 실수를 입력하여 주세요.");
		
		double n1 = input.nextDouble();
		double n2 = input.nextDouble();
		
		double add = n1+n2;
		double mean = add/2;
		
		System.out.println("두 실수의 합은 : "+(int)add+" 입니다.");
		System.out.println("두 실수의 평균은 : "+(int)mean+" 입니다." );
	}
}
