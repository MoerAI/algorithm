package ch7;

public class StudentP{

	 String 이름;

	 String 학과;

	 int 학번;

	 double 학점평균;

	 

	 public StudentP(String 이름,String 학과,int 학번,double 학점평균)

	 {

	  this.이름=이름;

	  this.학과=학과;

	  this.학번=학번;

	  this.학점평균=학점평균;

	 }

	 public String toString()

	 {

	  return 이름+","+학과+","+학번+","+학점평균;

	 }

	}
