package dyjava.ch3;

import java.util.Scanner;

public class KgToPound {

	public static final double POUND = 0.453592;
	public static Scanner input = new Scanner(System.in);
	public static double weight;
	public static double pw;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Pound�� ��ȯ�� ����(KG)�� �Է��Ͻÿ�.");
		weight = input.nextDouble();
		pw = weight*POUND;
		System.out.print(weight+"kg�� ");
		System.out.printf("%.2fpound�Դϴ�.",pw);
	}
}
