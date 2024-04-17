// struct RedFox { // declaire
//     enemy: bool,
//     life: u8,
// }

// impl RedFox { // defualt
//     fn new()->Self {
//         Self {
//             enemy: true,
//             life: 70,
//         }
//     }
    
//     fn get_noise(&self) -> &str { "Meow?" }
// }

// fn print_noise<T:Noisy>(item:T) {
//     println!("{}", item.get_noise());
// }



// trait Noisy {
//     fn get_noise(&self) -> &str;
// }


// fn main() {
//     let mut fox = RedFox::new();
//     let life_left = fox.life;
//     fox.enemy = false;
// }

//trait
// trait Run {
//     fn run(&self) {
//         println!("I'm running");
//     }
// }

// struct Robot {}
// impl Run for Robot { // no field
//     fn run(&self) {
//         println!("I'm running and robot") // overwrite
//     }
// }

// fn main() {
//     let robot = Robot {};
//     robot.run();
// }

//vector
// fn main() {
//     let mut v:Vec<i32> = vec![1,2,3];

//     println!("{:?}",v);
//     let x = v.pop(); // x= 6
//     println!("{}", v[1])
// }

//hashmap
// use std::collections::HashMap;
// fn main(){
//     let mut h: HashMap<u8, bool> = HashMap::new();
//     h.insert(5, true);
//     h.insert(6, false);
//     let have_five = h.remove(&5).unwrap();
//     println!("{:?}", have_five);
//     println!("{:?}", h);
// }

//VecDeque, HashSet, BTreeMap, LinkedList, BinaryHeap, BTreeSet


//enum(algebraic data types)

// enum Color {
//     Red,
//     Green,
//     Blue,
// }

// enum DispenserItem {
//     Empty,
//     Ammo(u8),
//     Things(String, i32),
//     Place{x: i32, y:i32},
// }
// impl DispenserItem {
//     fn display(&self) {}
// }


// enum Option<T> {
//     Some(T),
//     None,
// }
// fn main() {
//     let my_variable = Some(12);
//     if let Some(x) = my_variable {
//         println!("value is {}", x);
//     }
// }

// fn main() {
//     let my_variable = Some(12);
//     match my_variable {
//         Some(x) =>{
//             println!("value is {}", x);        
//         },
//         None => {
//             println!("no value")
//         },
//     }
// }

//Option: 값이 없는 경우를 가정
// fn main() {
//     let mut x:Option<i32> = Some(5);
//     x.is_some();
//     x.is_none();
//     println!("{}", x.unwrap())
// }

//Result: result, error

// #[must_use]
// enum Result<T, E> {
//     Ok(T),
//     Err(E),
// }

use std::fs::File;
// fn main() {
//     let res = File::open("foo");
//     let f = res.expect("error message");
// }

// fn main() {
//     let res = File::open("foo");
//     if res.is_ok() {
//         let f = res.unwrap();
//     }
// }

// fn main() {
//     let res = File::open("foo");
//     match res {
//         Ok(f) => {println!("File open success")}
//         Err(e) => {println!("error message: {}", e)}
//     }
// }