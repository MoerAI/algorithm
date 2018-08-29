package dyjava.ch3;

import java.util.Scanner;

public class KgToPound {

	public static final double POUND = 0.453592;
	public static Scanner input = new Scanner(System.in);
	public static double weight;
	public static double pw;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Pound로 변환할 무게(KG)을 입력하시오.");
		weight = input.nextDouble();
		pw = weight*POUND;
		System.out.print(weight+"kg은 ");
		System.out.printf("%.2fpound입니다.",pw);
	}
}
