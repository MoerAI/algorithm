package method1;

//인스턴트메서드와 클래스 메서드의 비교
public class MethodEx6 {
	public static void view1() {
		System.out.println("static method");
	}
	public void view2() {
		System.out.println("non-static method");
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		view1();//메모리가 계속해서 잡혀있다.
		
		MethodEx6 ob = new MethodEx6();//ob를 스텍영역에 선언 후
		ob.view2();//힙에 있는 view2를 참조한다.
	}
}