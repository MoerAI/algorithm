package ch11;

import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

import ch7.Student;

public class TextFieldEx extends JFrame {
	public TextFieldEx() {
		setTitle("텍스트필드 만들기 예제");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Container c = getContentPane();
		c.setLayout(new FlowLayout());
		
		c.add(new JLabel("이름"));
		JTextField tfname = new JTextField(20);
		c.add(tfname);
		c.add(new JLabel("학과"));
		JTextField tfsub = new JTextField(20);
		c.add(tfsub);
		c.add(new JLabel("주소"));
		JTextField tfadd = new JTextField(20);
		c.add(tfadd);
		ArrayList<Student> alist = new ArrayList<>();
		JButton btn = new JButton("확인");
		
		btn.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				String name = tfname.getText();
				String sub = tfsub.getText();
				String add = tfadd.getText();
				Student stu = new Student(name, sub, add);
				alist.add(stu);
				System.out.println(name+sub+add);
			}
		});
		JButton btnCan = new JButton("취소");
		btnCan.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				
			}
		});
		c.add(btnCan);
		c.add(btn);
		setSize(300,200);
		setVisible(true);
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new TextFieldEx();
	}
}
