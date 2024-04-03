//2-1

use rand::Rng; //난수 생성기를 구현한 메서드들을 정의한 트레이드
use std::cmp::Ordering; // 열거형 비교 cmp=>두 값을 비교, Ordering =>Less, Greater, Equal 베리언트를 가짐
use std::io; // 입력 트레이드


fn main() { // 프로그램의 진입점
    println!("Guess the number!"); //문자열을 화면에 출력하는 매크로

    let secret_number = rand::thread_rng()/*난수생성기를 제공*/.gen_range(1..=100)/*표현식을 인수로 받음, start..=end */; 

    println!("The secret number is : {secret_number}");
    loop {
        println!("Please input your guess.");

        let mut guess = String::new(); //변수 생성, mutable, String=>표준라이브러리의 확장가능한 문자열타입, ::로 new()함수;새로운값을 만드는 함수;

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");
        
        let guess: u32 = match guess.trim()/*공백과 줄바꿈제거 */.parse()/*문자열을 다른 타입으로 바꿔줌 */{ //match표현식으로 바꿔 에러-종료가 아닌 에러 처리로 변경 parse()가 Ok Err값을 반환 (_)은 모든값(포괄값)
            Ok(num) => num,
            Err(_) => continue,
        };
        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!"); //guess와 secret_number을 비교하여 나온 Ordering 값에 따라 프린트
                break;
            }
        }
    }
}

//Cargo.toml [dependencies]에 rand = "0.8.5"추가; rand크레이트의 0.8.5버전 이상을 불러오기
//추가되면 Cargo.lock에 rand 관련 크레이트가 기록됨 cargo update로 lock을 무시하고 업데이트 가능

// error[E0308]: mismatched types
//    --> src\main.rs:25:21
//     |
// 25  |     match guess.cmp(&secret_number) {
//     |                 --- ^^^^^^^^^^^^^^ expected `&String`, found `&{integer}`
//     |                 |
//     |                 arguments to this method are incorrect
//     |
//     = note: expected reference `&String`
//                found reference `&{integer}` ===>quess가 string, secret_number가 int 이기때문에 미스매치