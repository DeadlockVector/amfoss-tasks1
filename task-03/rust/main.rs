use std::io;

fn main() {
    println!("Enter the number: ");
    
    let mut n = String::new();
    
    io::stdin().read_line(&mut n).expect("Failed to read input");  // to parse input string into an integer
    
    let n: u32 = n.trim().parse().expect("Invalid input. Please enter a valid integer.");
    
    for i in 2..n {
        let mut factors = 0;
        
        for j in 2..=i {
            if i % j == 0 {
                factors += 1;
            }
        }
        
        if factors == 1 {
            println!("{} is a prime number", i);
        }
    }
}
