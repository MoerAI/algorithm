package android;

public class Car {
	private int cc;
	private int speed;
	public int getCC() {
		return cc;
	}
	public void setCc(int cc) {
		this.cc = cc;
	}
	public int getSpeed() {
		return speed;
	}
	public void setSpeed(int speed) {
		this.speed = speed;
	}
	public Car() {
		this.cc = getCC();
		this.speed = getSpeed();
	}
}
