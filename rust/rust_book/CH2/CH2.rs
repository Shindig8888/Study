//2-1

use std::io;

fn main() { // 프로그램의 진입점
    println!("Guess the number!"); //문자열을 화면에 출력하는 매크로

    println!("Please input your guess.");

    let mut guess = String::new(); //변수 생성, mutable, String=>표준라이브러리의 확장가능한 문자열타입, ::로 new()함수;새로운값을 만드는 함수;

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    println!("You guessed: {guess}");


}