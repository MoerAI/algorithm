package ch7;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;

public class HashMapSorceEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		HashMap<String, Integer> javaScore = new HashMap<String, Integer>();
		
		//5개의 점수 저장
		javaScore.put("한홍진", 97);
		javaScore.put("황기태", 34);
		javaScore.put("이영희", 98);
		javaScore.put("정원석", 70);
		javaScore.put("한원선", 99);
		
		System.out.println("HashMap의 요소 개수 : "+javaScore.size());
		
		//모든 사람의 점수 출력. javaScore에 들어 있는 모든 (key,value)쌍 출력
		Set<String>keys = javaScore.keySet();
		Iterator<String> it = keys.iterator();
		
		while(it.hasNext()) {
			String name = it.next();
			int score = javaScore.get(name);
			System.out.println(name+" : "+score);
		}
		
	}

}
