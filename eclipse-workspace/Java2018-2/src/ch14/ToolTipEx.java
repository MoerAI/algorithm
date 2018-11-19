package ch14;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.JToolBar;

public class ToolTipEx extends JFrame {
	Container contentPane;
	
	ToolTipEx(){
		setTitle("ƫ������");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		contentPane = getContentPane();
		createToolBar();
		setSize(400,150);
		setVisible(true);
	}
	void createToolBar() {
		JToolBar bar = new JToolBar("Kitae Menu");
		bar.setBackground(Color.LIGHT_GRAY);
		JButton newBtn = new JButton("new");
		newBtn.setToolTipText("������ �����մϴ�.");
		bar.add(newBtn);
		
		JButton openBtn = new JButton(new ImageIcon("./images/open.jpg"));
		openBtn.setToolTipText("������ ���ϴ�.");
		bar.add(openBtn);
		bar.addSeparator();
		
		JButton saveBtn = new JButton(new ImageIcon("./images/save.jpg"));
		saveBtn.setToolTipText("������ �����մϴ�");
		bar.add(saveBtn);
		bar.addSeparator();
		
		bar.add(new JLabel("search"));
		
		JTextField tf = new JTextField("text field");
		tf.setToolTipText("ã�����ϴ� ���ڿ��� �Է��ϼ���");
		bar.add(tf);
		contentPane.add(bar,BorderLayout.NORTH);
	}
	public static void main(String[] args) {
		new ToolTipEx();
	}

}
