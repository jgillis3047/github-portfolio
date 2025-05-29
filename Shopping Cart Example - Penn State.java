/*Filename: ShoppingCart2_Num_gillisjordan.java
	* Name: JordanGillis
	* Class: IST140.002
	* Assignment: In-Class Exercise
	* Date: 9/11/2019
	* 
	*
	*/
public class Shoppingcart2_num_gillisjordan {

	public static void main(String[] args) {
		//Declare and initialize variables 
		int ordNum = 1001; 
		
		int itmNum1 = 987; 
		int itmQty1 = 5;
		double itmPrice1 = 0.10;
		double itmSubTtl1 = itmQty1 * itmPrice1;
		
		int itmNum2 = 682; 
		int itmQty2 = 1;
		double itmPrice2 = 2.50;
		double itmSubTtl2 = itmQty2 * itmPrice2;
		
		//Print store info
		System.out.println("Store name: Jordan Gillis's General Store");
		System.out.println("Store manager: Jordan Gillis");
		System.out.println("Store phone number: 555-1234");
		
		//Order info
		System.out.println("Order name: " + ordNum);
		System.out.println("Order date: January 20,2019");
		
		//Item info
		System.out.println("Item number: " + itmNum1);
		System.out.println("Item description: Apple");
		System.out.println("Item quantity: " + itmQty1); 
		System.out.printf("Item price: $%2.2f\n" , itmPrice1);
		System.out.printf("Item subtotal: $2.2f\n" , itmSubTtl1);
		
		System.out.println("Item number: " + itmNum2);
		System.out.println("Item description: Bread");
		System.out.println("Item quantity: " + itmQty2); 
		System.out.printf("Item price: $%2.2f\n" , itmPrice2);
		System.out.printf("Item subtotal: $2.2f\n" , itmSubTtl2);
		
		//Print order total
		System.out.printf("Order total: $%2.2f" , (itmSubTtl1 + itmSubTtl2));
	}

}
