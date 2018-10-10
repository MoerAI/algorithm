package ch8;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class FileOutputStreamEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			FileOutputStream fout = new FileOutputStream("c:\\test.out");
			FileInputStream fin = null;
			for(int i=0; i<10; i++) {
				int n = 10 - i;
				fout.write(n);
			}
			fout.close();
			fin = new FileInputStream("c:\\test.out");
			
			int c = 0;
			while((c=fin.read())!=-1) {
				System.out.print(c+" ");
			}
			fin.close();
		}catch(IOException e) {
			System.out.println("입출력 오류");
		}
	}

}
