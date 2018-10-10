package ch7;

import java.util.ArrayList;
import java.util.Scanner;

public class PracticeEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList<StudentP> student = new ArrayList<StudentP>();
		
		Scanner scanner = new Scanner(System.in);
		for(int i=0; i<4; i++) {
			System.out.println("학생 이름, 학과, 학번, 학점평균을 입력하세요.");
			String 이름= scanner.next();
			String 학과= scanner.next();
			int 학번= scanner.nextInt();
			Double 학점평균= scanner.nextDouble();
			StudentP stup = new StudentP(이름, 학과, 학번, 학점평균);
			student.add(stup);
		}
		for(int i=0; i<student.size(); i++) {
			System.out.println(student.get(i));
		}
	}
	}
