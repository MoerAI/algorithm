package ch9;

import java.awt.BorderLayout;
import java.awt.Container;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Ex2 extends JFrame {
	public Ex2(){
		setTitle("GUI Programming");
		setSize(400, 200);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//������ �����츦 ������ ���α׷� ����
		
		Container cpane = this.getContentPane();//����Ʈ ���� ������
		//cpane.setLayout(new FlowLayout());
		
		cpane.setLayout(new BorderLayout(5,7));
		cpane.add(new JButton("NORTH"), BorderLayout.NORTH);
		cpane.add(new JButton("WEST"), BorderLayout.WEST);
		cpane.add(new JButton("CENTER"), BorderLayout.CENTER);
		cpane.add(new JButton("EAST"), BorderLayout.EAST);
		cpane.add(new JButton("SOUTH"), BorderLayout.SOUTH);
		setVisible(true);
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Ex2();
	}

}
