package android;

import java.util.ArrayList;

public class Truck extends Car {
	public static Car car1 = new Car();
	public static void main() {
		car1.setSpeed(30);
		car1.setCc(30);
		ArrayList<Car> myCar = new ArrayList<Car>();
		myCar.add(car1);
		System.out.println(myCar.get(0).getSpeed());
	}
	
	public Truck() {
		// TODO Auto-generated constructor stub
	}
}
