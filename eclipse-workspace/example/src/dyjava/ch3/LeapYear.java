package dyjava.ch3;

import java.util.Scanner;

public class LeapYear {
/*
 * ��� ����� 4�� ������ �������� �ش� �켱 �������� �ϰ�,
 * 1�� �߿��� 100���� ������ �������� �ظ� ������� �ϸ�,
 * �ٸ� 400���� ����������� �ش� �������� ���Ѵ�.
 */
	public static Scanner input = new Scanner(System.in);
	public static int year;
	
	public static void main(String[] args) {
		System.out.print("������� �Դϴ�. �⵵�� �Է��Ͽ��ּ��� : ");
		year = input.nextInt();
		if(year%4==0) {
			System.out.println(year+"�� �����Դϴ�.");
		}else if(year%100==0) {
			if(year%400==0) {
				System.out.println(year+"�� �����Դϴ�.");
			}else {
			System.out.println(year+"�� ����Դϴ�.");
			}
		}else {
			System.out.println(year+"�� ����Դϴ�.");
		}
	}
}
