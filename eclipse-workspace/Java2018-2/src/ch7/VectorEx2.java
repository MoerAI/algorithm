package ch7;

import java.util.Vector;

public class VectorEx2 {
	public static void main(String[] args) {
		
		Vector<String> v = new Vector<String>();
		v.add("���");
		v.add("�ٳ���");
		v.add("��");
		v.add("����");
		v.add("����");
		
		for(String s:v) {
			System.out.println(s);
		}
		System.out.println("------------");
		for(int i = 0; i<v.size();i++) {
			System.out.println(v.get(i));
		}
	}
}
