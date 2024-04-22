//스마트 포인터:String, Vec<T> 등

//Box<T>=>스택대신 힙에 저장

// fn main() {
//     let b = Box::new(5);
//     println!("b={}", b);
// }

//콘스 리스트: 재귀적, 무한한 크기의 타입
// use crate::List::{Cons, Nil};
// enum List {
//     Cons(i32, List),
//     Nil,
// }

// fn main() {
//     let list = Cons(1, Cons(2, Cons(3, (Nil)))); // 재귀적 베리언트를 이용해 List를 정의했기때문에 에러
// }

// //비재귀적타입의 공간 계산
// enum Message {
//     //어떤 베리언트가 가장 큰 공간을 필요로 하는지 확인
//     Quit, //0
//     Move{x:i32, y:i32}, //2개의 i32값
//     Write(String), //...
//     ChangeColor(i32, i32, i32),//......
// }

//Box<T>
// enum List {
//     Cons(i32, Box<List>),
//     Nil
// }

// use crate::List::{Cons, Nil};

// fn main(){
//     let list = Cons(1, Box::new(Cons(2, Box::new(Cons(3, Box::new(Nil))))));
// }

// //Deref 트레이트
// fn main() {
//     let x = 5;
//     let y = Box::new(x);
//     assert_eq!(5, x);
//     assert_eq!(5, *y); //Box사용시 y는 x의 참조값
// }

//자체 스마트 포인터 정의
// struct MyBox<T>(T);

// impl<T> MyBox<T> {
//     fn new(x:T)->MyBox<T> {
//         MyBox(x)
//     }
// }

// fn main() {
//     let x = 5;
//     let y = MyBox::new(x);

//     assert_eq!(5, x);
//     assert_eq!(5, *y); // MyBox에 Deref트레이트가 구현되지 않음

// }

//Deref
// use std::ops::Deref;
// struct MyBox<T>(T);

// impl<T> MyBox<T> {
//     fn new(x:T)->MyBox<T> {
//         MyBox(x)
//     }
// }

// impl<T> Deref for MyBox<T> {
//     type Target = T;

//     fn deref(&self) -> &Self::Target {
//         &self.0
//     }
// }

// fn main() {
//     let x = 5;
//     let y = MyBox::new(x);

//     assert_eq!(5, x);
//     assert_eq!(5, *y);

// }

//역참조 강제
// fn hello(name:&str) {
//     println!("Hello, {name}!")
// }

// fn main() {
//     let m = MyBox::new(String::from("Rust")); //Deref트레이트가 구현되어있다면
//     hello(&m)//자동으로 &String을 &str로 변환
// }

//역참조 강제가 가변성과 상호작용하는법
//T:Deref<Target=U> 일 때 &T에서 &U로
//T:DerefMut<Target=U>일 때 &mut T에서 &mut U로
//T:Deref<Target=U>일 때 &mut T에서 &U로

//Drop 트레이트

// struct CustomSmartPointer {
//     data:String,
// }

// impl Drop for CustomSmartPointer {
//     fn drop(&mut self) {
//         println!("Dropping CustomSmartPointer with data '{}'!", self.data);
//     }
// }

// fn main() {
//     let c = CustomSmartPointer {
//         data:String::from("my stuff"),
//     };
//     let d = CustomSmartPointer {
//         data: String::from("other stuff")
//     };
//     println!("CustomSmartPointers create.");
// }

//값 일찍 버리기
// struct CustomSmartPointer {
//     data: String,
// }

// impl Drop for CustomSmartPointer {
//     fn drop(&mut self) {
//         println!("Dropping CustomSmartPointer with data '{}'!", self.data);
//     }
// }

// fn main() {
//     let c = CustomSmartPointer {
//         data: String::from("my stuff"),
//     };
//     println!("CustomSmartPointers create.");
//     drop(c); // 구현한 drop function은 명시적으로 호출할 수 없고, std::mem::drop함수를 이용해 간접적으로 함수를 실행시켜야함
//     println!("CustomSmartPointer dropped before the end of main");
// }

//Rc<T>: 소유권의 공유

// enum List {
//     Cons(i32, Rc<List>),
//     Nil,
// }

// use crate::List::{Cons, Nil};
// use std::rc::Rc;

// fn main() {
//     let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
//     let b = Cons(3, Rc::clone(&a));
//     let c = Cons(4, Rc::clone(&a));
// }

//Rc<T>는 참조자 카운트 증가

// enum List {
//     Cons(i32, Rc<List>),
//     Nil,
// }

// use crate::List::{Cons, Nil};
// use std::rc::Rc;

// fn main() {
//     let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
//     println!("count after creating a = {}", Rc::strong_count(&a));
//     let b = Cons(3, Rc::clone(&a));
//     println!("count after creating b = {}", Rc::strong_count(&a));
//     {
//         let c = Cons(4, Rc::clone(&a));
//         println!("count after creating c = {}", Rc::strong_count(&a));
//     }
//     println!("count after c goes out of scope = {}", Rc::strong_count(&a));
// }

//RefCell<T>와 내부가변성패턴

use std::cell::RefCell;
use std::rc::Rc;

fn main() {
    // Box<T>의 사용 예제
    let boxed_int: Box<i32> = Box::new(42);
    println!("Boxed integer: {}", boxed_int);

    // Rc<T>의 사용 예제
    let rc_string1 = Rc::new(String::from("Hello"));
    let rc_string2 = Rc::clone(&rc_string1);
    println!(
        "Reference count of rc_string1: {}",
        Rc::strong_count(&rc_string1)
    );

    // RefCell<T>의 사용 예제
    let refcell_data = RefCell::new(10);
    {
        let mut borrowed_data = refcell_data.borrow_mut();
        *borrowed_data += 5;
    }
    println!("RefCell data after mutation: {:?}", refcell_data.borrow());
}
