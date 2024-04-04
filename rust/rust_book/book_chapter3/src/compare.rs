use std::io;

fn main() {
    println!("Ferenhite Celcius Calulator");
    
    println!("Enter f or c");
    let mut temperature_type = String::new();
    io::stdin()
        .read_line(&mut temperature_type)
        .expect("Failed to read line");

    println!("Enter temperature");
    let mut temperature_degree = String::new();
    io::stdin()
        .read_line(&mut temperature_degree)
        .expect("Failed to read line");
    let temperature_degree: f64 = temperature_degree.trim().parse().expect("Failed to parse temperature");

    let result: f64 = if temperature_type.trim() == "f" {
        (temperature_degree - 32.0) / 1.8
    } else {
        temperature_degree * 1.8 + 32.0
    };
    
    println!("Your temperature in another type is : {}", result);
}
