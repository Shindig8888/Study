// 열거형과 패턴 매칭

//열거형: 어떤 값이 여러 개의 가능한 값의 집합중 하나라는 것을 나타냄
//사용가능한 베리언트를 모두 열거할 수 있을 때

// enum IpAddrKind {
//     V4,
//     V6,
// }

// struct IpAddr {
//     kind: IpAddrKind,
//     address: String,
// }

// let home = IpAddr {
//     kind: IpAddrKind:: V4,
//     address: String::from("127.0.0.1"),
// };

// let loopback = IpAddr {
//     kind: IpAddrKind::V6,
//     address: String::from("::1"),
// };
// fn main() {
//     let four = IpAddrKind::V4;
//     let six = IpAddrKind :: V6;
// }

// fn route (ip_kind : IpAddrKind) {}

//각 열거형 베리언트에 데이터를 직접 넣는 방식(구조체를 사용하지 않고)
// fn main() {

//     enum IpAddr {
//         V4(u8, u8, u8, u8),
//         V6(String), //구조체로는 하나를 다ㅇ른타입으로 성정 물가능
//     }

//     let home = IpAddr::V4(String::from("127.0.0.1"));
//     let loopback = IpAddr::V6(String::from("::1"));

// }

//구조체를 먼저 정의하고 열거하는 방식(표준라이브러리)

// use std::net::Ipv6Addr;

// struct Ipv4Addr {
//     //생략
// }
// struct Ip64Addr {
//     //생략
// }

// enum IpAddr {
//     V4(Ipv4Addr),
//     V6(Ipv6Addr),
// }

//열거형 예제

// enum Message {
//     Quit, // 연관된 데이터 없음
//     Move { x:i32, y:i32}, //x, y 이름을 가지는 구조체형식
//     Write(String), // 하나의 String
//     ChangeColor(i32, i32, i32), // 세개의 i32
// }

//구조체로 표현하면:
// struct QuitMessage; // 유닛 구조체
// struct MoveMessage {
//     x:i32, 
//     y:i32,
// } 
// struct WriteMessage(String); // 튜플구조체
// struct ChangeColorMessage(i32, i32, i32); // 튜플구조체

//열거형 impl
// impl Message {
//     fn call(&self) {
//         //메서드 정의
//     }
// }
// fn main() {
//     let m = Message::Write(String::from("hello"));
//     m.call();
// }

//Option 열거형: 값이 없거나 있을 수 있는 상황
//러스트에서는 null이 없음

// enum Option<T> {
//     None,
//     Some(T),
// }
// //가장 기본적, 정의하지 않아도 되고, Option::을 붙이지 않고 사용해도 작동함

// fn main() {
//     let some_number = Some(5); // Option<i32>
//     let some_char = Some('e'); // Option<char>
//     let absent_number: Option<i32> = None;
// }

//Option<T>와 T는 다른값
// fn main() {
//     let x: i8 = 5;
//     let y:Option<i8> = Some(5); // 명시적으로 Null일때 수행을 지정해주고 Option<i8>을 i8로 변환해야 x와 연산가능
//     let sum = x+y;
// }

// fn main() {
//     let x: i8 = 5;
//     let y: Option<i8> = Some(5); // 명시적으로 Null일때 수행을 지정해주고 Option<i8>을 i8로 변환해야 x와 연산가능

//     // Option<i8> 타입에서 값을 추출해서 i8로 변환
//     let y_value = match y {
//         Some(val) => val,
//         None => 0, // 만약 None이라면 기본값으로 0을 사용하거나 원하는 값을 지정할 수 있습니다.
//     };

//     // 추출한 값과 x를 더합니다.
//     let sum = x + y_value;
//     println!("Sum: {}", sum);
// }

//match 제어 흐름 구조=>match는 동전분류기

// enum Coin {
//     Penny,
//     Nickel,
//     Dime,
//     Quarter,
// }

// fn value_in_cents(coin:Coin) {
//     match coin {
//         Coin::Penny => {
//             println!("Luckey Penny!");
//             1
//         }
//         Coin::Nickel => 5,
//         Coin::Dime => 10,
//         Coin::Quarter => 25,
//     }
// }

//값을 바인딩하는 패턴

// #[derive(Debug)]
// enum UsState {
//     Alabama,
//     Aslaska,
// }

// enum Coin {
//     Penny,
//     Nickel,
//     Dime,
//     Quarter(UsState), // 바인딩
// }

// fn value_in_cents(coin:Coin) -> u8 {
//     match coin {
//         Coin::Penny => 1,
//         Coin::Nickel => 5,
//         Coin::Dime => 10,
//         Coin::Quarter(state) => { // 바인딩
//             println!("State quarter from {:?}!", state);
//             25
//         }
//     }
// }


// //Option<T>를 사용하는 매칭
// fn plus_one(x:Option<i32>)->Option<i32> {
//     match x {
//         //모든 케이스를 다뤄야 함!
//         None => None,
//         Some(i) => Some(i+1),
//     }
// }

// fn main() {
//     let five = Some(5);
//     let six = plus_one(five);
//     let none = plus_one(None);
// }//Option<i32>의 연산



// //포괄패턴과 _자리표시자

// fn main() {
//     let dice_roll = 9;
//     match dice_roll {
//         3 => add_fancy_hat(),
//         7 => remove_fancy_hat(),
//         // other => move_player(other), // 포괄패턴
//         // _ => reroll(), //어떤 값이라도 매칭되지만 값을 바인딩하지않음
//         _ => (), // 3과 7이외의 어떤값이 나와도, 아무것도 하지않음
//     }
// }

// fn add_fancy_hat() {}
// fn remove_fancy_hat() {}
// // fn move_player(num_spaces: u8) {}
// // fn reroll() {}

// //if let
// fn main() {
//     let config_max = Some(3u8);
//     match config_max {
//         Some(max) =>println!("The maximum is configured to be {}", max),
//         _=>(), //match를 이용할 경우 None값을 따로 처리해줘야함
//     }
// }
// fn main(){
//     let config_max = Some(3u8);
//     if let Some(max) = config_max {
//         println!("The maximum is configured to be {}", max);
//     }
// } // 한 패턴에 매칭될 경우만, match보다 덜 엄격함, else를 사용해서 이외의 경우도 설정가능
