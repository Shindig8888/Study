// pub fn add(left: usize, right: usize) -> usize {
//     left + right
// }

// #[cfg(test)]
// mod tests {
//     use super::*;

//     #[test] // 테스트 함수임을 명시
//     fn exploration() {
//         assert_eq!(2+2, 4);
//     }
//     #[test]
//     fn another() {
//         panic!("Make this test fail!")
//     }
// }

//assert!
// #[derive(Debug)]
// struct Rectangle {
//     width: u32,
//     height: u32,
// }

// impl Rectangle {
//     fn can_hold(&self, other: &Rectangle)->bool {
//         self.width > other.width && self.height > other.height
//     }
// }

// #[cfg(test)]
// mod tests {
//     use super::*;

//     #[test] // 테스트 함수임을 명시
//     fn larger_can_hold_smaller() {
//         let larger = Rectangle {
//             width: 8,
//             height: 7,
//         };

//         let smaller = Rectangle {
//             width: 5,
//             height: 1,
//         };

//         assert!(!smaller.can_hold(&larger));
//     }
// }

//assert_eq!, assert_ne!

// pub fn add_two(a:i32) -> i32 {
//     a + 2
// }
// #[cfg(test)]
// mod tests {
//     use super::*; // 외부함수

//     #[test] // 테스트 함수임을 명시
//     fn it_adds_two() { //테스트함수명 선언
//         assert_eq!(4, add_two(2)) // 4가 add_two 와 같은지 테스트
//     }
// }
//assert_ne!()는 같지않음일때
// pub fn greeting(name: &str) -> String {
//     format!("Hello")
// }

// #[cfg(test)]
// mod tests {
//     use super::*;

//     #[test]
//     fn greeting_contains_name() {
//         let result = greeting("Carol");
//         assert!(
//             result.contains("Carol"),
//             "Greeting did not contain name, value was '{}'", result
//         );
//     }
// }


//should_panic 매크로
// pub struct Guess {
//     value: i32,
// }

// impl Guess {
//     pub fn new(value:i32) -> Guess {
//         if value <1 {
//             panic!("Guess value must be greater than or equal to 1, got {}", value);
//         } else if value > 100 {
//             panic!("Guess value must be less than or equal to 100, got {}", value);
//         }
//         Guess { value }
//     }
// }


// #[cfg(test)]
// mod tests {
//     use super::*;

//     #[test]
//     #[should_panic(expected = "less than or equal to 100")] // 패닉이 일어나면 통과
//     fn greater_than_100() {
//         Guess::new(200);
//     }
// }


//Result<T,E>를 이용한 테스트
// #[cfg(test)]
// mod test {
//     #[test]
//     fn it_works() -> Result<(), String> {
//         if 2+2 == 4 {
//             Ok(())
//         } else {
//             Err(String::from("Two plus two does not equal four"))
//         }
//     }
// }

//테스트 실행 방법 제어
//cargo test는 기본적으로 테스트모드 바이너리를 병렬로 실행
// cargo test -- --test-threads=1: 병렬처리 제어

//함수 출력 표시하기
// fn print_and_returns_10(a:i32)->i32 {
//     println!("I got the value {}", a);
//     10
// }

// #[cfg(test)]
// mod tests {
//     use super::*;

//     #[test]
//     fn this_test_will_pass() {
//         let value = print_and_returns_10(4);
//         assert_eq!(10, value);
//     }

//     #[test]
//     fn this_test_will_fail() {
//         let value = print_and_returns_10(8);
//         assert_eq!(5, value);
//     }
// }

//cargo test this_test_will_fail 처럼 이름을 지정해서 실행 가능
//[test] 아래에 [ignore]추가, cargo test -- --ignored 명령어 사용하면 무시된것만, cargo test -- --include-ignored 실행하면 모든 테스트

//테스트 조직화
//유닛테스트: src 디렉터리 내 각 파일에 테스트 대상이 될 코드와 함께 작성
//통합테스트는 [cfg(test)] 가 필요없음
//테스트 경로에 대해서는 301쪽 확인
//통합 테스트에서는 use root 사용, 모듈 분리 가능

//바이너리 크레이트에서는 함수노출이 불가능