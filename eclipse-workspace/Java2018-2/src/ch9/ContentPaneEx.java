package ch9;

import java.awt.FlowLayout;

import javax.swing.JButton;
import javax.swing.JFrame;

public class ContentPaneEx extends JFrame {
	ContentPaneEx(){
		setTitle("ContentPane�� JFrame");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		setLayout(new FlowLayout(FlowLayout.LEFT, 30, 40));
		
		add(new JButton("add"));
		add(new JButton("sub"));
		add(new JButton("mul"));
		add(new JButton("div"));
		add(new JButton("Calculate"));
		setSize(300,200);
		setVisible(true);
	}
	public static void main(String[] args) {
		new ContentPaneEx();
	}
}
