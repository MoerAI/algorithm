package ch9;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

import java.awt.Color;
import java.awt.GridLayout;

public class Ex3 extends JFrame {
	
	public Ex3() {
		setTitle("swing Ex3");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		GridLayout grid = new GridLayout(1,10);
		
		setLayout(grid);
		JButton btn1 = new JButton("0");
		btn1.setBackground(Color.red);
		add(btn1);
		setLayout(grid);
		JButton btn2 = new JButton("1");
		btn2.setBackground(Color.orange);
		add(btn2);
		setLayout(grid);
		JButton btn3 = new JButton("2");
		btn3.setBackground(Color.yellow);
		add(btn3);
		setLayout(grid);
		JButton btn4 = new JButton("3");
		btn4.setBackground(Color.green);
		add(btn4);
		setLayout(grid);
		JButton btn5 = new JButton("4");
		btn5.setBackground(Color.white);
		add(btn5);
		setLayout(grid);
		JButton btn6 = new JButton("5");
		btn6.setBackground(Color.blue);
		add(btn6);
		setLayout(grid);
		JButton btn7 = new JButton("6");
		btn7.setBackground(Color.CYAN);
		add(btn7);
		setLayout(grid);
		JButton btn8 = new JButton("7");
		btn8.setBackground(Color.gray);
		add(btn8);
		setLayout(grid);
		JButton btn9 = new JButton("8");
		btn9.setBackground(Color.pink);
		add(btn9);
		setLayout(grid);
		JButton btn10 = new JButton("9");
		btn10.setBackground(Color.black);
		add(btn10);
		setSize(700,300);
		setVisible(true);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Ex3();
	}

}
