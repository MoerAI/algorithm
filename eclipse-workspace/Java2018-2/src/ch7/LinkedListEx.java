package ch7;

import java.util.LinkedList;

public class LinkedListEx {
//LinkedList는 포인터의 연결로 이루어져 있어서 삽입삭제가 빠르다
	public static void main(String[] args) {
		LinkedList<String> list = new LinkedList<String>();
		list.add("사과");
		list.add("감");
		list.add("바나나");
		list.add("포도");
		list.add("딸기");
		list.add(2,"수박");
		
		for(int i = 0; i<list.size();i++) {
			System.out.println(list.get(i));
		}
		System.out.println("-------------------------");
		for (String string : list) {
			System.out.println(string);
		}
	}
}
