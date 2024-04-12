//러스트의 에러: recovaerable, unrecoverable

//panic! macro
//*프로그램 내 결과 바이너리를 작게 만들고 싶다면 Cargo.toml [profile/release]섹션에 panic = 'abort'추가 */

// fn main() {
//     panic!("crash and burn");
// }

//panic 백트레이스
// fn main() {
//     let v = vec![1, 2, 3];

//     v[99]; // buffer overread
// }

//Result로 복구가능한 에러 처리

// enum Result<T, E> {
//     Ok(T),
//     Err(E),
// }

// use std::fs::File;

// fn main() {
//     let greeting_file_result = File::open("heelo.txt");

//     let greeting_file = match greeting_file_result {
//         Ok(file) => file,
//         Err(error) => panic!("Problem opening the file : {:?}", error),
//     };
// }

//서로 다른 에러 매칭

// use std::fs::File;
// use std::io::ErrorKind;

// fn main() {
//     let greeting_file_result = File::open("hello.txt");

//     let greeting_file = match greeting_file_result {
//         Ok(file) => file,
//         Err(error) => match error.kind() {
//             ErrorKind::NotFound => match File::create("hello.txt") {
//                 Ok(fc) => fc,
//                 Err(e) => panic!("Problem creating the file: {:?}", e),
//             },
//             other_error => {
//                 panic!("Problem opening the file: {:?}", other_error);
//             }
//         },
//     };
// }

//Result<T, E>와 match에 대한 대안

// use std::fs::File;
// use std::io::ErrorKind;

// fn main() {
//     let greeting_file = File::open("hello.txt").unwrap_or_else(|error| {
//         if error.kind() == ErrorKind::NotFound {
//             File::create("hello.txt").unwrap_or_else(|error| {
//                 panic!("Problem creating the file : {:?}", error);
//             })
//         } else {
//             panic!("Problem opening the file : {:?}", error);
//         }
//     });
// }

//unwrap과 expect

// use std::fs::File;
// fn main() {
//     let greeting_file = File::open("hello.txt").unwrap(); // 기본패닉 메시지
// }

// fn main() {
//     let greeting_file = File::open("hello.txt")
//         .expect("hello.txt should be included in this project"); // 사용자 설정 메시지
// }

//에러 전파

// use std::fs::File;
// use std::io::{self, Read};

// fn read_username_from_file() -> Result<String, io::Error> {
//     let username_file_result = File::open("hello.txt");

//     let mut username_file = match username_file_result {
//         Ok(file) => file,
//         Err(e) => return Err(e),
//     };

//     let mut username = String::new();

//     match username_file.read_to_string(&mut username) {
//         Ok(_) => Ok(username),
//         Err(e) => Err(e), // 마지막코드이기때문에 서둘러 끝낼필요가없음; return생략
//     }
// }

//에러전파 - ?연산자

// use std::fs::File;
// use std::io::{self, Read};

// fn read_username_from_file() -> Result<String, io::Error> {
//     let mut username_file = File::open("hello.txt")?; // 알아서 match, 에러를 반환타입에 맞게 변환
//     let mut username = String::new();
//     username_file.read_to_string(&mut username)?;
//     Ok(username)
// }

// use std::fs::{read_to_string, File};
// use std::io::{self, Read};

// fn read_username_from_file() -> Result<String, io::Error> {
//     let mut username = String::new();

//     File::open("hello.txt")?/read_to_string(&mut username)?;

//     Ok(username)
// }

// use std::fs;
// use std::io;

// fn read_username_from_file() {
//     fs::read_to_string("hello.txt") // 파일을 열지 않아도 자동으로
// }

//?연산자가 사용될 수 있는 곳: 호환 가능한 반환 타입을 가진 함수에서만 사용; Result<>, Option<>(섞어서는 사용불가능)

// use std::fs::File;

// fn main() {
//     let greeting_file = File::open("hello.txt")?; // main함수는 반환 타입이 Result가 아니라 ()
// }

// use std::error::Error;
// use std::fs::File;

// fn main() ->Result<(), Box<dyn Error>> {
//     let greeting_file = File::open("hello.txt")?;

//     Ok(())
// }

// panic!과 Result
//panic!: 복구 불가능, 실패할지도 모르는 함수를 정의할 때는 Result 반환, 보안을위해 설정