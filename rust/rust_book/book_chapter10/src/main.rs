// 함수로 추출하여 중복 ㅇ벗애기

// fn main() {
//     let number_list = vec![34, 50, 25, 100, 65];

//     let mut largest = &number_list[0];

//     for number in &number_list {
//         if number > largest {
//             largest = number;
//         }
//     }
//     println!("The largest number is {}", largest)
// }

// 함수를 계속 써야할 때

// fn largest(list: &[i32]) -> &i32 {
//     let mut largest = &list[0];

//     for item in list {
//         if item > largest {
//             largest = item;
//         }
//     }
//     largest
// }

// fn main() {
//     let number_list = vec![34, 50, 25, 100, 65];

//     let result = largest(&number_list);
//     println!("The largest number is {}", result);

//     let number_list = vec![102, 34,6000, 89, 54, 2, 43, 8];


//     let result = largest(&number_list);
//     println!("The largest number is {}", result);
// }

//제네릭 데이터 타입

// fn largest_i32(list:&[i32]) -> &i32 {
//     let mut largest = &list[0];

//     for item in list {
//         if item> largest{
//             largest = item; 
//         }
//     }
//     largest
// }

// fn largest_char(list:&[char]) -> &char {
//     let mut largest = &list[0];

//     for item in list {
//         if item> largest{
//             largest = item; 
//         }
//     }
//     largest
// }

// fn main() {
//     let number_list = vec![34, 50, 25, 100, 65];
//     let result = largest_i32(&number_list);
//     println!("The largest number is {}", result);

//     let char_list = vec!['y', 'm', 'a', 'q'];
//     let result = largest_char(&char_list);
//     println!("The largest char is {}", result);
// } // 중복이 심함

//제네릭타입 매개변수

// fn largest<T>(list:&[T]) -> &T {
//     let mut largest = &list[0];

//     for item in list {
//         if item > largest { // 타입값이 비교가능할 경우에만 실행가능, 컴파일에러
//             largest = item;
//         }
//     }
//     largest
// }

// fn main() {
//     let number_list = vec![34, 50, 25, 100, 65];
//     let result = largest(&number_list);
//     println!("The largest number is {}", result);

//     let char_list = vec!['y', 'm', 'a', 'q'];
//     let result = largest(&char_list);
//     println!("The largest char is {}", result);
// }

//제네릭 구조체 정의

// struct Point<T> {
//     x: T,
//     y: T,
// }

// fn main() {
//     let interger = Point {x: 5, y: 10};
//     let float = Point {x:1.0, y:4.0}; // 임의의 제너릭타입 T에 대해서는 x, y가 모두 동일한 타입이어야함
// }

//////

// struct Point<T, U> {
//     x: T,
//     y: U,
// }

// fn main() {
//     let both_interger = Point { x:5, y:10};
//     let both_float = Point{x:1.0, y: 4.0};
//     let interger_and_float = Point{x:5, y:4.0};
// } // x, y를 서로다른 타입으로 설정가능
//열거형도 마찬가지

//제네릭 메서드 정의

// struct Point<T> {
//     x: T,
//     y: T,
// }

// impl<T> Point<T> {
//     fn x(&self) -> &T { // x()함수정의
//         &self.x // &self.x반환
//     }
// }

// fn main() {
//     let p = Point {x:5, y:10};
//     println!("p.x = {}", p.x());
// }

//특정 타입인경우에만 적용되는 impl
//제너릭타입 T에 대한 구조체 정의 후:

// impl Point<f32> {
//     fn distance_from_origin(&self) -> f32 {
//         (self.x.powi(2)+self.y.powi(2)).sqrt()
//     }
// } // 제네릭 타입 T가 f32인 경우에만 적용

// struct Point<X1, Y1> {
//     x: X1,
//     y: Y1,
// }

// impl <X1, Y1> Point<X1, Y1> { // X1, Y2는 구조체에 정의, impl시작을 구조체와 연관지어 정의하는 역할
//     fn mixup<X2, Y2>(self, other: Point<X2, Y2>) -> Point<X1, Y2> { //함수와 연관된 X2, Y2 정의
//         Point {
//             x:self.x,
//             y: other.y,
//         }
//     }
// }

// fn main() {
//     let p1 = Point {x:5, y:10.4};
//     let p2 = Point{x: "Hello", y:'c'};

//     let p3 = p1.mixup(p2);

//     println!("p3.x = {}, p3.y = {}", p3.x, p3.y);
// }


//제네릭 코드는 단형성화를 통해 성능이 떨어지지않음
// enum Option_i32 {
//     Some(i32),
//     None,
// }

// enum Option_f64 {
//     Some(f64),
//     None,
// }

// fn main() {
//     let interger = Option_i32::Some(5);
//     let float = Option_f64::Some(5.0);
// }

//트레이트 정의
// pub trait  Summary {
//     fn summarize(&self) -> String;
// }

