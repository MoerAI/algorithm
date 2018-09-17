package ch7;

public class Student {
	int id;
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getTel() {
		return tel;
	}
	public void setTel(String tel) {
		this.tel = tel;
	}
	private String tel;
	public Student(int id, String tel) {
		this.id=id;
		this.tel = tel;
	}
}