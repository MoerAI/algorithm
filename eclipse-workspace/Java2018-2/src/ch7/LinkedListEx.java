package ch7;

import java.util.LinkedList;

public class LinkedListEx {
//LinkedList�� �������� ����� �̷���� �־ ���Ի����� ������
	public static void main(String[] args) {
		LinkedList<String> list = new LinkedList<String>();
		list.add("���");
		list.add("��");
		list.add("�ٳ���");
		list.add("����");
		list.add("����");
		list.add(2,"����");
		
		for(int i = 0; i<list.size();i++) {
			System.out.println(list.get(i));
		}
		System.out.println("-------------------------");
		for (String string : list) {
			System.out.println(string);
		}
	}
}
