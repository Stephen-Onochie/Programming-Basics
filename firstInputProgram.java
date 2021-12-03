import java.util.Scanner;


public class firstInputProgram {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter your first name " );
        String firstname = input.next();

        System.out.println("Your first name is " + firstname);
    }
}
