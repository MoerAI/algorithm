package method1;

//�ν���Ʈ�޼���� Ŭ���� �޼����� ��
public class MethodEx6 {
	public static void view1() {
		System.out.println("static method");
	}
	public void view2() {
		System.out.println("non-static method");
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		view1();//�޸𸮰� ����ؼ� �����ִ�.
		
		MethodEx6 ob = new MethodEx6();//ob�� ���ؿ����� ���� ��
		ob.view2();//���� �ִ� view2�� �����Ѵ�.
	}
}