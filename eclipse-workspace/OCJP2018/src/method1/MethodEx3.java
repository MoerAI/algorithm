package method1;

//Call by value
public class MethodEx3 {
	public static void show1(char a, double b, int c) {
		System.out.println(a+" "+b+" "+c);
	}
	public static int show2(int a, int b, int c) {
		return a+b+c;
	}
	public static double show3(int a, int b, int c) {
		return (double)show2(a,b,c)/3;
	}
	public static String show4(int a, int b, int c) {
		double d = show3(a,b,c);
		if(d>=60)
			return "�հ�";
		else
			return "���հ�";
	}
	public static void main(String[] args) {
		show1('A',10.5,100);
		int sum=show2(95,85,73);
		System.out.println("�հ�:"+sum);
		System.out.println("���:"+show3(95,85,73));
		System.out.printf("%.2f \n",show3(95,85,73));
		System.out.println("���: "+show4(95,85,73));
	}
}
