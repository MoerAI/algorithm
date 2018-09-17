package ch7;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Scanner;
import java.util.Set;

public class HashMapDicEx {

	private static Scanner scanner;

	public static void main(String[] args) {
		//���� �ܾ�� �ѱ� �ܾ��� ���� �����ϴ� HashMap �÷��� ����
		HashMap<String, String>dic= new HashMap<String, String>();
		
		//3���� (Key,Value)���� dic�� ����
		dic.put("baby", "�Ʊ�");
		dic.put("love", "���");
		dic.put("apple", "���");
		
		//dic �÷��ǿ� ��� �ִ� ��� (Key,Value) �� ���
		Set<String>keys = dic.keySet();
		Iterator<String> it = keys.iterator();
		while(it.hasNext()) {
			String key = it.next();
			String value = dic.get(key);
			System.out.println("("+key+","+value+")");
		}
		
		scanner = new Scanner(System.in);
		for(int i=0; i<3; i++) {
			System.out.println("ã�� ���� �ܾ��?");
			String eng = scanner.next();
			System.out.println(dic.get(eng));//'Ű' eng�� �ش��ϴ� '��' ����
		}
	}
}
