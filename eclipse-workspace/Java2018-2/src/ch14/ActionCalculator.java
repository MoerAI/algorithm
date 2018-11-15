package ch14;

import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class ActionCalculator extends JFrame{
	
	public ActionCalculator() {
		setTitle("task");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Container c = getContentPane();
		c.setLayout(new FlowLayout());		

		c.add(new JLabel("숫자1"));
		JTextField num1 = new JTextField(23);
		c.add(num1);
		c.add(new JLabel("숫자2"));
		JTextField num2 = new JTextField(23);
		c.add(num2);
		JButton btnAdd = new JButton("더하기");
		JButton btnMinus = new JButton("빼기");
		JButton btnMultiply = new JButton("곱하기");
		JButton btnDivision = new JButton("나누기");
		c.add(btnAdd);
		c.add(btnMinus);
		c.add(btnMultiply);
		c.add(btnDivision);
		c.add(new JLabel("결과"));
		JTextField result = new JTextField(23);
		c.add(result);
		btnAdd.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				Double n1 = Double.parseDouble(num1.getText());
				Double n2 = Double.parseDouble(num2.getText());
				Double rst = n1+n2;
				result.setText(String.valueOf(rst));
			}
		});
		btnDivision.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				Double n1 = Double.parseDouble(num1.getText());
				Double n2 = Double.parseDouble(num2.getText());
				Double rst = n1/n2;
				result.setText(String.valueOf(rst));
			}
		});
		btnMinus.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				Double n1 = Double.parseDouble(num1.getText());
				Double n2 = Double.parseDouble(num2.getText());
				Double rst = n1-n2;
				result.setText(String.valueOf(rst));
			}
		});
		btnMultiply.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				Double n1 = Double.parseDouble(num1.getText());
				Double n2 = Double.parseDouble(num2.getText());
				Double rst = n1*n2;
				result.setText(String.valueOf(rst));
			}
		});
		setSize(330,200);
		setVisible(true);
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new ActionCalculator();
	}
}
