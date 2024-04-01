//###ch1,2###
// 코멘트
///문서화
/* 코드 중간에 주석 */

//###ch3###
// fn main() {
//     i8, i16, i32, i64, i128, isize
//     u8, u16, u32, u64, u128, usize
//     /*bits : 8bit = 1byte
//     //isize ==> 컴퓨터 운영체제에 따른 사이즈
//     //32-bit isize == i32*/
// }

// fn main() {
//     let my_number:u8 = 100; /*디폴트는 i32*/
//     let my_other_number = 200;
//     let third_number = my_number + my_other_number; /*다른 타입은 연산이 안됨*/
// }

//type inference

//###ch4###
// fn main() {
//     println!("Hello, World");
//     let first_letter = 'A';
//     let space = ' ';
//     let my_number:u16 = 8;
//     let second_number:u8 = 10;
//     let third_number = my_number + second_number as u16;/*casting*/
// }


// "" => string
// '' => char = 4bytes

// fn main() {
//     let my_number = 'a' as u8;
//     println!("Hello World! My number is {}", my_number)
// }

// a를 u8 숫자로 썼을 때의 숫자가 출력 이것도 캐스팅
//간단한 타입에서만 가능능


//###ch5###
// use std::mem::size_of;
// fn main() {
//     println!("Size of a char: {} bytes", size_of::<char>());
//     // println!("Size of a char: {}", std::mem::size_of::<char>()); // 4 bytes
//     println!("Size of string containing 'a': {}", "a".len()); // .len() gives the size of the string in bytes
//     println!("Size of string containing 'ß': {}", "ß".len());
//     println!("Size of string containing '国': {}", "国".len());
//     println!("Size of string containing '𓅱': {}", "𓅱".len());
// }

//rust에서 .len()은 바이트의 길이를 말함함

// fn main() {
//     let slice = "Hello!";
//     println!("Slice is {} bytes and also {} characters.", slice.len(), slice.chars().count());
//     let slice2 = "안녕!";
//     println!("Slice2 is {} bytes but only {} characters.", slice2.len(), slice2.chars().count());
// }
// string 의 한 글자 글자를 char로 변환해서 slice.chars().count로


//###ch6###
// fn main(){
//     let my_number = 9_u8; /*_를 안넣어도됨*/
//     let other_number = 100_000_000_000_u64;
// }
//파이썬이랑 비슷

fn main(){
    let my_number = 9.6; //f64
    let other_number = 9; //i32
    println!("{}", my_number + other_number as f64)

    /*float는 보통 f64를 사용*/
}