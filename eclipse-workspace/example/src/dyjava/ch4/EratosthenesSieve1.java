package dyjava.ch4;

public class EratosthenesSieve1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] number = new int[1000];
		int [] prime = new int[200];
		int i, j=0;
		for(i=0;i<number.length;i++) {
			number[i] = i+1;
		}
		i=2;
		while(true) {
			if(number[i-2]%i==0) {
				prime[j]=number[i-1];
				if((j+1)%20==0) {
					System.out.println();
				}
				System.out.print(prime[j]+", ");
				j++;
			}
			i++;
			if(i==1002) {
				break;
			}
		}
	}
}
