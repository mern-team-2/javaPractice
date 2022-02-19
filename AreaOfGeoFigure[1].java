package practiceSet;

import java.util.Scanner;

public class AreaOfGeoFigure {
	
//	1:Triangle
	static void areaofTriangle(float base, float height){
		float area = (base* height)/2;
	    System.out.println("Area of Triangle is: " + area);
	}
//	2:Square
	static void areaofSquare(float side) {
		float area = side*side; 
	    System.out.println("Area of Square is: "+area);
	}
//	3:Rectangle
	static void areaofRectangle(float length, float width) {
		float area = length*width;
	    System.out.println("Area of Rectangle is:"+area);
	}
//	4:Circle
	static void areaofCircle(float radius) {
		double area = Math.PI * (radius * radius);
	     System.out.println("The area of circle is: " + area);
	}
	
	
	public static void main(String[] args) {
		
		System.out.println("calculate any of the geomatrical figure area mentioned below.");
		System.out.println("1:Triangle\n2:Square\n3:Rectangle\n4:Circle");
		System.out.println("enter figure number to calculate it's area:");
		
		Scanner input = new Scanner(System.in);
		byte index = input.nextByte();
		
		switch (index) {
		case 1:
			System.out.println("enter width of the Triangle");
			float base = input.nextFloat();
			System.out.println("enter height of the Triangle");
			float height = input.nextFloat();
			
			areaofTriangle(base, height);
			break;
		case 2:
			System.out.println("Enter Side of Square:");
			float side = input.nextFloat();
			
			areaofSquare(side);
			break;
		case 3:
			System.out.println("Enter the length of Rectangle:");
			float length = input.nextFloat();
			System.out.println("Enter the width of Rectangle:");
			float width = input.nextFloat();
			
			areaofRectangle(length, width);
			break;
		case 4:
		    System.out.print("Enter the radius: ");
		    float radius = input.nextFloat();
		    
			areaofCircle(radius);
			break;
		}
		
		input.close();
	}
}
