package ch8;

import java.io.FileReader;
import java.io.FileWriter;

public class FileReaderEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			//������ �о��
			FileReader fin = new FileReader("C:\\Users\\frien\\Documents\\algorithm\\eclipse-workspace\\Java2018-2\\src\\ch8\\test.txt");
			//������ ��
			FileWriter fout = new FileWriter("C:\\Users\\frien\\Documents\\algorithm\\eclipse-workspace\\Java2018-2\\src\\ch8\\test_copy.txt");
			int c;
			while((c=fin.read())!=-1) {//read()�޼ҵ��� ������ int������ -1�� ������ �������� �ǹ�
				fout.write(c);//Read�� ���� ���� ��
				System.out.print((char)c);//Read�� ���� ���� �ֿܼ� ���
			}
			fin.close();//�аų� �� ������ �ݾ������
			fout.close();
		} catch (Exception e) {//���� ����ó���� �� ���� ����
			e.printStackTrace();
			System.out.println("������ ã�� �� �����ϴ�.");
		}
	}
}
