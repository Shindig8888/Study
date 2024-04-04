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

// use std::io;

// fn main() {
//     let a = [1,2,3,4,5];

//     println!("Please enter an array index");

//     let mut index = String::new();

//     io::stdin()
//         .read_line(&mut index)
//         .expect("Failed to read line");

//     let index:usize = index
//         .trim()
//         .parse()
//         .expect("Index entered was not a number");

//     let element = a[index];

//     println!("The value of the element at index {index} is: {element}");
// }

//##함수
// fn main() {
//     println!("Hello, world");
//     another_function();
// }

// fn another_function() {
//     println!("Another functiion.")
// }
//another function이 main다음에 정의
//러스트는 함수 위치를 고려하지 않음

//#매개변수(parameter)
// fn main(){
//     another_function(5);
// }

// fn another_function(x:i32) { //x가 매개변수
//     println!("The calue of x is: {x}");
// }


// fn main() {
//     print_labeled_measurement(5, 'h');
// }

// fn print_labeled_measurement(value: i32, unit_label:char) {
//     println!("The measurement is : {value}{unit_label}");
// }

//구문과 표현식

//구문 : 어떤 동작을 수행하고 값을 반환하지 않는 명령
// fn main() {
//     let y = 6; // 값을 반환하지 않음
// }

//표현식 : 결과값을 평가
// fn main() {
//     let y = {
//         let x = 3;
//         x + 1 // 표현식의 종결은 세미콜론을 사용하지않음
//     };

//     println!("The value of y is : {y}")
// }

//#반환값을 갖는 함수
// fn five() -> i32 {
//     5
// }
// fn main(){
//     let x = five();
//     println!("The value of x is : {x}")
// }

// fn main(){
//     let x = plus_one(5);
//     print!("The value of x is : {x}");
// }

// fn plus_one(x:i32) -> i32 {
//     x+1 // 세미콜론을 사용하지않음
// }

//##제어 흐름
//# if
// fn main(){
//     let number = 3;
//     if number <1 {
//         println!("condition was true");
//     } else {
//         println!("condition was false");
//     }
// }

//#다중 else if
// fn main() {
//     let number = 6;
//     if number % 4 == 0 {
//         println!("number is divided by 4");
//     } else if number %3 ==0{
//         println!("number is divided by 3");
//     } else if number %3 ==0{
//         println!("number is divided by 2");
//     } else {
//         println!("number is not devided by 4, 3 or 2");
//     }
// }

//# let 구문에서 if 사용
// fn main() {
//     let condition = true;
//     let number = if condition {5} else {6};

//     println!("The value of number is : {number}");
// }
//타입호환이 안되는경우
// fn main() {
//     let condition = true;
//     let number = if condition {5} else {'six};

//     println!("The value of number is : {number}");
// }

//#반복문
// fn main() {
//     let mut counter = 0;
//     let result = loop {
//         counter += 1;

//         if counter == 10 {
//             break counter *2;
//         }
//     };
//     println!("The result is {result}")
    
// }
//루프 라벨
// fn main() {
//     let mut count = 0;
//     'counting_up: loop {
//         println!("count = {count}");
//         let mut remaing = 10;

//         loop {
//             println!("remaing = {remaing}");
//             if remaing == 9 {
//                 break;
//             }
//             if count == 2{
//                 break 'counting_up;
//             }
//             remaing -= 1;
//         }
//         count += 1;
//     }
//     println!("End count = {count}");
// }

//#while 조건 반복문
// fn main() {
//     let mut number = 3;

//     while number != 0 {
//         println!("{number}");

//         number -= 1;
//     }
//     println!("LIFTOFF!!!");
// }

//#for

// fn main(){
//     let a  = [10,20,30,40,50];

//     for element in a {
//         println!("the values is : {element}")
//     }
// }

// fn main(){
//     for number in (1..4).rev() { // rev():역순
//         println!("{number}!");
//     }
//     println!("LIFTOFF!!!")
// }


//###과제

//1. 화씨, 섭씨 온도 간 변화

// use std::io;

// fn main() {
//     println!("Ferenhite Celcius Calulator");
    
//     println!("Enter f or c");
//     let mut temperature_type = String::new();
//     io::stdin()
//         .read_line(&mut temperature_type)
//         .expect("Failed to read line");

//     println!("Enter temperature");
//     let mut temperature_degree = String::new();
//     io::stdin()
//         .read_line(&mut temperature_degree)
//         .expect("Failed to read line");
//     let temperature_degree: f64 = temperature_degree.trim().parse().expect("Failed to read line");


//     let result: f64 = if temperature_type.trim() == "f" {
//         (temperature_degree-32.0)/1.8
//         } else {
//         temperature_degree*1.8+32.0
//     };
    
//     println!("Your temperature in another type is : {result}");
// }

//#2. n번째 피보나치 수 생성하기

// use std::io;
// fn main() {
//     println!("fibonacci number generator!");
//     let mut end: bool = true;
//     while end {
//         println!("Enter number");
//         let mut fibo_number = String::new();
//         io::stdin()
//             .read_line(&mut fibo_number)
//             .expect("Failed to read line");
//         let fibo_number: i32 = fibo_number.trim().parse().expect("Failed to read line");
//         let result_number: i32 = fibo(fibo_number);

//         println!("the {fibo_number}th fibonacci number is : {result_number}");
//         println!("\nwanna do it again? : y/n");
//         let mut try_again = String::new();
//         io::stdin()
//             .read_line(&mut try_again)
//             .expect("Failed to read line");
//         if try_again.trim() == "n" {
//             end = false
//         }
//     }
// }


// fn fibo(n:i32)->i32 {
//     let mut count = 0;
//     let mut first = 1;
//     let mut second = 1;
//     let mut result = 0;
//     if n == 1{
//         result = 1
//     } else if n == 2 {
//         result = 2
//     } else {
//         while count !=n-2 {
//             result = first + second;
//             count += 1;
//             first = second;
//             second = result;
//         }
//     }
//     result
// }

//#3. twelve days of Christmas

// fn main() {
//     let days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "nineth", "tenth", "eleventh", "twelveth"];
//     let comments = ["A partridge in a pear tree" ,"Two turtle doves", "Three French hens", "four calling birds", "five gold rings", "six geese a-laying", "seven swans a-swimming", "eight maids a-milking", "nine ladies dancing", "ten lords a-leaping", "eleven pipers piping", "twelve drummers drumming"];

//     for i in 1..=12 {
//         let index_days = days[i-1]; 
//         println!("On the {index_days} of Christmas my true love sent me\n");
//         for j in 1..=i {
//             let index_comment = comments[j-1];
//             println!("{index_comment}\n");

//             }
//         println!("\n\n")
//         }
        
// }