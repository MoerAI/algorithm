package dyjava.ch3;

import java.util.Scanner;

public class LeapYear {
/*
 * 기원 년수가 4로 나누어 떨어지는 해는 우선 윤년으로 하고,
 * 1번 중에서 100으로 나누어 떨어지는 해를 평년으로 하며,
 * 다만 400으로 나누어떨어지는 해는 윤년으로 정한다.
 */
	public static Scanner input = new Scanner(System.in);
	public static int year;
	
	public static void main(String[] args) {
		System.out.print("윤년계산기 입니다. 년도를 입력하여주세요 : ");
		year = input.nextInt();
		if(year%4==0) {
			System.out.println(year+"은 윤년입니다.");
		}else if(year%100==0) {
			if(year%400==0) {
				System.out.println(year+"은 윤년입니다.");
			}else {
			System.out.println(year+"은 평년입니다.");
			}
		}else {
			System.out.println(year+"은 평년입니다.");
		}
	}
}
