package dyjava.ch4;

public class PlusUntil5000 {
	
	public static int i=1;
	public static int sum=0;
	
	public static void main(String[] args) {
		while(true) {
			i++;
			sum +=i;
			if(sum>5000) {
				break;
			}
		}
		System.out.println(i-1);
	}

}
