package method;

//Call by Name : �̸��� �ִ� �Լ�
//Method�� Ŀ�� �ΰ� f3�� ������ �ش� �޼ҵ�� �Ѿ��.
//�޼ҵ带 ����� ������ �ݺ��� �Ⱦ�̴�.
public class MethodEx1 {
	public static void view() {
		//�޴� ���ڰ� ���� �̸��� �ִ� �Լ��� ���ϴ� ����  Call by name�̶�� �Ѵ�.
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
