package ch9;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.GridLayout;

import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class MyFrame extends JFrame {
	
	public MyFrame() {
		setTitle("GUI Programming");
		setSize(500, 400);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//프레임 윈도우를 닫으면 프로그램 종료
		
		Container cpane = this.getContentPane();//컨텐트 팬을 가져옴
		//cpane.setLayout(new FlowLayout());
		
		JPanel panel1 = new JPanel();
		panel1.setLayout(new GridLayout(4, 1));
		panel1.setBackground(Color.YELLOW);
		panel1.add(new JLabel("아이디"));
		panel1.add(new JTextField(20));
		panel1.add(new JLabel("페스워드"));
		panel1.add(new JTextField(20));
		
		
		JPanel panel2 = new JPanel();
		cpane.add(panel2 ,BorderLayout.WEST);
		panel2 = new JPanel();
		panel2.setLayout(new GridLayout(4, 1));
		panel2.setBackground(Color.GREEN);
		panel2.add(new JLabel("채크하세요."));
		panel2.add(new JCheckBox("C# JCheckBox"));
		panel2.add(new JCheckBox("C++ JCheckBox"));
		this.setVisible(true);//this(클래스)를 안써도 괜찮은 이유는 JFrame의 매소드들이 static으로 선언되었기 때문이다.
		
	}
	
	public static void main(String[] args) {
		
		new MyFrame();
		
	}
}
