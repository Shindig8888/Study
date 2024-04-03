//##변수##

// fn main() {
//     let x = 5;
//     println!("The value of x is:{x}");
    
//     x = 6;
//     println!("The value of x is:{x}");
    
// } //불변변수 x의 값을 변경하려고해서 오류 발생

// fn main() {
//     let mut x = 5;
//     println!("The value of x is:{x}");
    
//     x = 6;
//     println!("The value of x is:{x}");
    
// }

//##상수##
// 항상 불변, 상수표현식으로만 설정
//const THREE_HOURS_IN_SECOND: u32 = 60*60*3
//선언된 스코프 내 프로그램이 작동하는 전체 시간동안 유효

//##섀도잉##
// fn main() {
//     let x = 5;
//     let x = x+1; // x변수 재성정
//     {
//         let x = x*2; // 스코프 안에서 섀도잉
//         println!("The value of x in the inner scope is:{x}");

//     }
//     println!("The value of x is :{x}");
// }
//섀도잉으로 다른 타입을 지정가능, mut은 불가능
// let spaces = " ";
// let spaces = spaces.len();
//  let mut spaces = " ";
//  spaces = spaces.len();


//###데이터 타입###

//##스칼라 타입## : 하나의 값

// #정수형 : 소수점이 없는 숫자 기본 i32#
// i = +-
// u = +만

// #부동소수점 타입 f32, f64 기본 f64#
// fn main(){
//     let x = 2.0; //f64
//     let y: f32 =3.0; // f32
// }

// #수치연산#
// fn main(){
//     //덧셈
//     let sum = 50+10;

//     //뺄셈
//     let difference = 95.5 - 4.3;

//     //곱셈
//     let product = 4*30;

//     //나눗셈
//     let quotient = 56.7 /32.2;
//     let truncated = -5/3; // 정수나눗셈

//     //나머지연산
//     let remainder = 43 % 5;
// }

//#불리언#
// let f: bool = false;
// let f: bool = true;

//#문자타입
// let c = 'z'
// let z:char = 'Z'
// 작은따옴표, 4바이트, 유니코드 커버


//##복합타입##

//#튜플#
//고정된길이
// fn main() {
//     let tup: (i32, f64, u8) = (500, 6.4, 1);
// }

// fn main() {
//     let tup = (500, 6.4, 1);

//     let (x, y, z) = tup;

//     println!("The valure of y is {y}");
// }

// fn main() {
//     let x: (i32, f64, u8) = (500, 6.4, 1)
//     let five_hundred = x.0;
//     let six_point_four = x.1;
//     let one = x.2
// }
// 빈 튜플은 유닛이라는 이름을 가짐

//#배열 타입#
//러스트는 배열(리스트)도 고정된 길이를 가짐, 모두가 같은 타입이어야함

// fn main() {
//     let a = [1,2,3,4,5];
// }

// 길이가 고정되지 않길 원하면 벡터사용(추후 학습)

// let a: [i32; 5] = [1,2,3,4,5]; // 배열은 타입을 [타입; 길이]로 지정
// let a: [5;5] // 초깃값 5인 5자리배열 [5,5,5,5,5]

//#배열요소에 접근
// fn main(){
//     let a = [1,2,3,4,5];

//     let first = a[0]; // 1
//     let second = a[1]; // 2

// }

//#유효하지않은 배열요소에 접근

use std::io;

fn main() {
    let a = [1,2,3,4,5];

    println!("Please enter an array index");

    let mut index = String::new();

    io::stdin()
        .read_line(&mut index)
        .expect("Failed to read line");

    let index:usize = index
        .trim()
        .parse()
        .expect("Index entered was not a number");

    let element = a[index];

    println!("The value of the element at index {index} is: {element}");
}