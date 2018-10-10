package ch8;
import java.io.*;
public class FileInputStreamEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			FileInputStream in = new FileInputStream("c:\\windows\\system.ini");
			
			int c;
			while((c = in.read()) != -1) {
				System.out.println((char)c);
			}
			in.close();
			
		}catch(IOException e) {
			System.out.println("입출력 오류");
		}
	}

}
