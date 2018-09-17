package ch7;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;

public class HashMapStudentEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		HashMap<String, Student>map = new HashMap<String,Student>();
		
		map.put("황기태", new Student(1111,"010-1111-1111"));
		map.put("한원선", new Student(2222,"010-2222-2222"));
		map.put("이영희", new Student(3333,"010-3333-3333"));
		
		System.out.println("HashMap의 요소 개수 : "+map.size());
		
		//모든 학생 출력. map에 들어 있는 모든 (key,value)쌍 출력
		Set<String> names= map.keySet();
		Iterator<String> it = names.iterator();
		
		while(it.hasNext()) {
			String name = it.next();
			Student student = map.get(name);
			System.out.println(name+" : "+student.getId()+", tel: "+student.getTel());
		}
	}

}
