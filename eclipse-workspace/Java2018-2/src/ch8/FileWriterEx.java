package ch8;

import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;

public class FileWriterEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		InputStreamReader in = new InputStreamReader(System.in);
		
		FileWriter fout = null;
		int c;
		try {
			fout = new FileWriter("c:\\tmp\\test.txt");
			while((c=in.read())!=-1) {
				fout.write(c);
			}
			in.close();
			fout.close();
	
		}catch(IOException e) {
			System.out.println("입출력 오류");
		}
	}

}
