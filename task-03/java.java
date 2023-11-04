import java.util.Scanner;

public class PrimeNumbers {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number: ");
        int n = scanner.nextInt();
        
        for (int i = 1; i<n; i++) {
            int factors = 1;
            
            for (int j = 2; j<=i; j++) {
                if (i%j == 0) {
                    factors += 1;
                }
            }
            
            if (factors == 2) {
                System.out.println(i + " is a prime number\n");
            }
        }
        
    }
}