package dyjava.ch4;

import java.util.Scanner;

//절대 java num5
public class IsolationCalculator {
	
	/*
	 * 원금이 1,000,000인 경우, 예치 기간을 1년에서 10년까지 매년말에 받을 총 금액을 출력
	 * 년단위 단리이자 = 원금*이율(4.5%)*년(예치기간)
	 * 만기 시 총 수령액(단리적용)=원금(1+이율(4.5%)*년(예치기간))
	 */
	public static double money;
	public static int year;
	public static double rate= 0.045;
	public static double interest;
	public static Scanner input = new Scanner(System.in);
	public static void main(String[] args) {
		System.out.print("원금을 입력하여 주세요 : ");
		money = input.nextInt();
		System.out.print("예치기간(년)을 입력하여 주세요 : ");
		year = input.nextInt();
		interest = money*rate;
		for(int i = 0; i<year;i++) {
			money= money + interest;
		}
		System.out.println("만기시 총 수령 액은 "+(int)money+"원 입니다.");
	}
}
