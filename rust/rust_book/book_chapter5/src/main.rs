//구조체 = attribute

//#구조체 정의 및 인스턴스화

// struct User {
//     active: bool,
//     username: String,
//     email: String,
//     sign_in_count: u64,
// }
// 구조체 인스턴스 생성(순서는 상관없음)
// fn main(){
//     let user1 = User {
//         active: true,
//         username: String::from("someusername123"),
//         email: String::from("someone@example.com"),
//         sign_in_count: 1,
//     };
//     println!("{0}", user1.email);
// }

// 가변 인스턴스 email 필드값 변경
// fn main() {
//     let mut user1 = User {
//         active: true,
//         username: String::from("someusername123"),
//         email: String::from("someone@example.com"),
//         sign_in_count: 1,
//     };
//     user1.email = String::from("anotheremail@example.com");
//     println!("{0}", user1.email);
// }

// fn build_user(email: String, username:String) -> User{ // 반환타입 명시
//     User { 
//         active: true, 
//         username, // username: username, ; 변수명과 필드명이 같음
//         email, //email: email,
//         sign_in_count: 1, }
// }

// //구조체 업데이트(승계)
// fn main() {
//     let user1 = User {
//                 active: true,
//                 username: String::from("someusername123"),
//                 email: String::from("someone@example.com"),
//                 sign_in_count: 1,
//             };
//     //user2를 생성하면 user1을 사용할 수 없음(String); 정확히는 user1.username과 user1.email을 사용불가
//     let user2 = User {
//         email : String::from("another@example.com"),
//         ..user1
//     };
//     println!("{}", user1.sign_in_count);
// }

//명명된 필드 없는 튜플 구조체를 사용해 다른

// struct Color(i32, i32, i32);
// struct Point(i32, i32, i32);

// fn main() {
//     let black = Color(0,0,0);
//     let origin = Point(0,0,0);
// }

//필드가 없는 유사 유닛 구조체

// struct AwaysEqual;
// fn main() {
//     let subject = AwaysEqual;
// }

//필드구성 : {} 튜플 () 유사유닛: 

//구조체 예제

//각 변수에 지정된 너비와 높이로 사각형 넓이 계산

// fn main() {
//     let width1 = 30;
//     let height1 = 50;

//     println!(
//         "The area of the rectangle is {} square pixels.",
//         area(width1, height1)
//     );
// }

// fn area(width:u32, height: u32) -> u32 {
//     width*height
// }
//=>튜플로
// fn main() {
//     let rect1 = (30,50);

//     println!(
//         "The area of the rectangle is {} square pixels.",
//         area(rect1)
//     );
// }

// fn area(dimensions:(u32, u32)) -> u32 {
//     dimensions.0 * dimensions.1
// }
//튜플로 작성해 명료해졌으나, 튜플 내 요소에 대한 정보를 확인불가능 ==>구조체로 리팩터링

//구조체정의

// #[derive(Debug)]
// struct Rectangle {
//     width: u32,
//     height: u32,
// }

// fn main() {
//     let scale= 2;
    
// //구조체인스턴스
//     let rect1 = Rectangle {
//         width: dbg!(30*scale),
//         height: 50,
//     };
//     //구조체인스턴스의 출력 : 
//     // println!("rect1 is {}", rect1);
//     // `Rectangle` cannot be formatted with the default formatter
//     // println!("rect1 is {:?}", rect1);
//     // `Rectangle` doesn't implement `Debug` ==> 구조체에 외부 속성을 추가해야됨; 디버깅에 대한 명시적 동의
//     // println!("rect1 is {:?}", rect1);
//     dbg!(&rect1);
// //출력
//     println!(
//         "The area of the rectangle is {} square pixels."
//         , area(&rect1)
//     );
// }
// //함수
// fn area(rectangle: &Rectangle) -> u32 {
//     rectangle.width * rectangle.height
// }
// //변수들이 모두 u32라 borrow할필요는 없지만, 그래도 혹시모르니 참조


//메서드 문법

#[derive(Debug)]
struct Rectangle {
    width : u32,
    height : u32,
}

// impl Rectangle { // Rectanle 구조체의 콘텍스트에 함수를 정의, 구현
//     fn area(&self) -> u32 { // 매개변수 self: &Self
//         self.width * self.height
//     }
// } //파이썬의 클래스 내 함수정의와 비슷함

// fn main() {
//     let rect1 = Rectangle {
//         width: 30,
//         height: 50,
//     };

//     println!(
//         "The area of the rectangle is {} square pixels.",
//         rect1.area()
//     );
// }

//필드와 메서드 이름이 중복될 때
// impl Rectangle {
//     fn width(&self) -> bool {
//         self.width>0
//     }
// }

// fn main() {
//     let rect1 = Rectangle {
//         width: 30,
//         height: 30,
//     };

//     if rect1.width() { // 메서드로서의 width: .width()
//         println!("The rectangle has a nonzero width; it is {}", rect1.width) //필드로서의 width: rect1.width 괄호없음
//     }
// }


//# 더 많은 매개변수를 가진 메서드

// impl Rectangle{
//     fn area(&self) -> u32 {
//         self.width * self.height
//     }
//     fn can_hold(&self, other:&Rectangle) -> bool {
//         self.width > other.width && self.height > other.height
//     }
// }
// fn main() {
//     let rect1 = Rectangle {
//         width: 30,
//         height: 50,
//     };
//     let rect2 = Rectangle {
//         width: 10,
//         height: 40,
//     };
//     let rect3 = Rectangle {
//         width: 60,
//         height: 45,
//     };
//     println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
//     println!("Can rect1 hold rect3? {}", rect1.can_hold(&rect3));

// }

//#메서드가 아닌 연관 함수
// Rectangle 내 필드를 함수 내에서 사용하지는 않고, 오히려 함수를 Rectangle의 필드로 사용함
// impl Rectangle {
//     fn square(size:u32) -> Self {
//         Self {
//             width: size,
//             height: size,
//         }
//     }
// }

// 호출할때는 let sq = Rectangle::square(3)

//#여러개의 impl 블록

// impl Rectangle {
//     fn area(&self) -> u32 {
//         self.width * self.height
//     }
// }

// impl Rectangle {
//     fn can_hold(&self, other: &Rectangle) -> bool {
//         self.width > other.width && self.height > other.height
//     }
    
// }

//블록을 나눠도됨

