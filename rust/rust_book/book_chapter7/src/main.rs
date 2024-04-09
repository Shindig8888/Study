//크레이트: 러스트가 한번의 컴파일 시에 고려하는 가장 작은 코드 단위
//바이너리 크레이트: main()을 가지는 컴파일가능한 프로그램
//라이브러리 크레이트: 기능들이 정의된 크레이트
//패키지: 번들
//main.rs는 Cargo.toml에 적시되지는않음, src/main.rs가 크레이트 루트, 라이브러리크레이트는 src/lib.rs

// //보편적인 use 경로 작성법 으로부터
// use std::collections::HashMap;

// fn main() {
//     let mut map = HashMap::new();
//     map.insert(1,2);
// } // lib.rs로

// use rand::Rng;

// fn main() {
//     let secret_number = rand::thread_rng().gen_range(1..=10);
//     println!("{}", secret_number);
// }

//중첩 경로를 사용하여 대량의 use 나열
// use std::cmp::Ordering;
// use std::io;
// //를
// use std::{cmp::Ordering, io}; //와 같이 표현가능

// use std::io;
// use std::io::Write; //는

// use std::io::{self, Write}; //과 같이 표현가능

// 모두 가져오려면:
// use std::collections::*;