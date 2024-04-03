// fn main() {
//     println!("Hello, world!");
// }

// macro => 파이썬의 펑션같은거 function that writes code

// fn give_age() -> i32 {
//     42
// }


// fn main() {
//     let my_name = "David";
//     println!("My name is : {my_name} and my age is : {}", give_age());
// }

// fn main() {
//     let my_city = "Seoul";
//     let my_year = 2002;
//     let population = 9_987_987;

//     println!("The city of {my_city} in {my_year} had a population of {population}");
// }

// fn main() {
//     let my_city = "Seoul";
//     let my_year = 2002;
//     let population = 9_987_987;

//     println!("The city of {city} in {year} had a population of {population}", 
//     city = my_city,
//     year = my_year,
//     population = population);
// }


// fn main() {
//     let my_city = "Seoul";
//     let my_year = 2002;
//     let population = 9_987_987;

//     println!("The city of {0} in {1} had a population of {2}, I love {0}", 
//     my_city,
//     my_year,
//     population);
// }

// //string interpolation
// fn main() {
//     let my_city = "Seoul";
//     let my_year = 2002;
//     let population = 9_987_987;

//     println!("The city of {my_city} in {my_year} had a population of {population}, I love {my_city}") 
// }

// // expression은 사용안됨


// fn number() -> i32 {
//     8 // 여기에 ;이 있으면 fn number -> ()로 인식
// }

// fn main() {
//     let my_number = number();
//     println!("{my_number}");
// }

// fn empty_tuple() {

// }

// //display print=> {}
// //debug print => {:?}
// fn main() {
//     let tuple = empty_tuple();
//     println!("{:?}", tuple);
// }