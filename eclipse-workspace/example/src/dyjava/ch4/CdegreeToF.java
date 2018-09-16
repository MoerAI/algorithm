package dyjava.ch4;

import java.util.Scanner;

public class CdegreeToF {
	
	public static double C;
	public static int c;
	public static double F;
	public static double f;
	
	public static Scanner input = new Scanner(System.in);
	public static void main(String[] args) {
		C = input.nextDouble();
		F = (9.0/5.0)*C+32;
		System.out.println(C+"C는 "+F+"F입니다.");
		for(c=-60;c<=140;c+=20) {
			f =((9.0/5.0)*c+32);
			System.out.println(c+"c 는"+f+"f 입니다.");
		}
	}

}
