package method;

//call by reference
public class MethodEx5 {
	public static void view(String str) {
		System.out.println(str);
	}
	public static void view2(int[] num) {
		for(int i:num) {
			System.out.println(i);
		}
//		for(int i =0; i<num.length;i++) {
//			System.out.println(num[i]);
//		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str ="happy";
		view(str);
		
		int[] num = {10,20,30,40,50};
		view2(num);
	}
}
