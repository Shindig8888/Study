// fn main() {
//     const WARP_FACTRP: f64 = 9.9;
// }

//scope
// fn main() {
//     let x = 5;
//     {
//         let y = 99;
//         println!("{}, {}", x, y);
//     }
//     // println!("{},{}", x, y);
// }

//섀도잉: 다른 타입으로도 가능


// memory saftey

// fn main() {
//     let enigma:i32; // 값을 가져야함
//     if true {
//         enigma = 42;
//     } else {
//         enigma = 7;
//     } // 빈틈이 없으므로 에러발생 x
//     println!("{}", enigma);
// }

//excercise A

//functions

// fn main() {
//     let x = do_stuff(2.0, 12.5);
//     println!("{}", x)
// }

// fn do_stuff(qty:f64, oz:f64) -> f64 {
//     println!("{} {}-oz sarsaparilla(s)!", qty, oz);
//     //return qty*oz; // return ;
//     qty*oz // tail exprettion
// } // function은 위치에 상관없음

// excersise B

// Module System
// fn main() {
//     sction2::greet();
// }

use sction2::greet;

fn main() {
    greet();
}




