// mod front_of_house {
//     mod hosting {
//         fn add_to_waitlist() {}

//         fn seat_at_table() {}
//     }
//     mod serving {
//         fn take_order() {}
//         fn serve_order() {}
//         fn take_payment() {}
//     }
// } // 네스팅하여 디렉토리 구성

// mod front_of_house {
//     pub mod hosting {
//         pub fn add_to_waitlist() {}
//     }
// }

// pub fn eat_at_restaurant() {
//     crate::front_of_house::hosting::add_to_waitlist();

//     front_of_house::hosting::add_to_waitlist();
// } // 형제모듈에는 pub없이 접근가능, 형제모듈의 자녀모듈에는 pub이 있어야 접근가능

// //super
// fn deliver_order() {}

// mod back_of_house {
//     fn fix_incorrect_order() {
//         cook_order();
//         super::deliver_order();
//     }
//     fn cook_order() {}
// }

//구조체, 열거형 공개

//구조체
// mod back_of_house {
//     pub struct Breakfast {
//         pub toast:String,//pub된 구조체 내에서도 필드를 공개하려면 이렇게
//         seasonal_fruit: String, // 필드 공개되지않음
//     }
//     impl Breakfast {
//         pub fn summer(toast: &str) -> Breakfast {
//             Breakfast {
//                 toast: String::from(toast),
//                 seasonal_fruit: String::from("peaches"),
//             }
//         }
//     } 
// }

// pub fn eat_at_restaurant() {
//     let mut meal = back_of_house::Breakfast::summer("Rye");
//     meal.toast = String::from("Wheat");
//     println!("I'd like {} toast please", meal.toast);
//     //비공개필드 seasonal_fruit는 수정 및 조회불가
//     // meal.seasonal_fruit = String::from("BlueBerries")
// }

// //열거형
// mod back_of_house {
//     pub enum Appetizer {  //열거형은 전부공개
//         Soup,
//         Salad,
//     }
// }

// pub fn eat_at_restaurant() {
//     let order1 = back_of_house::Appetizer::Soup;
//     let order2 = back_of_house::Appetizer::Salad;
// }

// //use로 모듈을 스코프안으로 가져오기
// mod front_of_house {
//     pub mod hosting {
//         pub fn add_to_waitlist(){}
//     }
// }

// use crate::front_of_house::hosting;
// pub fn eat_at_restaurant() {
//     hosting::add_to_waitlist();
// }

// //보편적인 use 경로 작성법
// mod front_of_house {
//     pub mod hosting {
//         pub fn add_to_waitlist(){}
//     }
// }

// use crate::front_of_house::hosting::add_to_waitlist;
// pub fn eat_at_restaurant() {
//     add_to_waitlist();
// }//main.rs에서 설명이어감

// // 동일한 이름의 아이템을 여럿 가져오는 경우에는 이 방식을 사용하지 않음
// use std::fmt;
// use std::io;

// fn function() -> fmt::Result {
//     //
// }

// fn function2() -> io::Result<()> {
//     //
// }

// //동일한 이름인 경우 as를 사용해도됨
// use std::fmt::Result;
// use std::io::Result as IoResult;

// fn function() -> Result {
//     //
// }

// fn function2() -> IoResult<()> {
//     //
// }

// // pub use로 다시 내보내기
// mod front_of_house {
//     pub mod hosting {
//         pub fn add_to_waitlist() {}
//     }
// }

// pub use crate::front_of_house::hosting;

// pub fn eat_at_restaurant(){
//     hosting::add_to_waitlist();//pub use 자체를 경로로 사용가능
// }

//별개의 파일로 모듈 분리
mod front_of_house;// 형제 모듈 front_of_house 모드 사용

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
} 