package dyjava.ch4;

public class RaggedArraySumAvg {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int ragAry [][]= {{78,48,78,98},{99,92},{29,64,83},{34,78,92,56}};
		int sum = 0;
		double avg;
		for(int i=0; i<ragAry.length;i++) {
			for(int j=0; j<ragAry[i].length;j++) {
				sum =+ragAry[i][j];
			}
		}
		avg = sum/13;
		System.out.println("배열의 합계 :"+sum+" 배열의 평균 :"+avg);
	}
}
