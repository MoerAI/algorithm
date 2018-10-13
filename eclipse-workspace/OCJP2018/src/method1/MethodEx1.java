package method;

//Call by Name : 이름만 있는 함수
//Method에 커서 두고 f3을 누르면 해당 메소드로 넘어간다.
//메소드를 만드는 이유는 반복이 싫어서이다.
public class MethodEx1 {
	public static void view() {
		//받는 인자가 없고 이름만 있는 함수를 콜하는 것을  Call by name이라고 한다.
		System.out.println("Korea");
	}
	private static void star() {
		System.out.println("*******");
	}
	
	public static void main(String[] args) {
		view();
		star();
	}
	
}
