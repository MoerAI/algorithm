package method1;

//중첩 메소드
public class MethodEx4 {
	public static int total(int k, int e, int m) {
		return k+e+m;
	}
	public static double avg(int a) {
		return (double)a/3;
	}
	public static char grade(double avg) {
		int intAvg = (int)avg/10;//Swich문에는 int만 들어갈 수 있다.
		
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
			return "불합격";
		else
			return "합격";
	}
	public static void main(String[] args) {
		int k=95, e=85, m=73;
		System.out.println("총점: "+total(k,e,m) +"점");
		System.out.println("평균: "+avg(total(k,e,m))+"점 ");
		System.out.println("학점 : "+grade(avg(total(k,e,m)))+"점 ");
		System.out.println("결과: "+result(grade(avg(total(k,e,m))))+"입니다.");
	}
}