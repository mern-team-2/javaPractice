package codeChallenge;

import java.util.Scanner;


class Gadgett {
	private int id;
	private String name;
	private int price;



	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}
	
	public String getName() {
		return name;
	}


	public void setName(String name) {
		this.name = name;
	}


	public int getPrice() {
		return price;
	}

	public void setPrice(int price) {
		this.price = price;
	}

	public Gadgett(int id, String name, int price) {
		super();
		this.id = id;
		this.name = name;
		this.price = price;
	}

	public Gadgett() {

	}
}

public class Gadgets {
	
	static Scanner userInput = new Scanner(System.in);
	
	public static void main(String[] args) {
		
		// TODO Auto-generated method stub
		System.out.println("Enter number of gadgets: ");
		int num = userInput.nextInt();
		userInput.nextLine();
		
		Gadgett gadget[] = new Gadgett[num];
		
		for (int i = 0; i < num; i++) {
			System.out.println("Enter name of gadget");
			String name = userInput.nextLine();
			
			System.out.println("Enter gadget id: ");
			int id = userInput.nextInt();
			
			System.out.println("Enter price of gadget: ");
			int price = userInput.nextInt();
			userInput.nextLine();
			gadget[i] = new Gadgett(id, name, price);
		}
		
		do {
			System.out.println("1:Display All Gadget"
					+ "\n2:Sort By Gadget Id"
					+ "\n3:Sort by Gadget Price"
					+ "\n4:Search by gadget Id"
					+ "\n5:Update price"
					+ "\n6:Exit");
			System.out.println("Enter your choice");
			int choice = userInput.nextInt();
			userInput.nextLine();
			switch (choice) {
			case 1:
				displayGadgets(gadget);
				break;
			case 2:
				sortById(gadget);
				break;
			case 3:
				sortByPrice(gadget);
				break;
			case 4:
				searchById(gadget);
				break;
			case 5:
				updatePrice(gadget);
			default:
				System.out.println("Enter valid choice");
				break;
			}
		} while (true);

	}
	
//	-- display --
	private static void displayGadgets(Gadgett[] gadget) {
		for (int i = 0; i < gadget.length; i++) {
			System.out.println("Name: " + gadget[i].getName() +
									" id: " + gadget[i].getId() +
										" price: " + gadget[i].getPrice());
		}
		userInput.nextLine();

	}
	
//	-- bubble sort --
	private static void sortById(Gadgett[] gadget) {
		for (int i = 0; i < gadget.length; i++) {
			
			for (int j = 1; j < gadget.length - i; j++) {
				
				if (gadget[j-1].getId() > gadget[j].getId()) {
					Gadgett t = gadget[j - 1];
					gadget[j - 1] = gadget[j];
					gadget[j] = t;
				}
			}
		}
		System.out.println("sorted by gadgets Id: ");
		displayGadgets(gadget);
	}
	
	
//	-- insertion sort --
	private static void sortByPrice(Gadgett[] gadget) {
		
		for (int i = 1; i < gadget.length; i++) {
			  int key = gadget[i].getPrice();
		      int j = i - 1;

		      while (j >= 0 && gadget[j].getPrice()> key) {
		    	  gadget[j + 1].setPrice(gadget[j].getPrice());
		    	  --j;
		      }
		      gadget[j + 1].setPrice(key);
		}
		System.out.println("sorted by gadgets Price: ");
		displayGadgets(gadget);
	}
	
	
//	-- binary search --
	private static void searchById(Gadgett[] gadget) {
		System.out.println("Enter gadget ID: ");
		int id = userInput.nextInt();
		int found = 1;
		int len = gadget.length;
		
		for (int i = 0; i < gadget.length; i++) {
					
				for (int j = 1; j < gadget.length - i; j++) {
					
					if (gadget[j-1].getId() > gadget[j].getId()) {
						Gadgett t = gadget[j - 1];
						gadget[j - 1] = gadget[j];
						gadget[j] = t;
					}
				}
			}
		
		for (int i = 0; i < len; i++) {
			
			int mid = len/2;
			if(id < gadget[mid].getId()) {
				len = len/2;
			}else {
				i = mid;
			}
				
			if (gadget[i].getId() == id) {
				
				System.out.println("Item found: ");
				System.out.println("Name: " + gadget[i].getName() +
										" id: " + gadget[i].getId() + 
												" price: " + gadget[i].getPrice());
				found = 0;
				break;
			}
		}
		if (found == 1){
			System.out.println("Not found");
		}

	}

//	-- update --
	private static void updatePrice(Gadgett[] gadget) {
		
		System.out.println("Enter gadget name: ");
		String name = userInput.nextLine();
		
		System.out.println("Enter new price: ");
		int newPrice = userInput.nextInt();
		userInput.nextLine();
		int found = 1;
		
		for (int i = 0; i < gadget.length; i++) {
			if (gadget[i].getName().equals(name)) {
				gadget[i].setPrice(newPrice);
				found = 0;
				break;
			}
		}
		if (found == 1){
			System.out.println("gadget Not found");
		}else {
			System.out.println("After Updating Gadget Price: ");
			displayGadgets(gadget);
		}
		
	}

	}

