package dyjava.ch3;

import java.util.Scanner;

public class PlusNumCast {

	public static Scanner input = new Scanner(System.in);

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("�� �Ǽ��� �Է��Ͽ� �ּ���.");
		
		double n1 = input.nextDouble();
		double n2 = input.nextDouble();
		
		double add = n1+n2;
		double mean = add/2;
		
		System.out.println("�� �Ǽ��� ���� : "+(int)add+" �Դϴ�.");
		System.out.println("�� �Ǽ��� ����� : "+(int)mean+" �Դϴ�." );
	}
}
