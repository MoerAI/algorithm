package dyjava.ch4;

import java.util.Scanner;

//�̰Ŵ� ������ ����
public class CompoundingCalculator {
/*
 * �ռ� ���� �ܸ� ���⸦ ���� ����� ������
 */
	public static double money;
	public static int year;
	public static double rate;
	public static double interest;
	public static Scanner input = new Scanner(System.in);
	
	public static void main(String[] args) {
		System.out.print("������ �Է��Ͽ� �ּ��� : ");
		money = input.nextInt();
		System.out.print("��ġ�Ⱓ(��)�� �Է��Ͽ� �ּ��� : ");
		year = input.nextInt();
		System.out.print("�������� �Է��Ͽ� �ּ��� : ");
		rate = input.nextDouble();
		for(int i = 0; i<year; i++) {
			interest = money*rate;
			money= money+interest;
		}
		System.out.println("����� �� ���� ���� "+(int)money+"�� �Դϴ�.");
	}

}
