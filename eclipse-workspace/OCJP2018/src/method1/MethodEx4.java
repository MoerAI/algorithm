package method1;

//��ø �޼ҵ�
public class MethodEx4 {
	public static int total(int k, int e, int m) {
		return k+e+m;
	}
	public static double avg(int a) {
		return (double)a/3;
	}
	public static char grade(double avg) {
		int intAvg = (int)avg/10;//Swich������ int�� �� �� �ִ�.
		
		switch(intAvg) {
		case 10: case 9: return 'A';
		case 8: 		 return 'B';
		case 7:			 return 'C';
		case 6:			 return 'D';
		default:		 return 'F';
		}
	}
	public static String result(char a) {
		if(a=='F')
			return "���հ�";
		else
			return "�հ�";
	}
	public static void main(String[] args) {
		int k=95, e=85, m=73;
		System.out.println("����: "+total(k,e,m) +"��");
		System.out.println("���: "+avg(total(k,e,m))+"�� ");
		System.out.println("���� : "+grade(avg(total(k,e,m)))+"�� ");
		System.out.println("���: "+result(grade(avg(total(k,e,m))))+"�Դϴ�.");
	}
}