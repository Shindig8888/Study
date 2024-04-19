use book_chapter14::kinds::PrimaryColor;
use book_chapter14::utils::mix;

fn main() {
    let x = PrimaryColor::Red;
    let y = PrimaryColor::Blue;
    let z = mix(x, y);

    println!("{:?}", z.unwrap())
}
