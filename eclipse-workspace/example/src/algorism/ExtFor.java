package algorism;
/*for 구문을 이용하여 아래와 같은 구문을 출력하시오.
 * 4 3 2 1
 * 5 6 7 8
 * 12 11 10 9*/
public class ExtFor {
	public static int i,j=4,k=1;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for(i=4;i<=12;i=i+4) {
			for(;j>=1;j--) {
				if(i>9&&j<9) {
					break;
				}else if(i>5&&j<5) {
					break;
				}else if(i<10&&i>5&&j>=5){
					for(;k<=4;k++) {
						System.out.print(j+" ");
						j=j-1;
					}
					j=12;
					break;
				}else {
					System.out.print(j+" ");
				}
			}
			System.out.println();
			j=4;
			j = j+i;
		}
	}

}
