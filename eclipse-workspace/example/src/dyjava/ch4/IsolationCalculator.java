package dyjava.ch4;

import java.util.Scanner;

//���� java num5
public class IsolationCalculator {
	
	/*
	 * ������ 1,000,000�� ���, ��ġ �Ⱓ�� 1�⿡�� 10����� �ų⸻�� ���� �� �ݾ��� ���
	 * ����� �ܸ����� = ����*����(4.5%)*��(��ġ�Ⱓ)
	 * ���� �� �� ���ɾ�(�ܸ�����)=����(1+����(4.5%)*��(��ġ�Ⱓ))
	 */
	public static double money;
	public static int year;
	public static double rate= 0.045;
	public static double interest;
	public static Scanner input = new Scanner(System.in);
	public static void main(String[] args) {
		System.out.print("������ �Է��Ͽ� �ּ��� : ");
		money = input.nextInt();
		System.out.print("��ġ�Ⱓ(��)�� �Է��Ͽ� �ּ��� : ");
		year = input.nextInt();
		interest = money*rate;
		for(int i = 0; i<year;i++) {
			money= money + interest;
		}
		System.out.println("����� �� ���� ���� "+(int)money+"�� �Դϴ�.");
	}
}
