package ch8;

import java.io.FileReader;
import java.io.FileWriter;

public class FileReaderEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			//파일을 읽어옴
			FileReader fin = new FileReader("C:\\Users\\frien\\Documents\\algorithm\\eclipse-workspace\\Java2018-2\\src\\ch8\\test.txt");
			//파일을 씀
			FileWriter fout = new FileWriter("C:\\Users\\frien\\Documents\\algorithm\\eclipse-workspace\\Java2018-2\\src\\ch8\\test_copy.txt");
			int c;
			while((c=fin.read())!=-1) {//read()메소드의 리턴은 int형으로 -1은 파일의 마지막을 의미
				fout.write(c);//Read로 읽은 값을 씀
				System.out.print((char)c);//Read로 읽은 값을 콘솔에 출력
			}
			fin.close();//읽거나 쓴 파일은 닫아줘야함
			fout.close();
		} catch (Exception e) {//각종 예외처리를 한 번에 해줌
			e.printStackTrace();
			System.out.println("파일을 찾을 수 없습니다.");
		}
	}
}
