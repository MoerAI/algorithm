package ch10;

import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class MouseAdapterEx extends JFrame{
	JPanel contentPane = new JPanel();
	JLabel la;

	public MouseAdapterEx() {
		setTitle("Mouse 이벤트 예제");
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		setContentPane(contentPane);
		contentPane.setLayout(null);
		contentPane.addMouseListener(new MyMouseAdapter());
		
		la = new JLabel("hello");
		la.setSize(30,30);
		la.setLocation(30,30);
		contentPane.add(la);
		setSize(200,200);
		setVisible(true);
	}
	class MyMouseAdapter extends MouseAdapter{
		public void mousePressed(MouseEvent e) {
			int x = e.getX();
			int y = e.getY();
			la.setLocation(x,y);
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new MouseListenerEx();
	}
}
