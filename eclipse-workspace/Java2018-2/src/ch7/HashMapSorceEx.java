package ch7;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;

public class HashMapSorceEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		HashMap<String, Integer> javaScore = new HashMap<String, Integer>();
		
		//5���� ���� ����
		javaScore.put("��ȫ��", 97);
		javaScore.put("Ȳ����", 34);
		javaScore.put("�̿���", 98);
		javaScore.put("������", 70);
		javaScore.put("�ѿ���", 99);
		
		System.out.println("HashMap�� ��� ���� : "+javaScore.size());
		
		//��� ����� ���� ���. javaScore�� ��� �ִ� ��� (key,value)�� ���
		Set<String>keys = javaScore.keySet();
		Iterator<String> it = keys.iterator();
		
		while(it.hasNext()) {
			String name = it.next();
			int score = javaScore.get(name);
			System.out.println(name+" : "+score);
		}
		
	}

}
