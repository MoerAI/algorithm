package ch9;

import java.awt.BorderLayout;

import javax.swing.JButton;
import javax.swing.JFrame;

public class BorderLayoutEx extends JFrame {
	public BorderLayoutEx() {
		// TODO Auto-generated constructor stub
		setTitle("BorderLayout Sample");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		add(new JButton("Calculate"),BorderLayout.CENTER);
		add(new JButton("add"),BorderLayout.NORTH);
		add(new JButton("sub"),BorderLayout.SOUTH);
		add(new JButton("mul"),BorderLayout.EAST);
		add(new JButton("div"),BorderLayout.WEST);
	}
	
	public static void main(String[] args) {
		new BorderLayoutEx();
	}
}