//특정 타입에 트레이트 구현하기

// use std::fmt::format;

// pub struct NewArticle {
//     pub headline: String,
//     pub location: String,
//     pub author: String,
//     pub content: String,
// }

// impl Summary for NewsArticle {
//     fn summarize(&self) -> String {
//         format!("{}, ny {} ({})", self.headline, self.author, self.location)
//     }
// }

// pub struct Tweet {
//     pub username: String,
//     pub content: String,
//     pub reply: bool,
//     pub retweet: bool,
// }

// impl Summary for Tweet {
//     fn summarize(&self) -> String {
//         format!("{}: {}", self.username, self.content)
//     }
// } -->라이브러리로

//트레이트로 사용


// use aggregator::{Summary, Tweet};
// fn main() {
//     let tweet = Tweet {
//         username: String::from("horse_ebooks"),
//         content: String::from(
//             "of course, as you probably already know, people",
//         ),
//         reply: false,
//         retweet: false,
//     };
//     println!("1 new tweet: {}", tweet.summarize());
// }

//

// //라이프타임
// fn main() {
//     let r;

//     {
//         let x = 5;
//         r = &x;
//     }

//     println!("r:{}", r);
// } // 재정의된 r의 lifetime이 맨처음 정의된 r의 lifetime보다 짧음

// //함수에서의 제네릭 라이프타임

// fn main() {
//     let string1 = String::from("abcd");
//     let string2 = "xyz";

//     let result = longest(string.as_str(), string2);
//     println!("The longgest is {}", result);
// }

// fn longest(x:&str, y:&str)-> &str {
//     if x.len() > y.len() {
//         x
//     } else {
//         y
//     }
// } // x를 반환할지, y를 반환할 지 알 수 없는데, 둘 다 스코프에 갇혀있기 때문에 라이프타임 명시 필요

// fn main() {
//     let string1 = String::from("abcd");
//     let string2 = "xyz";

//     let result = longest(string1.as_str(), string2);
//     println!("The longgest is {}", result);
// }

// fn longest<'a>(x:&'a str, y:&'a str)-> &'a str { // 두개의 매개변수가 유효한 동안에는 반환값도 유효, 함수 시그니쳐에 명시
//     if x.len() > y.len() {
//         x
//     } else {
//         y
//     }
// }

//서로 다른 구체적인 라이프탐을 가진 String값의 참조자

// fn main() {
//     let string1 = String::from("long string is long");
//     let result;
//     {
//         let string2 = String::from("xyz");
//         result = longest(string1.as_str(), string2.as_str());
//     }
//     println!("The longest string is {}", result);
// }

// fn longest<'a>(x:&'a str, y:&'a str)-> &'a str { // 두개의 매개변수가 유효한 동안에는 반환값도 유효, 함수 시그니쳐에 명시
//     if x.len() > y.len() {
//         x
//     } else {
//         y
//     }
// }

//라이프타임의 측면에서 생각하기

// fn longest<'a>(x:&'a str, y:&str) -> &'a str {// y는 리턴값과 상관없기 때문에 라이프타임을 지정하지 않음
//     x
// } 

//구조체 정의에서 라이프타임

// struct ImportantExcerpt<'a> {
//     part:&'a str,
// }

// fn main() {
//     let novel = String::from("Call me Ishmael. Some years ago...");
//     let first_sentence = novel.split('.').next().expect("Could not find a '.'");
//     let i = ImportantExcerpt {
//         part: first_sentence,
//     };
// }

//라이프타임 생략

// fn first_word(s:&str) -> &str {
//     let bytes = s.as_bytes();
//     for (i, &item)in bytes.iter().enumerate()() {
//         if item == b' ' {
//             return &s[0..i];
//         }
//     }
//     &s
// } // 예측가능한 상황이세는 라이프타임생략규칙


//메서드 정의에서 라이프타임 명시하기

// struct ImportantExcerpt<'a> {
//     part:&'a str,
// }

// impl<'a> ImportantExcerpt<'a> {
//     fn level(&self)->i32 {
//         3
//     }
// }

// impl<'a> ImportantExcerpt<'a> {
//     fn announce_and_return_part(&self, announcement: &str)-> &str {
//         println!("Attention pleas: {}", announcement);
//         self.part
//     }
// }

// fn main() {
//     let novel = String::from("Call me Ishmael. Some years ago...");
//     let first_sentence = novel.split('.').next().expect("Could not find a '.'");
//     let i = ImportantExcerpt {
//         part: first_sentence,
//     };
// }

//정적 라이프타임

// let s:&'static str = "I have a static lifetime";//프로그램 전체 생애주기동안 살아있음


//집약

use std::fmt::Display;

fn longest_with_an_announcement<'a, T> (
    x: &'a str,
    y: &'a str,
    ann: T,
 ) -> 'a &str
where
    T:Display,
{
    println!("Announcement! {}", ann);
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

