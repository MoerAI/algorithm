package ch7;

import java.util.Vector;

public class VectorEx2 {
	public static void main(String[] args) {
		
		Vector<String> v = new Vector<String>();
		v.add("사과");
		v.add("바나나");
		v.add("감");
		v.add("포도");
		v.add("딸기");
		
		for(String s:v) {
			System.out.println(s);
		}
		System.out.println("------------");
		for(int i = 0; i<v.size();i++) {
			System.out.println(v.get(i));
		}
	}
}
