package ch7;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;

public class HashMapStudentEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		HashMap<String, Student>map = new HashMap<String,Student>();
		
		map.put("Ȳ����", new Student(1111,"010-1111-1111"));
		map.put("�ѿ���", new Student(2222,"010-2222-2222"));
		map.put("�̿���", new Student(3333,"010-3333-3333"));
		
		System.out.println("HashMap�� ��� ���� : "+map.size());
		
		//��� �л� ���. map�� ��� �ִ� ��� (key,value)�� ���
		Set<String> names= map.keySet();
		Iterator<String> it = names.iterator();
		
		while(it.hasNext()) {
			String name = it.next();
			Student student = map.get(name);
			System.out.println(name+" : "+student.getId()+", tel: "+student.getTel());
		}
	}

}
