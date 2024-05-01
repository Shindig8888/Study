//고급기능

//안전하지 않은 러스트

//#안전하지 않은 슈퍼파워
// --원시 포인터 역참조
// fn main() {
//     let mut num = 5;
//     let r1 = &num as *const i32;
//     let r2 = &mut num as *mut i32;

//     unsafe {
//         println!("r1 is : {}", *r1);
//         println!("r2 is : {}", *r2);

//     }

//     let address = 0x012345usize;
//     let r = address as *const i32; // 역참조는 불가
// }

// --안전하지 않은 함수 혹은 메서드 호출
// unsafe fn dangerous () {}

// fn main() {
//     unsafe {
//         dangerous()
//     }

// }

// use std::slice;

// fn main() {
//     let mut v = vec![1, 2, 3, 4, 5, 6];

//     let r = &mut v[..];

//     let (a, b) = r.split_at_mut(3);

//     assert_eq!(a, &mut [1, 2, 3]);
//     assert_eq!(b, &mut [4, 5, 6]);
// }

// fn split_at_mut(values: &mut [i32], mid: usize) -> (&mut [i32], &mut [i32]) {
//     let len = values.len();
//     let ptr = values.as_mut_ptr();

//     assert!(mid <= len);

//     unsafe {
//         (
//             slice::from_raw_parts_mut(ptr, mid),
//             slice::from_raw_parts_mut(ptr.add(mid), len - mid),
//         )
//     }
// }

//extern

// extern  "C" {
//     fn abs(input: i32) -> i32;
// }

// fn main() {
//     unsafe {
//         println!("Absolute value of -3 according to C: {}", abs(-3))
//     }
// }

// --가변 정적 변수에 접근 및 수정
// static HELLOW_WORD: &str = "Hello, world";

// fn main() {
//     println!("name is: {}", HELLOW_WORD);
// }

// static mut COUNTER: u32 = 0;

// fn add_to_count(inc: u32) {
//     unsafe {
//         COUNTER += inc;
//     }
// }

// fn main() {
//     add_to_count(3);

//     unsafe {
//         println!("COUNTER: {}", COUNTER)
//     }
// }
// --안전하지 않은 트레이트 구현

// unsafe trait Foo {
//     //..
// }

// unsafe impl Foo for i32 {
//     //..
// }

// fn main() {}
// --union의 필드 접근

//고급 트레이트

//#연관 타입
// pub trait Iterator {
//     type  Item;

//     fn next(&mut self) -> Option<Self::Item>;
// }

// impl Iterator for Counter {
//     type Item = u32;

//     fn next(&mut self) -> Option<Self::Item> {
//         //..
//     }
// }

//#기본 제네릭 타입 매개변수와 연산자 오버로딩

// use std::ops::Add;

// #[derive(Debug, Copy, Clone, PartialEq)]
// struct Point {
//     x: i32,
//     y: i32,
// }

// impl Add for Point {
//     type Output = Point;

//     fn add(self, other: Point) -> Point {
//         Point {
//             x: self.x + other.x,
//             y: self.y + other.y,
//         }
//     }
// }

// fn main() {
//     assert_eq!(
//         Point { x: 1, y: 0 } + Point { x: 2, y: 3 },
//         Point { x: 3, y: 3 }
//     );
// }

//#모호성 방지를 위한 완전 정규화 문법

// trait Pilot {
//     fn fly(&self);
// }

// trait Wizard {
//     fn fly(&self);
// }

// struct Human;

// impl Pilot for Human {
//     fn fly(&self) {
//         println!("This is your captain speaking.");
//     }
// }

// impl Wizard for Human {
//     fn fly(&self) {
//         println!("Up!")
//     }
// }

// impl Human {
//     fn fly(&self) {
//         println!("waving arms furiously*")
//     }
// }

// fn main() {
//     let person = Human;
//     person.fly();

//     Pilot::fly(&person);
//     Wizard::fly(&person);
//     person.fly();
// }

//연관 함수가 있는 트레이트와 트레이트를 구현하면서 동시에 같은 이름의 연관 함수가 있는 타입

// trait Animal {
//     fn baby_name() -> String;
// }

// struct Dog;

// impl Dog {
//     fn baby_name() -> String {
//         String::from("Spot")
//     }
// }

// impl Animal for Dog {
//     fn baby_name() -> String {
//         String::from("puppy")
//     }
// }

// fn main() {
//     println!("A baby dog is called a {}", <Dog as Animal>::baby_name())
// }

//타입 별칭, 동의어

// fn main() {
//     type Kilometer = i32;

//     let x: i32 = 5;
//     let y: Kilometer = 4;

//     println!("x+y = {}", x + y);
// }

// fn main() {
//     type Thunk = Box<dyn Fn() + Send + 'static>
//     let f: Thunk = Box::new(|| println!("hi"));

// }

//절대 반환하지 않는 부정 타입

// fn bar () -> ! {
//     //..
// }

//동적 크기 타입과 Sized 트레이트
// fn generic<T:?Sized> (t: &T) {
//     //..
// }

// 고급 함수와 클로저
//함수 포인터

// fn add_one(x: i32) -> i32 {
//     x + 1
// }

// fn do_twice(f: fn(i32) -> i32, arg: i32) -> i32 {
//     f(arg) + f(arg)
// }

// fn main() {
//     let answer = do_twice(add_one, 5);

//     println!("The anser is: {}", answer);
// }

//클로저 반환
// fn returns_closure() -> Box<dyn Fn(i32) -> i32> {
//     Box::new(|x| x + 1)
// }

///매크로
/// 선언적 매크로
// fn main() {
//     let v:Vec<u32> = vec![1,2,3]
// }

// #[macro_export]
// macro_rules! vec {

//     ($($x:expr), *) => {
//         {
//             let mut temp_vec = Vec::new();
//             $(
//                 temp_vec.push($x);
//             )*
//             temp_vec
//         }

//     };
// }

/// 절차적 매크로
use hello_macro::HelloMacro;
use hello_macro_derive::HelloMacro;

#[derive(HelloMacro)]
struct Pancakes;

fn main() {
    Pancakes::hello_macro();
}
