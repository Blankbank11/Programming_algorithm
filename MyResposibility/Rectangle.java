import java.util.Scanner; // import the Scanner class
public class Rectangle {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in); //create a scanner object
        System.out.print("How many size you want: ");
        int size = input.nextInt(); // read user input

        System.out.println();
     for(int i=0;i<=size;i++){
         for(int j=0;j<=size;j++){
             if(i ==0 || j==0 || i==size || j==size){
                 System.out.print("* ");
             }
             else{
                 System.out.print("  ");
             }
         }
         System.out.println();
     }
    }
}
