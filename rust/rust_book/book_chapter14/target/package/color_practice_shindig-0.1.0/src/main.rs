use color_practice_shindig::kinds::PrimaryColor;
use color_practice_shindig::utils::mix;

fn main() {
    let x = PrimaryColor::Red;
    let y = PrimaryColor::Blue;
    let z = mix(x, y);

    println!("{:?}", z.unwrap())
}
