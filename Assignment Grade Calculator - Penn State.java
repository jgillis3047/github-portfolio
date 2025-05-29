import java.util.Scanner;

/*
 *Name: Jordan Gillis
 *Class: IST140.002
 *Assignment: Lab 2
 *Date Created:  09/29/2019
 *Filename: IST140002_Lab2_GillisJordan.java
 */
public class IST140002_Lab2_GillisJordan {
	public static void main(String[] args) {
	 Scanner in= new Scanner(System.in);
	 Scanner readInput = new Scanner(System.in);
	 //class information
	 System.out.println(" First name: ");
	 String fname = in.nextLine();
	 System.out.println(" Last name: ");
	 String lname = in.nextLine();
	 System.out.println("Major ");
	 String major = in.nextLine();
	 System.out.println("Class name: ");
	 String classnm = in.nextLine();
	 System.out.println("Assignment name 1: ");
	 String agname1 = in.nextLine();
	 System.out.println("Assignment grade 1: ");
	 String agname2 = in.nextLine();
	 System.out.println("Assignment name 2: ");
	 double aggrade1 = in.nextInt();
	 System.out.println("Assignment grade 2: ");
	 double aggrade2 = in.nextInt();
	 double avg = (aggrade1 + aggrade2)/2;
	 //output
	 System.out.println("name:" +fname  +lname);
	 System.out.println("major:" +major);
	 System.out.println("classname:" +classnm);
	 System.out.println("assignment grade 1:" +agname1 + "" +aggrade1);
	 System.out.println("assignment grade 2:" +agname2 + "" +aggrade2);
	 
	 

	}

}
