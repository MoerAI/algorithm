package dyjava.ch4;

import java.util.Scanner;

//이거는 예제에 없음
public class CompoundingCalculator {
/*
 * 앞서 만든 단리 계산기를 복리 계산기로 만들어보자
 */
	public static double money;
	public static int year;
	public static double rate;
	public static double interest;
	public static Scanner input = new Scanner(System.in);
	
	public static void main(String[] args) {
		System.out.print("원금을 입력하여 주세요 : ");
		money = input.nextInt();
		System.out.print("예치기간(년)을 입력하여 주세요 : ");
		year = input.nextInt();
		System.out.print("이자율을 입력하여 주세요 : ");
		rate = input.nextDouble();
		for(int i = 0; i<year; i++) {
			interest = money*rate;
			money= money+interest;
		}
		System.out.println("만기시 총 수령 액은 "+(int)money+"원 입니다.");
	}

}
