package ch11;

import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class TextFieldEx extends JFrame {
	public TextFieldEx() {
		setTitle("�ؽ�Ʈ�ʵ� ����� ����");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Container c = getContentPane();
		c.setLayout(new FlowLayout());
		
		c.add(new JLabel("�̸�"));
		JTextField tfname = new JTextField(20);
		c.add(tfname);
		c.add(new JLabel("�а�"));
		JTextField tfsub = new JTextField(20);
		c.add(tfsub);
		c.add(new JLabel("�ּ�"));
		JTextField tfadd = new JTextField(20);
		c.add(tfadd);
		JButton btn = new JButton("Ȯ��");
		
		btn.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				String name = tfname.getText();
				String sub = tfsub.getText();
				String add = tfadd.getText();
				System.out.println(name+sub+add);
			}
		});
		JButton btnCan = new JButton("���");
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
