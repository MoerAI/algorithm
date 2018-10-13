package ch9;

import java.awt.*;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class Calculator extends JFrame {
	
	public Calculator() {
		setTitle("Calculator");
		setSize(500,400);
		Container contentPane = this.getContentPane();
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		JPanel panel_north = new JPanel();
		panel_north.add(new JLabel("계산식 :"));
		panel_north.add(new JTextField(30));
		panel_north.setBackground(Color.gray);
		contentPane.add(panel_north, BorderLayout.NORTH);
		
		JPanel panelCenter = new JPanel();
		contentPane.add(panelCenter, BorderLayout.CENTER);
		panelCenter.setLayout(new GridLayout(4,5));
		panelCenter.add(new JButton("0"));
		panelCenter.add(new JButton("1"));
		panelCenter.add(new JButton("2"));
		panelCenter.add(new JButton("3"));
		panelCenter.add(new JButton("4"));
		panelCenter.add(new JButton("5"));
		panelCenter.add(new JButton("6"));
		panelCenter.add(new JButton("7"));
		panelCenter.add(new JButton("8"));
		panelCenter.add(new JButton("9"));
		panelCenter.add(new JButton("CE"));
		panelCenter.add(new JButton("계산"));
		JButton btnPlus = new JButton("+");
		btnPlus.setBackground(Color.CYAN);
		panelCenter.add(btnPlus);
		JButton btnMinus = new JButton("-");
		btnMinus.setBackground(Color.CYAN);
		panelCenter.add(btnMinus);
		JButton btnMultiplication = new JButton("*");
		btnMultiplication.setBackground(Color.CYAN);
		panelCenter.add(btnMultiplication);
		JButton btnDivision = new JButton("/");
		btnDivision.setBackground(Color.CYAN);
		panelCenter.add(btnDivision);
		this.setVisible(true);
		
		JPanel panel_south = new JPanel();
		contentPane.add(panel_south, BorderLayout.SOUTH);
		panel_south.add(new JLabel("계산 결과 : "));
		panel_south.setBackground(Color.YELLOW);
		panel_south.add(new JTextField(30));
	}
	public static void main(String[] args) {
		new Calculator();
	}

}
