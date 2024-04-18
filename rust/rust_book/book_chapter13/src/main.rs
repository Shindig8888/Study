//클로저: 자신의 환경을 캡처하는 익명 함수

// #[derive(Debug, PartialEq, Copy, Clone)]
// enum ShirtColor {
//     Red,
//     Blue,
// }

// struct Inventory {
//     shirts: Vec<ShirtColor>

// }

// impl  Inventory {
//     fn giveaway(&self, user_preference: Option<ShirtColor>) -> ShirtColor {
//         user_preference.unwrap_or_else(|| self.most_stocked()) // 매개변수가 없는 클러져, 표현식이 하나일때만 중괄호 생략가능
//     }

//     fn most_stocked(&self) -> ShirtColor {
//         let mut num_red = 0;
//         let mut num_blue = 0;

//         for color in &self.shirts {
//             match color {
//                 ShirtColor::Red => num_red += 1,
//                 ShirtColor::Blue=>num_blue += 1,
//             }
//         }
        
//         if num_red > num_blue {
//             ShirtColor::Red
//         } else {
//             ShirtColor::Blue
//         }
//     }
// }

// fn main() {
//     let store = Inventory {
//         shirts: vec![ShirtColor::Blue, ShirtColor::Red, ShirtColor::Blue],
//     };

//     let user_pref1 = Some(ShirtColor::Red);
//     let giveaway1 = store.giveaway(user_pref1);
//     println!("The user with preference {:?} gets {:?}", user_pref1, giveaway1);
    
//     let user_pref2 = None;
//     let giveaway2 = store.giveaway(user_pref2);
//     println!("The user with preference {:?} gets {:?}", user_pref2, giveaway2);


// }


//클로저와 함수
// fn add_one_1(x:u32) -> u32{ x+1 }
// fn main() {
//     let add_one2 = |x:u32| -> u32{ x+1 };
//     let add_one3 = |x|{ x+1 };
//     let add_one4 = |x| x+1;
// }

//클로저는 하나의 타입만 추론가능
// fn main() {
//     let example_closure = |x| x;

//     let s = example_closure(String::from("hello"));
//     let n = example_closure(5);
// }

//참조자 캡처
// fn main() {
//     let mut list = vec![1,2,3];
//     println!("Before defining closure: {:?}", list);

//     let mut only_borrows = || list.push(7);
//     //가변클로저일경우 클로저 정의와 호출 사이에 다른 클로저가 위치할 수 없음; 가변대여이기 때문
//     only_borrows(); // 클로저를 함수처럼 call
//     println!("After calling closure: {:?}", list);
// }

//closure가 소유권을 가지도록 move사용
// use std::thread;

// fn main() {
//     let list = vec![1,2,3];
//     println!("Before defininf closure: {:?}", list);

//     thread::spawn(move || { //스레드(이후 학습)를 사용하기 위해서는 소유권 이전이 필요
//         println!("From thread:{:?}", list)
//     }).join().unwrap();
// }

//캡처된 값을 클로저 밖으로 이동하기, fn 트레이드

//FnOnce
//Option<T>의 unwrap_or_else 정의
// impl <T> Option<T> {
//     pub fn unwrap_or_else<F>(self, f:F) -> T
//     where
//         F:FnOnce() -> T
//     {
//         match self {
//             Some(x) => x,
//             None +> F(),
//         }
//     }
// }

//FnMut
// #[derive(Debug)]
// struct Rectangle {
//     width: u32,
//     height: u32,
// }

// fn main() {
//     let mut list = [
//         Rectangle {width:10, height:1,},
//         Rectangle {width:3, height:5,},
//         Rectangle {width:7, height:12,},
//     ];
//     list.sort_by_key(|r| r.width);
//     println!("{:#?}", list)
// }

//반복자
// fn main() {
//     let v1 = vec![1,2,3];
//     let v1_iter = v1.iter();

//     for val in v1_iter {
//         println!("Got: {}", val);
//     }
// }

//.next()
// #[test]
// fn iterator_demonstration() {
//     let v1 = vec![1,2,3];

//     let mut v1_iter = v1.iter(); // next()는 반복자를 소비하기때문에 mut

//     assert_eq!(v1_iter.next(), Some(&1)); // next()로 반환된 값은 참조자이기 때문에 Some(&1)
//     assert_eq!(v1_iter.next(), Some(&2));
//     assert_eq!(v1_iter.next(), Some(&3));
//     assert_eq!(v1_iter.next(), None); 
// }

//반복자를 소비하는 메서드(next를 호출하는 메서드들)
// #[test]
// fn iterator_sum() {
//     let v1 = vec![1,2,3];

//     let v1_iter = v1.iter();

//     let total:i32 = v1_iter.sum(); // sum()은 내부적으로 next()호출 // 다만 이때는 mut필요없음

//     assert_eq!(total, 6);
// }

//다른 반복자를 생성하는 매서드
//반복자를 소비하지 않음
// fn main() {
//     let v1: Vec<i32> = vec![1,2,3];
//     v1.iter().map(|x| x+1); // 반복자는 소비되지않으면 아무영향이 없음
//     let v2: Vec<i32> = v1.iter().map(|x| x+1).collect(); // collect()로 소비하면서 벡터 변환
//     println!("{:?}", v2);
// }

//환경을 캡처하는 클로저
// #[derive(PartialEq, Debug)]
// struct Shoe {
//     size: u32,
//     style: String,
// }

// fn shoes_in_size(shoes: Vec<Shoe>, shoe_size:u32) -> Vec<Shoe> {
//     shoes.into_iter().filter(|s| s.size == shoe_size).collect()
// }

// #[cfg(test)]
// mod tests {
//     use super::*;

//     #[test]
//     fn filters_by_size() {
//         let shoes = vec![
//             Shoe{
//                 size:10,
//                 style: String::from("sneaker"),
//             },
//             Shoe{
//                 size:13,
//                 style: String::from("snadal"),
//             },
//             Shoe{
//                 size:10,
//                 style: String::from("boot"),
//             },
            
//         ];

//         let in_my_size = shoes_in_size(shoes, 10);

//         assert_eq!(
//             in_my_size,
//             vec![Shoe{
//                 size:10,
//                 style: String::from("sneaker"),
//             },
//             Shoe{
//                 size:10,
//                 style: String::from("boot"),
//             },
//             ]
//         )
//     }
// }

