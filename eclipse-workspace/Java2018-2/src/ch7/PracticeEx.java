package ch7;

import java.util.ArrayList;
import java.util.Scanner;

public class PracticeEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList<StudentP> student = new ArrayList<StudentP>();
		
		Scanner scanner = new Scanner(System.in);
		for(int i=0; i<4; i++) {
			System.out.println("�л� �̸�, �а�, �й�, ��������� �Է��ϼ���.");
			String �̸�= scanner.next();
			String �а�= scanner.next();
			int �й�= scanner.nextInt();
			Double �������= scanner.nextDouble();
			StudentP stup = new StudentP(�̸�, �а�, �й�, �������);
			student.add(stup);
		}
		for(int i=0; i<student.size(); i++) {
			System.out.println(student.get(i));
		}
	}
	}
